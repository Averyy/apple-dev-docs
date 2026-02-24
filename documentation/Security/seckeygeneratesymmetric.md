# SecKeyGenerateSymmetric(_:_:)

**Framework**: Security  
**Kind**: func

Generates a random symmetric key.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecKeyGenerateSymmetric(_ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

#### Return Value

A newly generated symmetric key, or `NULL` on failure. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free the key’s memory when you are done with it.

## Parameters

- `parameters`: A key generation parameter dictionary. At minimum, this must contain [`kSecAttrKeyType`](ksecattrkeytype.md) and [`kSecAttrKeySizeInBits`](ksecattrkeysizeinbits.md). In addition, this function assumes default values for the following keys: - [`kSecAttrLabel`](ksecattrlabel.md) defaults to `NULL`.
- [`kSecAttrIsPermanent`](ksecattrispermanent.md) if this key is present and has a value of [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), the key or key pair will be added to the default keychain.
- [`kSecAttrApplicationTag`](ksecattrapplicationtag.md) defaults to `NULL`.
- [`kSecAttrEffectiveKeySize`](ksecattreffectivekeysize.md) defaults to `NULL`, which means the effective key size is the same as the key size ([`kSecAttrKeySizeInBits`](ksecattrkeysizeinbits.md)).
- [`kSecAttrCanEncrypt`](ksecattrcanencrypt.md) defaults to [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) for private keys, [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for public keys.
- [`kSecAttrCanDecrypt`](ksecattrcandecrypt.md) defaults to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for private keys, [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) for public keys.
- [`kSecAttrCanDerive`](ksecattrcanderive.md) defaults to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue).
- [`kSecAttrCanSign`](ksecattrcansign.md) defaults to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for private keys, [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) for public keys.
- [`kSecAttrCanVerify`](ksecattrcanverify.md) defaults to [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) for private keys, [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for public keys.
- [`kSecAttrCanWrap`](ksecattrcanwrap.md) defaults to [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) for private keys, [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for public keys.
- [`kSecAttrCanUnwrap`](ksecattrcanunwrap.md) defaults to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for private keys, [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) for public keys. These default values can be overridden by adding a value for the associated key in the parameter dictionary. When used as a replacement for [`SecKeyGenerate`](seckeygenerate.md), set the [`kSecUseKeychain`](ksecusekeychain.md) key to the keychain ([`SecKeychain`](seckeychain.md)) into which the key should be stored, [`kSecAttrLabel`](ksecattrlabel.md) to a user-visible label for the key, and [`kSecAttrApplicationLabel`](ksecattrapplicationlabel.md) to an identifier defined by your application, for subsequent use in calls to [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md). Additionally, you can specify keychain access controls for the key by setting [`kSecAttrAccess`](ksecattraccess.md) to a [`SecAccess`](secaccess.md) object.
- `error`: A pointer to a [`CFError`](https://developer.apple.com/documentation/CoreFoundation/CFError) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygeneratesymmetric(_:_:))*