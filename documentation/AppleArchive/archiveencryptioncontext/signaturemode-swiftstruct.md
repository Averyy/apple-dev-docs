# ArchiveEncryptionContext.SignatureMode

**Framework**: Apple Archive  
**Kind**: struct

Constants that describe the signature modes of an encryption context.

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
struct SignatureMode
```

## Topics

### Signature Mode Constants
- [static let none: ArchiveEncryptionContext.SignatureMode](archiveencryptioncontext/signaturemode-swift.struct/none.md)
  A constant that represents no signature.
- [static let ecdsa_p256: ArchiveEncryptionContext.SignatureMode](archiveencryptioncontext/signaturemode-swift.struct/ecdsa_p256.md)
  A constant that represents an ECDSA Nist P-256 signature.
### Raw Values
- [var rawValue: UInt32](archiveencryptioncontext/signaturemode-swift.struct/rawvalue.md)
  The corresponding value of the raw type.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [static func sign(encryptedStream: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext) throws](archiveencryptioncontext/sign(encryptedstream:encryptioncontext:).md)
  Signs an encrypted archive using the credentials stored in the specified encryption context.
- [var signatureMode: ArchiveEncryptionContext.SignatureMode](archiveencryptioncontext/signaturemode-swift.property.md)
  The signature mode, such as an ECDSA Nist P-256 signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/signaturemode-swift.struct)*