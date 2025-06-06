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

- [init()](archiveheader/init.md)
  Creates a new empty archive header.
- [init?(keySet: ArchiveHeader.FieldKeySet, directory: FilePath, path: FilePath, flags: ArchiveFlags)](archiveheader/init(keyset:directory:path:flags:).md)
  Creates a new archive header with fields derived from the filesystem object, at the specified directory and path.
- [init(copying: ArchiveHeader)](archiveheader/init(copying:).md)
  Creates a copy of an archive header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/init(withaaencodeddata:))*