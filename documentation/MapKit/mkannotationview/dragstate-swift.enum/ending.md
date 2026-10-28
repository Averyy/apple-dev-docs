# MKAnnotationView.DragState.ending

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

An annotation view ends dragging.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
case ending
```

```c
MKAnnotationViewDragStateEnding
```

## Discussion

A user action indicates the user dropped the view. The map view automatically moves annotation views to this state in response to appropriate user actions.

## See Also

### Constants
- [MKAnnotationView.DragState.none](./none.md)
  An annotation view that doesn’t have a drag operation.
- [MKAnnotationView.DragState.starting](./starting.md)
  An annotation view begins dragging.
- [MKAnnotationView.DragState.dragging](./dragging.md)
  An annotation view is actively dragging.
- [MKAnnotationView.DragState.canceling](./canceling.md)
  An annotation view cancels drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/ending)*