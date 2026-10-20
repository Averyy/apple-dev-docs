# archiveIdentifier

**Framework**: Apple Archive  
**Kind**: property  
**Role**: Instance Property

An optional set of data that represents the archive identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
var archiveIdentifier: Data? { get }
```

## See Also

### Getting and setting encryption context properties
- [func decryptAttributes() -> Bool](./decryptattributes%28%29.md)
  Validates decryption keys, collects archive attributes, and updates the context with decrypted archive attributes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/archiveidentifier)*