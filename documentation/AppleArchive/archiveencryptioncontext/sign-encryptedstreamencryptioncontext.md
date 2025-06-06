# sign(encryptedStream:encryptionContext:)

**Framework**: Apple Archive  
**Kind**: method

Signs an encrypted archive using the credentials stored in the specified encryption context.

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
static func sign(encryptedStream: ArchiveByteStream, encryptionContext context: ArchiveEncryptionContext) throws
```

#### Discussion

Close the encrypted stream before calling this function, and create the archive with a `signatureMode` other than [`none`](archiveencryptioncontext/signaturemode-swift.struct/none.md). Create the context that you pass to this function from the same archive and it must contain the signature encryption key and the signing private key.

## Parameters

- `encryptedStream`: A read-write byte stream that points to an encrypted archive.
- `context`: The encryption context that provides the credentials.

## See Also

- [var signatureMode: ArchiveEncryptionContext.SignatureMode](archiveencryptioncontext/signaturemode-swift.property.md)
  The signature mode, such as an ECDSA Nist P-256 signature.
- [ArchiveEncryptionContext.SignatureMode](archiveencryptioncontext/signaturemode-swift.struct.md)
  Constants that describe the signature modes of an encryption context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/sign(encryptedstream:encryptioncontext:))*