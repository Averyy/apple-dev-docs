# init(directory:path:flags:)

**Framework**: Apple Archive  
**Kind**: init

Creates a new extended attribute blob from the specified directory and path.

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
init?(directory: FilePath, path: FilePath, flags: ArchiveFlags)
```

## Parameters

- `directory`: The base directory of the filesystem object.
- `path`: The path, relative to  , to target filesystem object.
- `flags`: Flags that control the behavior of the operation.

## See Also

- [init()](archiveheader/entryxatblob/init.md)
  Creates a new empty extended attribute blob.
- [init?(withAAEncodedData: UnsafeBufferPointer<UInt8>)](archiveheader/entryxatblob/init(withaaencodeddata:).md)
  Creates a new archive header from encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryxatblob/init(directory:path:flags:))*