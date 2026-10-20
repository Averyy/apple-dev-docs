# init(profile:compressionAlgorithm:compressionBlockSize:)

**Framework**: Apple Archive  
**Kind**: init  
**Role**: Initializer

Returns a new encryption context from the specified profile, compression algorithm, and block size.

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
init(profile: ArchiveEncryptionContext.Profile, compressionAlgorithm: ArchiveCompression, compressionBlockSize: Int = 1<<20)
```

## Parameters

- `profile`: The profile to use to create the encryption context.
- `compressionAlgorithm`: The compression algorithm.
- `compressionBlockSize`: The size of the independently compressed blocks.

## See Also

### Creating an archive encryption context
- [init?(from: ArchiveByteStream)](./init%28from%29.md)
  Returns a new encryption context from the specified encrypted stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/init(profile:compressionalgorithm:compressionblocksize:))*