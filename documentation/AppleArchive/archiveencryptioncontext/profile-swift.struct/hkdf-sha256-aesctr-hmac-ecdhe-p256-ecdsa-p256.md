# hkdf_sha256_aesctr_hmac__ecdhe_p256__ecdsa_p256

**Framework**: Apple Archive  
**Kind**: property

A constant that represents signed ECDHE public key encryption, where only the recipient with the corresponding private key can unlock the container.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
static let hkdf_sha256_aesctr_hmac__ecdhe_p256__ecdsa_p256: ArchiveEncryptionContext.Profile
```

#### Discussion

The signature is encrypted.

## See Also

- [static let hkdf_sha256_hmac__none__ecdsa_p256: ArchiveEncryptionContext.Profile](archiveencryptioncontext/profile-swift.struct/hkdf_sha256_hmac__none__ecdsa_p256.md)
  A constant that represents no encryption, authenticated container, signature is mandatory.
- [static let hkdf_sha256_aesctr_hmac__symmetric__none: ArchiveEncryptionContext.Profile](archiveencryptioncontext/profile-swift.struct/hkdf_sha256_aesctr_hmac__symmetric__none.md)
  A constant that represents unsigned, symmetric key encryption.
- [static let hkdf_sha256_aesctr_hmac__symmetric__ecdsa_p256: ArchiveEncryptionContext.Profile](archiveencryptioncontext/profile-swift.struct/hkdf_sha256_aesctr_hmac__symmetric__ecdsa_p256.md)
  A constant that represents signed symmetric key encryption, signed with encrypted signature.
- [static let hkdf_sha256_aesctr_hmac__ecdhe_p256__none: ArchiveEncryptionContext.Profile](archiveencryptioncontext/profile-swift.struct/hkdf_sha256_aesctr_hmac__ecdhe_p256__none.md)
  A constant that represents unsigned ECDHE public key encryption, where only the recipient with the corresponding private key can unlock the container.
- [static let hkdf_sha256_aesctr_hmac__scrypt__none: ArchiveEncryptionContext.Profile](archiveencryptioncontext/profile-swift.struct/hkdf_sha256_aesctr_hmac__scrypt__none.md)
  A constant that represents unsigned password encryption using scrypt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/profile-swift.struct/hkdf_sha256_aesctr_hmac__ecdhe_p256__ecdsa_p256)*