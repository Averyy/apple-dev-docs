# NSCollectionView.DropOperation

**Framework**: AppKit  
**Kind**: enum

These constants specify if acceptance of a drop should be at the item it is dropped on or before the item. These constants are used by the  [`collectionView(_:acceptDrop:index:dropOperation:)`](nscollectionviewdelegate/collectionview(_:acceptdrop:index:dropoperation:).md) and [`collectionView(_:validateDrop:proposedIndex:dropOperation:)`](nscollectionviewdelegate/collectionview(_:validatedrop:proposedindex:dropoperation:).md) methods in [`NSCollectionViewDelegate`](nscollectionviewdelegate.md)

**Availability**:
- macOS 10.6+

## Declaration

```swift
enum DropOperation
```

## Topics

### Constants
- [NSCollectionView.DropOperation.on](nscollectionview/dropoperation/on.md)
  The drop occurs at the collection view item to which the item was dragged.
- [NSCollectionView.DropOperation.before](nscollectionview/dropoperation/before.md)
  The drop occurs before the collection view item to which the item was dragged.
### Initializers
- [init?(rawValue: Int)](nscollectionview/dropoperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSCollectionView.ScrollPosition](nscollectionview/scrollposition.md)
  Constants indicating the options for scrolling the collection view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/dropoperation)*