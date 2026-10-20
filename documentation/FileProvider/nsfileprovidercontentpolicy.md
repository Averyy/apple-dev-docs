# NSFileProviderContentPolicy

**Framework**: File Provider  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum NSFileProviderContentPolicy
```

```c
enum NSFileProviderContentPolicy : NSInteger;
```

## Topics

### Policies
- [NSFileProviderContentPolicy.downloadEagerlyAndKeepDownloaded](./nsfileprovidercontentpolicy/downloadeagerlyandkeepdownloaded.md)
- [NSFileProviderContentPolicy.downloadLazily](./nsfileprovidercontentpolicy/downloadlazily.md)
- [NSFileProviderContentPolicy.downloadLazilyAndEvictOnRemoteUpdate](./nsfileprovidercontentpolicy/downloadlazilyandevictonremoteupdate.md)
- [NSFileProviderContentPolicy.inherited](./nsfileprovidercontentpolicy/inherited.md)
### Initializers
- [init?(rawValue: Int)](./nsfileprovidercontentpolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing Content
- [var childItemCount: NSNumber?](./nsfileprovideritemprotocol/childitemcount.md)
  The number of items contained by this item.
- [var documentSize: NSNumber?](./nsfileprovideritemprotocol/documentsize.md)
  The document’s size, in bytes.
- [var contentPolicy: NSFileProviderContentPolicy](./nsfileprovideritemprotocol/contentpolicy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidercontentpolicy)*