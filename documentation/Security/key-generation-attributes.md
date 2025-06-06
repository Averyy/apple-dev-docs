# Key Generation Attributes

**Framework**: Security

Use attribute dictionary keys during cryptographic key generation.

#### Overview

Use these dictionary keys in the `parameter` dictionary when you create new cryptographic keys with the [`SecKeyCreateRandomKey(_:_:)`](seckeycreaterandomkey(_:_:).md) function. The type and size attributes are required, while all others are optional.

With the exception of [`kSecAttrTokenID`](ksecattrtokenid.md), you can specify the optional keys in either the top-level `parameter` dictionary or in one of the key-specific sub-dictionaries specified by the [`kSecPrivateKeyAttrs`](ksecprivatekeyattrs.md) and [`kSecPublicKeyAttrs`](ksecpublickeyattrs.md) attributes. In the latter case, the given attribute applies only to the private or public key, respectively.

Use these keys in exactly the same way for the `parameter` dictionary you supply to the legacy [`SecKeyGeneratePair(_:_:_:)`](seckeygeneratepair(_:_:_:).md) function.

## Topics

### Required
- [let kSecAttrKeyType: CFString](ksecattrkeytype.md)
  A key whose value indicates the item’s algorithm.
- [let kSecAttrKeySizeInBits: CFString](ksecattrkeysizeinbits.md)
  A key whose value indicates the number of bits in a cryptographic key.
### Key Specific
- [let kSecPrivateKeyAttrs: CFString](ksecprivatekeyattrs.md)
  A key whose value is a dictionary of cryptographic key attributes specific to a private key.
- [let kSecPublicKeyAttrs: CFString](ksecpublickeyattrs.md)
  A key whose value is a dictionary of cryptographic key attributes specific to a public key.
### Optional
- [let kSecAttrLabel: CFString](ksecattrlabel.md)
  A key with a value that’s a string indicating the item’s label.
- [let kSecAttrTokenID: CFString](ksecattrtokenid.md)
  A key whose value indicates that a cryptographic key is in an external store.
- [let kSecAttrIsPermanent: CFString](ksecattrispermanent.md)
  A key whose value indicates the item’s permanence.
- [let kSecAttrApplicationTag: CFString](ksecattrapplicationtag.md)
  A key whose value indicates the item’s private tag.
- [let kSecAttrEffectiveKeySize: CFString](ksecattreffectivekeysize.md)
  A key whose value indicates the effective number of bits in a cryptographic key.
- [let kSecAttrCanEncrypt: CFString](ksecattrcanencrypt.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for encryption.
- [let kSecAttrCanDecrypt: CFString](ksecattrcandecrypt.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for decryption.
- [let kSecAttrCanDerive: CFString](ksecattrcanderive.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for derivation.
- [let kSecAttrCanSign: CFString](ksecattrcansign.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for digital signing.
- [let kSecAttrCanVerify: CFString](ksecattrcanverify.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for signature verification.
- [let kSecAttrCanWrap: CFString](ksecattrcanwrap.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for wrapping.
- [let kSecAttrCanUnwrap: CFString](ksecattrcanunwrap.md)
  A key whose value is a Boolean that indicates whether the cryptographic key can be used for unwrapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/key-generation-attributes)*