# SecKeyAlgorithm

**Framework**: Security  
**Kind**: struct

The algorithms that cryptographic keys enable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct SecKeyAlgorithm
```

## Topics

### Elliptic curve encryption standard X963
- [static let eciesEncryptionStandardX963SHA1AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptionstandardx963sha1aesgcm.md)
- [static let eciesEncryptionStandardX963SHA224AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptionstandardx963sha224aesgcm.md)
- [static let eciesEncryptionStandardX963SHA256AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptionstandardx963sha256aesgcm.md)
- [static let eciesEncryptionStandardX963SHA384AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptionstandardx963sha384aesgcm.md)
- [static let eciesEncryptionStandardX963SHA512AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptionstandardx963sha512aesgcm.md)
### Elliptic curve encryption standard variable IVX963
- [static let eciesEncryptionStandardVariableIVX963SHA224AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptionstandardvariableivx963sha224aesgcm.md)
- [static let eciesEncryptionStandardVariableIVX963SHA256AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptionstandardvariableivx963sha256aesgcm.md)
- [static let eciesEncryptionStandardVariableIVX963SHA384AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptionstandardvariableivx963sha384aesgcm.md)
- [static let eciesEncryptionStandardVariableIVX963SHA512AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptionstandardvariableivx963sha512aesgcm.md)
### Elliptic curve encryption cofactor variable IVX963
- [static let eciesEncryptionCofactorVariableIVX963SHA224AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptioncofactorvariableivx963sha224aesgcm.md)
- [static let eciesEncryptionCofactorVariableIVX963SHA256AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptioncofactorvariableivx963sha256aesgcm.md)
- [static let eciesEncryptionCofactorVariableIVX963SHA384AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptioncofactorvariableivx963sha384aesgcm.md)
- [static let eciesEncryptionCofactorVariableIVX963SHA512AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptioncofactorvariableivx963sha512aesgcm.md)
### Elliptic curve encryption cofactor X963
- [static let eciesEncryptionCofactorX963SHA1AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptioncofactorx963sha1aesgcm.md)
- [static let eciesEncryptionCofactorX963SHA224AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptioncofactorx963sha224aesgcm.md)
- [static let eciesEncryptionCofactorX963SHA256AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptioncofactorx963sha256aesgcm.md)
- [static let eciesEncryptionCofactorX963SHA384AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptioncofactorx963sha384aesgcm.md)
- [static let eciesEncryptionCofactorX963SHA512AESGCM: SecKeyAlgorithm](seckeyalgorithm/eciesencryptioncofactorx963sha512aesgcm.md)
### Elliptic curve signature RFC4754
- [static let ecdsaSignatureRFC4754: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturerfc4754.md)
### Elliptic curve signature digest RFC4754
- [static let ecdsaSignatureDigestRFC4754: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestrfc4754.md)
  An algorithm for generating message digest signatures.
- [static let ecdsaSignatureDigestRFC4754SHA1: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestrfc4754sha1.md)
  An algorithm for generating signatures of SHA1 message digests.
- [static let ecdsaSignatureDigestRFC4754SHA224: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestrfc4754sha224.md)
  An algorithm for generating signatures of SHA224 message digests.
- [static let ecdsaSignatureDigestRFC4754SHA256: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestrfc4754sha256.md)
  An algorithm for generating signatures of SHA256 message digests.
- [static let ecdsaSignatureDigestRFC4754SHA384: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestrfc4754sha384.md)
  An algorithm for generating signatures of SHA384 message digests.
- [static let ecdsaSignatureDigestRFC4754SHA512: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestrfc4754sha512.md)
  An algorithm for generating signatures of SHA512 message digests.
### Elliptic curve signature message RFC4754
- [static let ecdsaSignatureMessageRFC4754SHA1: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagerfc4754sha1.md)
  An algorithm for generating message signatures by calculating and signing the SHA1 message digest.
- [static let ecdsaSignatureMessageRFC4754SHA224: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagerfc4754sha224.md)
  An algorithm for generating message signatures by calculating and signing the SHA224 message digest.
- [static let ecdsaSignatureMessageRFC4754SHA256: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagerfc4754sha256.md)
  An algorithm for generating message signatures by calculating and signing the SHA256 message digest.
- [static let ecdsaSignatureMessageRFC4754SHA384: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagerfc4754sha384.md)
  An algorithm for generating message signatures by calculating and signing the SHA384 message digest.
- [static let ecdsaSignatureMessageRFC4754SHA512: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagerfc4754sha512.md)
  An algorithm for generating message signatures by calculating and signing the SHA512 message digest.
### Elliptic curve signature digest X962
- [static let ecdsaSignatureDigestX962: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestx962.md)
- [static let ecdsaSignatureDigestX962SHA1: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestx962sha1.md)
- [static let ecdsaSignatureDigestX962SHA224: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestx962sha224.md)
- [static let ecdsaSignatureDigestX962SHA256: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestx962sha256.md)
- [static let ecdsaSignatureDigestX962SHA384: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestx962sha384.md)
- [static let ecdsaSignatureDigestX962SHA512: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturedigestx962sha512.md)
### Elliptic curve signature message X962
- [static let ecdsaSignatureMessageX962SHA1: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagex962sha1.md)
- [static let ecdsaSignatureMessageX962SHA224: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagex962sha224.md)
- [static let ecdsaSignatureMessageX962SHA256: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagex962sha256.md)
- [static let ecdsaSignatureMessageX962SHA384: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagex962sha384.md)
- [static let ecdsaSignatureMessageX962SHA512: SecKeyAlgorithm](seckeyalgorithm/ecdsasignaturemessagex962sha512.md)
### Elliptic curve key exchange
- [static let ecdhKeyExchangeCofactor: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangecofactor.md)
- [static let ecdhKeyExchangeStandard: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangestandard.md)
- [static let ecdhKeyExchangeCofactorX963SHA1: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangecofactorx963sha1.md)
- [static let ecdhKeyExchangeStandardX963SHA1: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangestandardx963sha1.md)
- [static let ecdhKeyExchangeCofactorX963SHA224: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangecofactorx963sha224.md)
- [static let ecdhKeyExchangeCofactorX963SHA256: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangecofactorx963sha256.md)
- [static let ecdhKeyExchangeCofactorX963SHA384: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangecofactorx963sha384.md)
- [static let ecdhKeyExchangeCofactorX963SHA512: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangecofactorx963sha512.md)
- [static let ecdhKeyExchangeStandardX963SHA224: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangestandardx963sha224.md)
- [static let ecdhKeyExchangeStandardX963SHA256: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangestandardx963sha256.md)
- [static let ecdhKeyExchangeStandardX963SHA384: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangestandardx963sha384.md)
- [static let ecdhKeyExchangeStandardX963SHA512: SecKeyAlgorithm](seckeyalgorithm/ecdhkeyexchangestandardx963sha512.md)
### RSA encryption
- [static let rsaEncryptionRaw: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionraw.md)
- [static let rsaEncryptionPKCS1: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionpkcs1.md)
### RSA encryption OAEP
- [static let rsaEncryptionOAEPSHA1: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha1.md)
- [static let rsaEncryptionOAEPSHA224: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha224.md)
- [static let rsaEncryptionOAEPSHA256: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha256.md)
- [static let rsaEncryptionOAEPSHA384: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha384.md)
- [static let rsaEncryptionOAEPSHA512: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha512.md)
### RSA encryption OAEP AESGCM
- [static let rsaEncryptionOAEPSHA1AESGCM: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha1aesgcm.md)
- [static let rsaEncryptionOAEPSHA224AESGCM: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha224aesgcm.md)
- [static let rsaEncryptionOAEPSHA256AESGCM: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha256aesgcm.md)
- [static let rsaEncryptionOAEPSHA384AESGCM: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha384aesgcm.md)
- [static let rsaEncryptionOAEPSHA512AESGCM: SecKeyAlgorithm](seckeyalgorithm/rsaencryptionoaepsha512aesgcm.md)
### RSA signature raw
- [static let rsaSignatureRaw: SecKeyAlgorithm](seckeyalgorithm/rsasignatureraw.md)
### RSA signature digest PKCS1v15
- [static let rsaSignatureDigestPKCS1v15Raw: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpkcs1v15raw.md)
- [static let rsaSignatureDigestPKCS1v15SHA1: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpkcs1v15sha1.md)
- [static let rsaSignatureDigestPKCS1v15SHA224: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpkcs1v15sha224.md)
- [static let rsaSignatureDigestPKCS1v15SHA256: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpkcs1v15sha256.md)
- [static let rsaSignatureDigestPKCS1v15SHA384: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpkcs1v15sha384.md)
- [static let rsaSignatureDigestPKCS1v15SHA512: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpkcs1v15sha512.md)
### RSA signature message PKCS1v15
- [static let rsaSignatureMessagePKCS1v15SHA1: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepkcs1v15sha1.md)
- [static let rsaSignatureMessagePKCS1v15SHA224: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepkcs1v15sha224.md)
- [static let rsaSignatureMessagePKCS1v15SHA256: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepkcs1v15sha256.md)
- [static let rsaSignatureMessagePKCS1v15SHA384: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepkcs1v15sha384.md)
- [static let rsaSignatureMessagePKCS1v15SHA512: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepkcs1v15sha512.md)
### RSA signature digest PSS
- [static let rsaSignatureDigestPSSSHA1: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpsssha1.md)
- [static let rsaSignatureDigestPSSSHA224: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpsssha224.md)
- [static let rsaSignatureDigestPSSSHA256: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpsssha256.md)
- [static let rsaSignatureDigestPSSSHA384: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpsssha384.md)
- [static let rsaSignatureDigestPSSSHA512: SecKeyAlgorithm](seckeyalgorithm/rsasignaturedigestpsssha512.md)
### RSA signature message PSS
- [static let rsaSignatureMessagePSSSHA1: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepsssha1.md)
- [static let rsaSignatureMessagePSSSHA224: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepsssha224.md)
- [static let rsaSignatureMessagePSSSHA256: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepsssha256.md)
- [static let rsaSignatureMessagePSSSHA384: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepsssha384.md)
- [static let rsaSignatureMessagePSSSHA512: SecKeyAlgorithm](seckeyalgorithm/rsasignaturemessagepsssha512.md)
### Initializers
- [init(rawValue: CFString)](seckeyalgorithm/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyalgorithm)*