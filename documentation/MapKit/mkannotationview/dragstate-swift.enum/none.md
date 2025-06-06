# MKAnnotationView.DragState.none

**Framework**: MapKit  
**Kind**: case

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

#### Discussion

The view isn’t involved in a drag operation. The annotation view is responsible for returning itself to this state when a drag ends or cancels.

## See Also

- [MKAnnotationView.DragState.starting](mkannotationview/dragstate-swift.enum/starting.md)
  An annotation view begins dragging.
- [MKAnnotationView.DragState.dragging](mkannotationview/dragstate-swift.enum/dragging.md)
  An annotation view is actively dragging.
- [MKAnnotationView.DragState.canceling](mkannotationview/dragstate-swift.enum/canceling.md)
  An annotation view cancels drag operation.
- [MKAnnotationView.DragState.ending](mkannotationview/dragstate-swift.enum/ending.md)
  An annotation view ends dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/none)*