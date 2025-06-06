# signatureMode

**Framework**: Apple Archive  
**Kind**: property

The signature mode, such as an ECDSA Nist P-256 signature.

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
var signatureMode: ArchiveEncryptionContext.SignatureMode { get }
```

## See Also

- [static func sign(encryptedStream: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext) throws](archiveencryptioncontext/sign(encryptedstream:encryptioncontext:).md)
  Signs an encrypted archive using the credentials stored in the specified encryption context.
- [ArchiveEncryptionContext.SignatureMode](archiveencryptioncontext/signaturemode-swift.struct.md)
  Constants that describe the signature modes of an encryption context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/signaturemode-swift.property)*