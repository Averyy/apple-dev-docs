# ArchiveEncryptionContext.EncryptionMode

**Framework**: Apple Archive  
**Kind**: struct  
**Role**: Structure

Constants that describe the checksum modes of an encryption context.

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
struct EncryptionMode
```

## Topics

### Encryption Mode Constants
- [static let none: ArchiveEncryptionContext.EncryptionMode](./encryptionmode-swift.struct/none.md)
  A constant that represents no encryption.
- [static let ecdhe_p256: ArchiveEncryptionContext.EncryptionMode](./encryptionmode-swift.struct/ecdhe_p256.md)
  A constant that represents ephemeral Diffie-Hellman encryption mode.
- [static let scrypt: ArchiveEncryptionContext.EncryptionMode](./encryptionmode-swift.struct/scrypt.md)
  A constant that represents ephemeral password encryption mode.
- [static let symmetric: ArchiveEncryptionContext.EncryptionMode](./encryptionmode-swift.struct/symmetric.md)
  A constant that represents symmetric key encryption mode.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Getting and setting encryption context properties
- [func decryptAttributes() -> Bool](./decryptattributes%28%29.md)
  Validates decryption keys, collects archive attributes, and updates the context with decrypted archive attributes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/encryptionmode-swift.struct)*