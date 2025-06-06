# NSFileProviderContentPolicy

**Framework**: File Provider  
**Kind**: enum

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum NSFileProviderContentPolicy
```

## Topics

### Policies
- [NSFileProviderContentPolicy.downloadEagerlyAndKeepDownloaded](nsfileprovidercontentpolicy/downloadeagerlyandkeepdownloaded.md)
- [NSFileProviderContentPolicy.downloadLazily](nsfileprovidercontentpolicy/downloadlazily.md)
- [NSFileProviderContentPolicy.downloadLazilyAndEvictOnRemoteUpdate](nsfileprovidercontentpolicy/downloadlazilyandevictonremoteupdate.md)
- [NSFileProviderContentPolicy.inherited](nsfileprovidercontentpolicy/inherited.md)
### Initializers
- [init?(rawValue: Int)](nsfileprovidercontentpolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var childItemCount: NSNumber?](nsfileprovideritemprotocol/childitemcount.md)
  The number of items contained by this item.
- [var documentSize: NSNumber?](nsfileprovideritemprotocol/documentsize.md)
  The document’s size, in bytes.
- [var contentPolicy: NSFileProviderContentPolicy](nsfileprovideritemprotocol/contentpolicy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidercontentpolicy)*