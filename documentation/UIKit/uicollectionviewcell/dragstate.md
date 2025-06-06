# UICollectionViewCell.DragState

**Framework**: UIKit  
**Kind**: enum

Constants indicating the current state of the drag operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum DragState
```

## Topics

### Constants
- [UICollectionViewCell.DragState.none](uicollectionviewcell/dragstate/none.md)
  The cell isn’t involved in a drag.
- [UICollectionViewCell.DragState.lifting](uicollectionviewcell/dragstate/lifting.md)
  The cell is being animated off of the surface of the collection view.
- [UICollectionViewCell.DragState.dragging](uicollectionviewcell/dragstate/dragging.md)
  The cell is being dragged.
### Initializers
- [init?(rawValue: Int)](uicollectionviewcell/dragstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func dragStateDidChange(UICollectionViewCell.DragState)](uicollectionviewcell/dragstatedidchange(_:).md)
  Called when the drag state of the cell changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/dragstate)*