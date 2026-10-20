# MKAnnotationView.DragState.starting

**Framework**: MapKit  
**Kind**: case  
**Role**: Case

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

```c
MKAnnotationViewDragStateStarting
```

#### Discussion

A user action causes the view to begin the drag operation. The map view automatically moves annotation views to this state in response to appropriate user actions.

## See Also

### Constants
- [MKAnnotationView.DragState.none](./none.md)
  An annotation view that doesn’t have a drag operation.
- [MKAnnotationView.DragState.dragging](./dragging.md)
  An annotation view is actively dragging.
- [MKAnnotationView.DragState.canceling](./canceling.md)
  An annotation view cancels drag operation.
- [MKAnnotationView.DragState.ending](./ending.md)
  An annotation view ends dragging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/dragstate-swift.enum/starting)*