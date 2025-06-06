# MKAnnotationView.DragState.starting

**Framework**: MapKit  
**Kind**: case

An annotation view begins dragging.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
case starting
```

#### Discussion

A user action causes the view to begin the drag operation. The map view automatically moves annotation views to this state in response to appropriate user actions.

## See Also

- [MKAnnotationView.DragState.none](mkannotationview/dragstate-swift.enum/none.md)
  An annotation view that doesn’t have a drag operation.
- [MKAnnotationView.DragState.dragging](mkannotationview/dragstate-swift.enum/dragging.md)
  An annotation view is actively dragging.
- [MKAnnotationView.DragState.canceling](mkannotationview/dragstate-swift.enum/canceling.md)
  An annotation view cancels drag operation.
- [MKAnnotationView.DragState.ending](mkannotationview/dragstate-swift.enum/ending.md)
  An annotation view ends dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/starting)*