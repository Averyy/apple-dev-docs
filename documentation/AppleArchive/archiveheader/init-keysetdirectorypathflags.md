# init(keySet:directory:path:flags:)

**Framework**: Apple Archive  
**Kind**: init

Creates a new archive header with fields derived from the filesystem object, at the specified directory and path.

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
init?(keySet: ArchiveHeader.FieldKeySet, directory: FilePath, path: FilePath, flags: ArchiveFlags)
```

## Parameters

- `keySet`: The fields that the new header includes.
- `directory`: The base directory of the filesystem object.
- `path`: The path, relative to  , to the target filesystem object.
- `flags`: Flags that control the behavior of the operation.

## See Also

- [init()](archiveheader/init.md)
  Creates a new empty archive header.
- [init?(withAAEncodedData: UnsafeBufferPointer<UInt8>)](archiveheader/init(withaaencodeddata:).md)
  Creates a new archive header from encoded data.
- [init(copying: ArchiveHeader)](archiveheader/init(copying:).md)
  Creates a copy of an archive header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/init(keyset:directory:path:flags:))*