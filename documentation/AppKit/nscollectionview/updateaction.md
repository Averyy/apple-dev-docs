# NSCollectionView.UpdateAction

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the type of action being performed on an item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum UpdateAction
```

```c
enum NSCollectionUpdateAction : NSInteger;
```

## Topics

### Constants
- [NSCollectionView.UpdateAction.insert](./updateaction/insert.md)
  Insert the item into the collection view.
- [NSCollectionView.UpdateAction.delete](./updateaction/delete.md)
  Remove the action from the collection view.
- [NSCollectionView.UpdateAction.reload](./updateaction/reload.md)
  Reload the item, which consists of deleting and then inserting the item.
- [NSCollectionView.UpdateAction.move](./updateaction/move.md)
  Move the item from its current location to a new location.
- [NSCollectionView.UpdateAction.none](./updateaction/none.md)
  Take no action on the item.
### Initializers
- [init?(rawValue: Int)](./updateaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [NSCollectionView.ScrollDirection](./scrolldirection.md)
  Constants indicating the scrolling direction for the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/updateaction)*