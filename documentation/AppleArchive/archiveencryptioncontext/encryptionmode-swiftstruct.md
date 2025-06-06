# ArchiveEncryptionContext.EncryptionMode

**Framework**: Apple Archive  
**Kind**: struct

Constants that describe the checksum modes of an encryption context.

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
struct EncryptionMode
```

## Topics

### Encryption Mode Constants
- [static let none: ArchiveEncryptionContext.EncryptionMode](archiveencryptioncontext/encryptionmode-swift.struct/none.md)
  A constant that represents no encryption.
- [static let ecdhe_p256: ArchiveEncryptionContext.EncryptionMode](archiveencryptioncontext/encryptionmode-swift.struct/ecdhe_p256.md)
  A constant that represents ephemeral Diffie-Hellman encryption mode.
- [static let scrypt: ArchiveEncryptionContext.EncryptionMode](archiveencryptioncontext/encryptionmode-swift.struct/scrypt.md)
  A constant that represents ephemeral password encryption mode.
- [static let symmetric: ArchiveEncryptionContext.EncryptionMode](archiveencryptioncontext/encryptionmode-swift.struct/symmetric.md)
  A constant that represents symmetric key encryption mode.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [func decryptAttributes() -> Bool](archiveencryptioncontext/decryptattributes.md)
  Validates decryption keys, collects archive attributes, and updates the context with decrypted archive attributes.
- [var archiveIdentifier: Data?](archiveencryptioncontext/archiveidentifier.md)
  An optional set of data that represents the archive identifier.
- [var authData: Data?](archiveencryptioncontext/authdata.md)
  An optional, unencrypted set of data that’s stored in the archive prologue.
- [var checksumMode: ArchiveEncryptionContext.ChecksumMode](archiveencryptioncontext/checksummode-swift.property.md)
  The checksum mode, such as the 256-bit SHA-256 checksum.
- [ArchiveEncryptionContext.ChecksumMode](archiveencryptioncontext/checksummode-swift.struct.md)
  Constants that describe the checksum modes of an encryption context.
- [var containerSize: Int](archiveencryptioncontext/containersize.md)
  The size of the compressed and encrypted archive.
- [var encryptionMode: ArchiveEncryptionContext.EncryptionMode](archiveencryptioncontext/encryptionmode-swift.property.md)
  The encryption mode, such as symmetric key encryption.
- [var compressionAlgorithm: ArchiveCompression](archiveencryptioncontext/compressionalgorithm.md)
  The compression algorithm, such as LZFSE.
- [struct ArchiveCompression](archivecompression.md)
  Constants that describe compression algorithms.
- [var compressionBlockSize: Int](archiveencryptioncontext/compressionblocksize.md)
  The compression block size that defines the size of the blocks, in bytes, that the context splits data into.
- [var paddingSize: Int](archiveencryptioncontext/paddingsize.md)
  An integer value that, if not zero, specifies that the size of the final archive is a multiple of the padding size.
- [var profile: ArchiveEncryptionContext.Profile](archiveencryptioncontext/profile-swift.property.md)
  The profile of the archve.
- [ArchiveEncryptionContext.Profile](archiveencryptioncontext/profile-swift.struct.md)
  Constants that describe the profile of an encryption context.
- [var rawSize: Int](archiveencryptioncontext/rawsize.md)
  The size of the archive raw data.
- [var signatureEncryptionKey: SymmetricKey?](archiveencryptioncontext/signatureencryptionkey.md)
  The signature encryption key that the context requires to sign an encrypted archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/encryptionmode-swift.struct)*