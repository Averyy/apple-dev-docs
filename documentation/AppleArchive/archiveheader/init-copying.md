# init(copying:)

**Framework**: Apple Archive  
**Kind**: init

Creates a copy of an archive header.

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
init(copying s: ArchiveHeader)
```

## Parameters

- `s`: The source header.

## See Also

- [init()](archiveheader/init.md)
  Creates a new empty archive header.
- [init?(keySet: ArchiveHeader.FieldKeySet, directory: FilePath, path: FilePath, flags: ArchiveFlags)](archiveheader/init(keyset:directory:path:flags:).md)
  Creates a new archive header with fields derived from the filesystem object, at the specified directory and path.
- [init?(withAAEncodedData: UnsafeBufferPointer<UInt8>)](archiveheader/init(withaaencodeddata:).md)
  Creates a new archive header from encoded data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/init(copying:))*