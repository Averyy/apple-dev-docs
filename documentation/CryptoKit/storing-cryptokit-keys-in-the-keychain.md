# Storing CryptoKit Keys in the Keychain

**Framework**: Apple CryptoKit

Convert between strongly typed cryptographic keys and native keychain types.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- Xcode 11.0+

#### Overview

CryptoKit defines highly specific key types that embody a particular cryptographic algorithm and purpose. Some of these key types, like [`P256.Signing.PrivateKey`](p256/signing/privatekey.md), correspond to items that the [`Keychain services`](https://developer.apple.com/documentation/security/keychain-services) API stores natively as [`SecKey`](https://developer.apple.com/documentation/security/seckey) instances. Other key types, like [`Curve25519.Signing.PrivateKey`](curve25519/signing/privatekey.md), have no direct keychain corollary. To store these kinds of keys, you package them as generic passwords.

This sample code project demonstrates the conversions needed to store all the CryptoKit key types in the keychain.

##### 3369555

The sample provides targets for both iOS and macOS. For both platforms, specify your developer team in the Xcode Signing & Capabilities tab before building. The macOS target also sets the [`Keychain Access Groups Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/keychain-access-groups), to enable access to the keychain on that platform.

##### 3369556

[`Keychain services`](https://developer.apple.com/documentation/security/keychain-services) lets you convert between [`SecKey`](https://developer.apple.com/documentation/security/seckey) instances and data in the X9.63 data format. For NIST keys that support that representation, like [`P256`](p256.md), [`P384`](p384.md), and [`P521`](p521.md), CryptoKit defines a property that you use to get the X9.63 data. The framework also provides a complementary initializer that creates a new key from data in that format.

Define a protocol called `SecKeyConvertible` to express this interface:

```swift
protocol SecKeyConvertible: CustomStringConvertible {
    /// Creates a key from an X9.63 representation.
    init<Bytes>(x963Representation: Bytes) throws where Bytes: ContiguousBytes
    
    /// An X9.63 representation of the key.
    var x963Representation: Data { get }
}
```

Then assert that all the NIST private keys adopt this protocol:

```swift
extension P256.Signing.PrivateKey: SecKeyConvertible {}
extension P256.KeyAgreement.PrivateKey: SecKeyConvertible {}
extension P384.Signing.PrivateKey: SecKeyConvertible {}
extension P384.KeyAgreement.PrivateKey: SecKeyConvertible {}
extension P521.Signing.PrivateKey: SecKeyConvertible {}
extension P521.KeyAgreement.PrivateKey: SecKeyConvertible {}
```

##### 3369557

[`Keychain services`](https://developer.apple.com/documentation/security/keychain-services) also lets you securely store small chunks of data as a generic password keychain item. For any CryptoKit key without a X9.63 representation, CryptoKit provides a means to obtain a data representation of the key, enabling generic password storage. Define the `GenericPasswordConvertible` protocol to establish an interface for these items:

```swift
protocol GenericPasswordConvertible: CustomStringConvertible {
    /// Creates a key from a raw representation.
    init<D>(rawRepresentation data: D) throws where D: ContiguousBytes
    
    /// A raw representation of the key.
    var rawRepresentation: Data { get }
}
```

Some keys, like [`Curve25519`](curve25519.md), adopt this interface directly, and you simply assert that they do:

```swift
extension Curve25519.KeyAgreement.PrivateKey: GenericPasswordConvertible {}
extension Curve25519.Signing.PrivateKey: GenericPasswordConvertible {}
```

Other keys offer similar functionality, but require modest adjustments to their interface. For example, you provide a secure conversion for instances of [`SymmetricKey`](symmetrickey.md):

```swift
extension SymmetricKey: GenericPasswordConvertible {
    init<D>(rawRepresentation data: D) throws where D: ContiguousBytes {
        self.init(data: data)
    }
    
    var rawRepresentation: Data {
        return dataRepresentation  // Contiguous bytes repackaged as a Data instance.
    }
}
```

Keys that you store in the Secure Enclave expose a raw representation as well, but in this case the data isn’t the raw key. Instead, the Secure Enclave exports an encrypted block that only the same Secure Enclave can later use to restore the key. You can adopt the same convertibility protocol to store the Secure Enclave’s encrypted data in the keychain as a generic password, and later allow the Secure Enclave to reconstruct the key on the same device:

```swift
extension SecureEnclave.P256.Signing.PrivateKey: GenericPasswordConvertible {
    init<D>(rawRepresentation data: D) throws where D: ContiguousBytes {
        try self.init(dataRepresentation: data.dataRepresentation)
    }
    
    var rawRepresentation: Data {
        return dataRepresentation  // Contiguous bytes repackaged as a Data instance.
    }
}
```

##### 3369558

To store a NIST key in the keychain, create a storage method that constrains input keys to be of type `SecKeyConvertible`:

```swift
func storeKey<T: SecKeyConvertible>(_ key: T, label: String) throws {
```

Then call the [`SecKeyCreateWithData(_:_:_:)`](https://developer.apple.com/documentation/security/seckeycreatewithdata(_:_:_:)) function with the X9.63 representation of the key to create a [`SecKey`](https://developer.apple.com/documentation/security/seckey) instance. Include attributes that describe the key as a private, elliptic-curve key.

```swift
// Describe the key.
let attributes = [kSecAttrKeyType: kSecAttrKeyTypeECSECPrimeRandom,
                  kSecAttrKeyClass: kSecAttrKeyClassPrivate] as [String: Any]

// Get a SecKey representation.
guard let secKey = SecKeyCreateWithData(key.x963Representation as CFData,
                                        attributes as CFDictionary,
                                        nil)
    else {
        throw KeyStoreError("Unable to create SecKey representation.")
}
```

Store the [`SecKey`](https://developer.apple.com/documentation/security/seckey) representation in the keychain by placing it in an add query and calling the [`SecItemAdd(_:_:)`](https://developer.apple.com/documentation/security/secitemadd(_:_:)) function. Give the key a label to make it easier to find later.

```swift
// Describe the add operation.
let query = [kSecClass: kSecClassKey,
             kSecAttrApplicationLabel: label,
             kSecAttrAccessible: kSecAttrAccessibleWhenUnlocked,
             kSecUseDataProtectionKeychain: true,
             kSecValueRef: secKey] as [String: Any]

// Add the key to the keychain.
let status = SecItemAdd(query as CFDictionary, nil)
guard status == errSecSuccess else {
    throw KeyStoreError("Unable to store item: \(status.message)")
}
```

##### 3369559

To store other kinds of keys, create a different storage method that constrains input keys to be of type `GenericPasswordConvertible`:

```swift
func storeKey<T: GenericPasswordConvertible>(_ key: T, account: String) throws {
```

In this case, you provide the raw representation as the data for the password item, and store that with a call to the [`SecItemAdd(_:_:)`](https://developer.apple.com/documentation/security/secitemadd(_:_:)) function:

```swift
// Treat the key data as a generic password.
let query = [kSecClass: kSecClassGenericPassword,
             kSecAttrAccount: account,
             kSecAttrAccessible: kSecAttrAccessibleWhenUnlocked,
             kSecUseDataProtectionKeychain: true,
             kSecValueData: key.rawRepresentation] as [String: Any]

// Add the key data.
let status = SecItemAdd(query as CFDictionary, nil)
guard status == errSecSuccess else {
    throw KeyStoreError("Unable to store item: \(status.message)")
}
```

##### 3369560

You retrieve a key from the keychain using a call to the [`SecItemCopyMatching(_:_:)`](https://developer.apple.com/documentation/security/secitemcopymatching(_:_:)) function. Construct a query dictionary that pinpoints the particular key that you want to find. After your search returns the desired key—stored as a [`SecKeychainItem`](https://developer.apple.com/documentation/security/seckeychainitem) instance—you cast it as a [`SecKey`](https://developer.apple.com/documentation/security/seckey) instance.

```swift
// Seek an elliptic-curve key with a given label.
let query = [kSecClass: kSecClassKey,
             kSecAttrApplicationLabel: label,
             kSecAttrKeyType: kSecAttrKeyTypeECSECPrimeRandom,
             kSecUseDataProtectionKeychain: true,
             kSecReturnRef: true] as [String: Any]

// Find and cast the result as a SecKey instance.
var item: CFTypeRef?
var secKey: SecKey
switch SecItemCopyMatching(query as CFDictionary, &item) {
case errSecSuccess: secKey = item as! SecKey
case errSecItemNotFound: return nil
case let status: throw KeyStoreError("Keychain read failed: \(status.message)")
}
```

> **Note**: The above query returns the first elliptic-curve key with the given label found in the user’s keychain. You might need to perform a more sophisticated search if more than one key might match, as described in [`Storing Keys in the Keychain`](https://developer.apple.com/documentation/security/storing-keys-in-the-keychain).

The above query returns the first elliptic-curve key with the given label found in the user’s keychain. You might need to perform a more sophisticated search if more than one key might match, as described in [`Storing Keys in the Keychain`](https://developer.apple.com/documentation/security/storing-keys-in-the-keychain).

After you get the [`SecKey`](https://developer.apple.com/documentation/security/seckey) reference, initialize a CryptoKit key using the X9.63 representation returned by the [`SecKeyCopyExternalRepresentation(_:_:)`](https://developer.apple.com/documentation/security/seckeycopyexternalrepresentation(_:_:)) function.

```swift
// Convert the SecKey into a CryptoKit key.
var error: Unmanaged<CFError>?
guard let data = SecKeyCopyExternalRepresentation(secKey, &error) as Data? else {
    throw KeyStoreError(error.debugDescription)
}
let key = try T(x963Representation: data)
```

Make sure that the type of the key that you initialize using the data matches the type of the original key. For example, initializing a [`P256`](p256.md) key from the data corresponding to a keychain item that you created using a [`P384`](p384.md) key produces undefined results.

##### 3369561

You also retrieve generic passwords using the  [`SecItemCopyMatching(_:_:)`](https://developer.apple.com/documentation/security/secitemcopymatching(_:_:)) function, in this case using [`kSecClassGenericPassword`](https://developer.apple.com/documentation/security/ksecclassgenericpassword) for the item’s class. You convert the returned item to data, and use it directly to instantiate a key of the corresponding type:

```swift
// Seek a generic password with the given account.
let query = [kSecClass: kSecClassGenericPassword,
             kSecAttrAccount: account,
             kSecUseDataProtectionKeychain: true,
             kSecReturnData: true] as [String: Any]

// Find and cast the result as data.
var item: CFTypeRef?
switch SecItemCopyMatching(query as CFDictionary, &item) {
case errSecSuccess:
    guard let data = item as? Data else { return nil }
    return try T(rawRepresentation: data)  // Convert back to a key.
case errSecItemNotFound: return nil
case let status: throw KeyStoreError("Keychain read failed: \(status.message)")
}
```

As long as the type you initialize matches the type that you previously used to store the item in the keychain, the initialization correctly reconstructs the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/storing_cryptokit_keys_in_the_keychain)*