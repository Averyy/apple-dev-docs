# withAAEncodedData(_:)

**Framework**: Apple Archive  
**Kind**: method

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
func withAAEncodedData<R>(_ body: (UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R
```

## See Also

- [func append(ArchiveHeader.EntryXATBlob.ExtendedAttribute)](archiveheader/entryxatblob/append(_:).md)
- [func remove(at: Int) -> ArchiveHeader.EntryXATBlob.ExtendedAttribute](archiveheader/entryxatblob/remove(at:).md)
- [func removeAll()](archiveheader/entryxatblob/removeall.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryxatblob/withaaencodeddata(_:))*