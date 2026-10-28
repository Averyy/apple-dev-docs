# reorderingCadence

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The speed at which items in the collection view are reordered to show potential drop locations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var reorderingCadence: UICollectionView.ReorderingCadence { get set }
```

```objc
@property (nonatomic) UICollectionViewReorderingCadence reorderingCadence;
```

## Discussion

The default value in this property is [`UICollectionView.ReorderingCadence.immediate`](./reorderingcadence-swift.enum/immediate.md). You might specify a slower cadence when you want to prevent the reordering of items from being a distraction to the user. For example, you might slow it down if immediate reordering makes it more difficult to drop items at the correct location.

## See Also

### Managing drop interactions
- [var dropDelegate: (any UICollectionViewDropDelegate)?](./dropdelegate.md)
  The delegate object that manages the dropping of items into the collection view.
- [protocol UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [var hasActiveDrop: Bool](./hasactivedrop.md)
  A Boolean value that indicates whether the collection view is currently tracking a drop session.
- [UICollectionView.ReorderingCadence](./reorderingcadence-swift.enum.md)
  Constants indicating the speed at which collection view items are reorganized during a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/reorderingcadence-swift.property)*