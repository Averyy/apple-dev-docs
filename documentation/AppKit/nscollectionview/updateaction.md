# NSCollectionView.UpdateAction

**Framework**: AppKit  
**Kind**: enum

Constants indicating the type of action being performed on an item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum UpdateAction
```

## Topics

### Constants
- [NSCollectionView.UpdateAction.insert](nscollectionview/updateaction/insert.md)
  Insert the item into the collection view.
- [NSCollectionView.UpdateAction.delete](nscollectionview/updateaction/delete.md)
  Remove the action from the collection view.
- [NSCollectionView.UpdateAction.reload](nscollectionview/updateaction/reload.md)
  Reload the item, which consists of deleting and then inserting the item.
- [NSCollectionView.UpdateAction.move](nscollectionview/updateaction/move.md)
  Move the item from its current location to a new location.
- [NSCollectionView.UpdateAction.none](nscollectionview/updateaction/none.md)
  Take no action on the item.
### Initializers
- [init?(rawValue: Int)](nscollectionview/updateaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSCollectionView.ScrollDirection](nscollectionview/scrolldirection.md)
  Constants indicating the scrolling direction for the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/updateaction)*