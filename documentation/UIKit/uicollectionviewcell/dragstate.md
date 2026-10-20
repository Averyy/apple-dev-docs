# UICollectionViewCell.DragState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UICollectionViewCellDragState : NSInteger;
```

## Topics

### Constants
- [UICollectionViewCell.DragState.none](./dragstate/none.md)
  The cell isn’t involved in a drag.
- [UICollectionViewCell.DragState.lifting](./dragstate/lifting.md)
  The cell is being animated off of the surface of the collection view.
- [UICollectionViewCell.DragState.dragging](./dragstate/dragging.md)
  The cell is being dragged.
### Initializers
- [init?(rawValue: Int)](./dragstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing drag state changes
- [func dragStateDidChange(UICollectionViewCell.DragState)](./dragstatedidchange%28_%29.md)
  Called when the drag state of the cell changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcell/dragstate)*