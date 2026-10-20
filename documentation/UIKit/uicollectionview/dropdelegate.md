# dropDelegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate object that manages the dropping of items into the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var dropDelegate: (any UICollectionViewDropDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UICollectionViewDropDelegate> dropDelegate;
```

## Mentions

- [Supporting Drag and Drop in Collection Views](../supporting-drag-and-drop-in-collection-views.md)

## See Also

### Managing drop interactions
- [protocol UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [var hasActiveDrop: Bool](./hasactivedrop.md)
  A Boolean value that indicates whether the collection view is currently tracking a drop session.
- [var reorderingCadence: UICollectionView.ReorderingCadence](./reorderingcadence-swift.property.md)
  The speed at which items in the collection view are reordered to show potential drop locations.
- [UICollectionView.ReorderingCadence](./reorderingcadence-swift.enum.md)
  Constants indicating the speed at which collection view items are reorganized during a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/dropdelegate)*