# SecKeyGeneratePairAsync(_:_:_:)

**Framework**: Security  
**Kind**: func

Generates a public/private key pair.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecKeyGeneratePairAsync(_ parameters: CFDictionary, _ deliveryQueue: dispatch_queue_t, _ result: @escaping SecKeyGeneratePairBlock)
```

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
- [`kSecAttrCanUnwrap`](ksecattrcanunwrap.md) defaults to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) for private keys, [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) for public keys. These default values can be overridden by adding a value for the associated key in the parameter dictionary.
- `deliveryQueue`: The dispatch queue on which the result block should be scheduled.
- `result`: A block of type [`SecKeyGeneratePairBlock`](seckeygeneratepairblock.md) that gets called with the result upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygeneratepairasync(_:_:_:))*