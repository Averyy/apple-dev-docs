# init(keySet:directory:path:flags:)

**Framework**: Apple Archive  
**Kind**: init  
**Role**: Initializer

Creates a new archive header with fields derived from the filesystem object, at the specified directory and path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
init?(keySet: ArchiveHeader.FieldKeySet, directory: FilePath, path: FilePath, flags: ArchiveFlags)
```

## Parameters

- `keySet`: The fields that the new header includes.
- `directory`: The base directory of the filesystem object.
- `path`: The path, relative to `directory`, to the target filesystem object.
- `flags`: Flags that control the behavior of the operation.

## See Also

### Creating an Archive Header
- [init()](./init%28%29.md)
  Creates a new empty archive header.
- [init?(withAAEncodedData: UnsafeBufferPointer<UInt8>)](./init%28withaaencodeddata%29.md)
  Creates a new archive header from encoded data.
- [init(copying: ArchiveHeader)](./init%28copying%29.md)
  Creates a copy of an archive header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/init(keyset:directory:path:flags:))*