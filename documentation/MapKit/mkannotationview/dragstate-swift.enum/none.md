# MKAnnotationView.DragState.none

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

An annotation view that doesn’t have a drag operation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
case none
```

```c
MKAnnotationViewDragStateNone
```

## Discussion

The view isn’t involved in a drag operation. The annotation view is responsible for returning itself to this state when a drag ends or cancels.

## See Also

### Constants
- [MKAnnotationView.DragState.starting](./starting.md)
  An annotation view begins dragging.
- [MKAnnotationView.DragState.dragging](./dragging.md)
  An annotation view is actively dragging.
- [MKAnnotationView.DragState.canceling](./canceling.md)
  An annotation view cancels drag operation.
- [MKAnnotationView.DragState.ending](./ending.md)
  An annotation view ends dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/none)*