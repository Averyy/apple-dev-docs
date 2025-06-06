# init(withAAEncodedData:)

**Framework**: Apple Archive  
**Kind**: init

Creates a new archive header from encoded data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
required init?(withAAEncodedData data: UnsafeBufferPointer<UInt8>)
```

## Parameters

- `data`: The encoded data.

## See Also

- [init()](archiveheader/entryxatblob/init.md)
  Creates a new empty extended attribute blob.
- [init?(directory: FilePath, path: FilePath, flags: ArchiveFlags)](archiveheader/entryxatblob/init(directory:path:flags:).md)
  Creates a new extended attribute blob from the specified directory and path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryxatblob/init(withaaencodeddata:))*