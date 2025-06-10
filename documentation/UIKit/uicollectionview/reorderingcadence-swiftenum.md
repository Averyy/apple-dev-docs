# UICollectionView.ReorderingCadence

**Framework**: UIKit  
**Kind**: enum

Constants indicating the speed at which collection view items are reorganized during a drop.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum ReorderingCadence
```

## Topics

### Constants
- [UICollectionView.ReorderingCadence.immediate](uicollectionview/reorderingcadence-swift.enum/immediate.md)
  Items are reordered into place immediately.
- [UICollectionView.ReorderingCadence.fast](uicollectionview/reorderingcadence-swift.enum/fast.md)
  Items are reordered quickly, but with a short delay.
- [UICollectionView.ReorderingCadence.slow](uicollectionview/reorderingcadence-swift.enum/slow.md)
  Items are reordered after a delay.
### Initializers
- [init?(rawValue: Int)](uicollectionview/reorderingcadence-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var dropDelegate: (any UICollectionViewDropDelegate)?](uicollectionview/dropdelegate.md)
  The delegate object that manages the dropping of items into the collection view.
- [protocol UICollectionViewDropDelegate](uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [var hasActiveDrop: Bool](uicollectionview/hasactivedrop.md)
  A Boolean value that indicates whether the collection view is currently tracking a drop session.
- [var reorderingCadence: UICollectionView.ReorderingCadence](uicollectionview/reorderingcadence-swift.property.md)
  The speed at which items in the collection view are reordered to show potential drop locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/reorderingcadence-swift.enum)*