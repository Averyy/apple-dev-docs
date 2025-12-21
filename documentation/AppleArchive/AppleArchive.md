# Apple Archive

**Framework**: Apple Archive  
**Kind**: module

Perform multithreaded lossless compression of directories, files, and data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

#### Overview

Apple Archive provides fast compression that includes file attributes, such as, ownership, permissions, flags, times, extended attributes, and error correction. Apple Archive offers these features:

- Multithreaded processing that uses all cores, is energy efficient, and yields faster results
- An ability to transport files and their attributes and use Apple File System (APFS) features when they’re available, for example, filesystem compression, full clones, and sparse files
- Flexible encoding formats, so you can use archives, for example, for error correction, digests, manifests, and external data storage
- API support for in-memory archive processing, streaming access, random access, and back-to-back archive and extraction

## Topics

### Apple Archive essentials
- [Compressing single files](../Accelerate/compressing-single-files.md)
  Compress a single file and store the result on the file system.
- [Decompressing single files](../Accelerate/decompressing-single-files.md)
  Recreate a single file from a compressed file.
- [Compressing file system directories](../Accelerate/compressing-file-system-directories.md)
  Compress the contents of an entire directory and store the result on the file system.
- [Decompressing and extracting an archived directory](../Accelerate/decompressing-and-extracting-an-archived-directory.md)
  Recreate an entire file system directory from an archive file.
- [Compressing and saving a string to the file system](../Accelerate/compressing-and-saving-a-string-to-the-file-system.md)
  Compress the contents of a Unicode string and store the result on the file system.
- [Decompressing and parsing an archived string](../Accelerate/decompressing-and-parsing-an-archived-string.md)
  Recreate a string from an archive file.
### Apple Encrypted Archive essentials
- [Encrypting and Decrypting a String](encrypting-and-decrypting-a-string.md)
  Encrypt the contents of a string and save the result to the file system, then decrypt and recreate the string from the archive file using Apple Encrypted Archive.
- [Encrypting and Decrypting a Single File](encrypting-and-decrypting-a-single-file.md)
  Encrypt a single file and save the result to the file system, then decrypt and recreate the original file from the archive file using Apple Encrypted Archive.
- [Encrypting and Decrypting Directories](encrypting-and-decrypting-directories.md)
  Compress and encrypt the contents of an entire directory or decompress and decrypt an archived directory  using Apple Encrypted Archive.
- [class ArchiveEncryptionContext](archiveencryptioncontext.md)
  An object that encapsulates all parameters, keys, and data necessary to open an encrypted archive for both encryption and decryption streams.
### Apple Archive headers
- [class ArchiveHeader](archiveheader.md)
  An AppleArchive entry header.
### Apple Archive streams
- [protocol ArchiveStreamProtocol](archivestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to data blobs.
- [class ArchiveStream](archivestream.md)
  An archive stream that reads from and writes to data blobs
- [protocol ArchiveByteStreamProtocol](archivebytestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to buffers.
- [class ArchiveByteStream](archivebytestream.md)
  An archive stream that reads from and writes to buffers.
### Apple Archive errors
- [enum ArchiveError](archiveerror.md)
  Error codes for AppleArchive.
### Constants
- [var APPLE_ARCHIVE_API_VERSION: Int32](apple_archive_api_version.md)
  The version of the framework at compile time.
### Reference
- [Apple Archive structures](apple-archive-structures.md)

## See Also

- [About Apple File System](../Foundation/about-apple-file-system.md)
  Use high-level APIs to get the most out of Apple File System.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppleArchive)*