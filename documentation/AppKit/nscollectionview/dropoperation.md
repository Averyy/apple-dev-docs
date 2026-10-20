# NSCollectionView.DropOperation

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants specify if acceptance of a drop should be at the item it is dropped on or before the item. These constants are used by the  [`collectionView(_:acceptDrop:index:dropOperation:)`](../nscollectionviewdelegate/collectionview%28_,acceptdrop,index,dropoperation%29.md) and [`collectionView(_:validateDrop:proposedIndex:dropOperation:)`](../nscollectionviewdelegate/collectionview%28_,validatedrop,proposedindex,dropoperation%29.md) methods in [`NSCollectionViewDelegate`](../nscollectionviewdelegate.md)

**Availability**:
- macOS 10.6+

## Declaration

```swift
enum DropOperation
```

```c
enum NSCollectionViewDropOperation : NSInteger;
```

## Topics

### Constants
- [NSCollectionView.DropOperation.on](./dropoperation/on.md)
  The drop occurs at the collection view item to which the item was dragged.
- [NSCollectionView.DropOperation.before](./dropoperation/before.md)
  The drop occurs before the collection view item to which the item was dragged.
### Initializers
- [init?(rawValue: Int)](./dropoperation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSCollectionView.ScrollPosition](./scrollposition.md)
  Constants indicating the options for scrolling the collection view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/dropoperation)*