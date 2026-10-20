# withAAEncodedData(_:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method

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
func withAAEncodedData<R>(_ body: (UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R
```

## See Also

### Collection Requirements
- [func append(ArchiveHeader.EntryXATBlob.ExtendedAttribute)](./append%28_%29.md)
- [func remove(at: Int) -> ArchiveHeader.EntryXATBlob.ExtendedAttribute](./remove%28at%29.md)
- [func removeAll()](./removeall%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryxatblob/withaaencodeddata(_:))*