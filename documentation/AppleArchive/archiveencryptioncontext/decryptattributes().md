# decryptAttributes()

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method

Validates decryption keys, collects archive attributes, and updates the context with decrypted archive attributes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func decryptAttributes() -> Bool
```

#### Return Value

`true` on success; otherwise, `false` if the credentials and archive prologue don’t match.

#### Discussion

You must have created the current context from an encrypted stream.

Apple Archive performs the same validation and updates when it opens a decryption input stream. Therefore, you don’t need to call this function before calling either [`decryptionStream(readingFrom:encryptionContext:flags:threadCount:)`](../archivebytestream/decryptionstream%28readingfrom,encryptioncontext,flags,threadcount%29.md) or [`randomAccessDecryptionStream(readingFrom:encryptionContext:allocationLimit:flags:threadCount:)`](../archivebytestream/randomaccessdecryptionstream%28readingfrom,encryptioncontext,allocationlimit,flags,threadcount%29.md).

## See Also

### Getting and setting encryption context properties
- [var archiveIdentifier: Data?](./archiveidentifier.md)
  An optional set of data that represents the archive identifier.
- [var authData: Data?](./authdata.md)
  An optional, unencrypted set of data that’s stored in the archive prologue.
- [var checksumMode: ArchiveEncryptionContext.ChecksumMode](./checksummode-swift.property.md)
  The checksum mode, such as the 256-bit SHA-256 checksum.
- [ArchiveEncryptionContext.ChecksumMode](./checksummode-swift.struct.md)
  Constants that describe the checksum modes of an encryption context.
- [var containerSize: Int](./containersize.md)
  The size of the compressed and encrypted archive.
- [var encryptionMode: ArchiveEncryptionContext.EncryptionMode](./encryptionmode-swift.property.md)
  The encryption mode, such as symmetric key encryption.
- [ArchiveEncryptionContext.EncryptionMode](./encryptionmode-swift.struct.md)
  Constants that describe the checksum modes of an encryption context.
- [var compressionAlgorithm: ArchiveCompression](./compressionalgorithm.md)
  The compression algorithm, such as LZFSE.
- [struct ArchiveCompression](../archivecompression.md)
  Constants that describe compression algorithms.
- [var compressionBlockSize: Int](./compressionblocksize.md)
  The compression block size that defines the size of the blocks, in bytes, that the context splits data into.
- [var paddingSize: Int](./paddingsize.md)
  An integer value that, if not zero, specifies that the size of the final archive is a multiple of the padding size.
- [var profile: ArchiveEncryptionContext.Profile](./profile-swift.property.md)
  The profile of the archve.
- [ArchiveEncryptionContext.Profile](./profile-swift.struct.md)
  Constants that describe the profile of an encryption context.
- [var rawSize: Int](./rawsize.md)
  The size of the archive raw data.
- [var signatureEncryptionKey: SymmetricKey?](./signatureencryptionkey.md)
  The signature encryption key that the context requires to sign an encrypted archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/decryptattributes())*