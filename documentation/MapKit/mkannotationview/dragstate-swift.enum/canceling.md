# MKAnnotationView.DragState.canceling

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

An annotation view cancels drag operation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
case canceling
```

```c
MKAnnotationViewDragStateCanceling
```

#### Discussion

A user action causes the view to cancel the drag operation. You can put an annotation view into this state to abort the operation.

## See Also

### Constants
- [MKAnnotationView.DragState.none](./none.md)
  An annotation view that doesn’t have a drag operation.
- [MKAnnotationView.DragState.starting](./starting.md)
  An annotation view begins dragging.
- [MKAnnotationView.DragState.dragging](./dragging.md)
  An annotation view is actively dragging.
- [MKAnnotationView.DragState.ending](./ending.md)
  An annotation view ends dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/canceling)*