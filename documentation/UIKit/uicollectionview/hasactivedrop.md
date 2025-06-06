# hasActiveDrop

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the collection view is currently tracking a drop session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hasActiveDrop: Bool { get }
```

## See Also

- [var dropDelegate: (any UICollectionViewDropDelegate)?](uicollectionview/dropdelegate.md)
  The delegate object that manages the dropping of items into the collection view.
- [protocol UICollectionViewDropDelegate](uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [var reorderingCadence: UICollectionView.ReorderingCadence](uicollectionview/reorderingcadence-swift.property.md)
  The speed at which items in the collection view are reordered to show potential drop locations.
- [UICollectionView.ReorderingCadence](uicollectionview/reorderingcadence-swift.enum.md)
  Constants indicating the speed at which collection view items are reorganized during a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/hasactivedrop)*