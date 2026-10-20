# SecKeyGenerateSymmetric(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Generates a random symmetric key.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: No longer supported

## Declaration

```swift
func SecKeyGenerateSymmetric(_ parameters: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

```c
SecKeyRefSecKeyGenerateSymmetric(CFDictionaryRef parameters, CFErrorRef*error);
```

#### Return Value

A newly generated symmetric key, or `NULL` on failure. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free the key’s memory when you are done with it.

## Parameters

- `parameters`: A key generation parameter dictionary. At minimum, this must contain [`kSecAttrKeyType`](./ksecattrkeytype.md) and [`kSecAttrKeySizeInBits`](./ksecattrkeysizeinbits.md). In addition, this function assumes default values for the following keys:

  - [`kSecAttrLabel`](./ksecattrlabel.md) defaults to `NULL`.
  - [`kSecAttrIsPermanent`](./ksecattrispermanent.md) if this key is present and has a value of [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), the key or key pair will be added to the default keychain.
  - [`kSecAttrApplicationTag`](./ksecattrapplicationtag.md) defaults to `NULL`.
  - [`kSecAttrEffectiveKeySize`](./ksecattreffectivekeysize.md) defaults to `NULL`, which means the effective key size is the same as the key size ([`kSecAttrKeySizeInBits`](./ksecattrkeysizeinbits.md)).
  - [`kSecAttrCanEncrypt`](./ksecattrcanencrypt.md) defaults to [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) for private keys, [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) for public keys.
  - [`kSecAttrCanDecrypt`](./ksecattrcandecrypt.md) defaults to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) for private keys, [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) for public keys.
  - [`kSecAttrCanDerive`](./ksecattrcanderive.md) defaults to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md).
  - [`kSecAttrCanSign`](./ksecattrcansign.md) defaults to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) for private keys, [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) for public keys.
  - [`kSecAttrCanVerify`](./ksecattrcanverify.md) defaults to [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) for private keys, [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) for public keys.
  - [`kSecAttrCanWrap`](./ksecattrcanwrap.md) defaults to [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) for private keys, [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) for public keys.
  - [`kSecAttrCanUnwrap`](./ksecattrcanunwrap.md) defaults to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) for private keys, [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) for public keys.

  These default values can be overridden by adding a value for the associated key in the parameter dictionary.

  When used as a replacement for [`SecKeyGenerate`](./seckeygenerate.md), set the [`kSecUseKeychain`](./ksecusekeychain.md) key to the keychain ([`SecKeychain`](./seckeychain.md)) into which the key should be stored, [`kSecAttrLabel`](./ksecattrlabel.md) to a user-visible label for the key, and [`kSecAttrApplicationLabel`](./ksecattrapplicationlabel.md) to an identifier defined by your application, for subsequent use in calls to [`SecItemCopyMatching(_:_:)`](./secitemcopymatching%28_,_%29.md). Additionally, you can specify keychain access controls for the key by setting [`kSecAttrAccess`](./ksecattraccess.md) to a [`SecAccess`](./secaccess.md) object.
- `error`: A pointer to a [`CFError`](../CoreFoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygeneratesymmetric(_:_:))*