# setDragState(_:animated:)

**Framework**: MapKit  
**Kind**: method

Sets the drag state for the annotation view.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setDragState(_ newDragState: MKAnnotationView.DragState, animated: Bool)
```

#### Discussion

Apps can override this method and use it to implement drag support for custom annotation views. As the system detects user actions that indicate a drag, it calls this method to update the drag state. In response to these changes, your custom implementation of this method needs to do the following:

- When the drag state changes to [`MKAnnotationView.DragState.starting`](mkannotationview/dragstate-swift.enum/starting.md), set the state to [`MKAnnotationView.DragState.dragging`](mkannotationview/dragstate-swift.enum/dragging.md). If you perform an animation to indicate the beginning of a drag, and the `animated` parameter is [`true`](https://developer.apple.com/documentation/Swift/true), perform that animation before changing the state.
- When the state changes to either [`MKAnnotationView.DragState.canceling`](mkannotationview/dragstate-swift.enum/canceling.md) or [`MKAnnotationView.DragState.ending`](mkannotationview/dragstate-swift.enum/ending.md), set the state to [`MKAnnotationView.DragState.none`](mkannotationview/dragstate-swift.enum/none.md). If you perform an animation at the end of a drag, and the `animated` parameter is [`true`](https://developer.apple.com/documentation/Swift/true), perform that animation before changing the state.

The default implementation of this method sets the value of the [`dragState`](mkannotationview/dragstate-swift.property.md) property to the value in the `newDragState` parameter only. Therefore, direct subclasses can call the inherited version of this method to change the drag state; otherwise, change the value in the [`isDraggable`](mkannotationview/isdraggable.md) property directly.

Changing the state to [`MKAnnotationView.DragState.dragging`](mkannotationview/dragstate-swift.enum/dragging.md) or [`MKAnnotationView.DragState.none`](mkannotationview/dragstate-swift.enum/none.md) is the way to signal to the map view when you finish performing animations. For example, when a drag operation begins for an annotation, the class executes an animation to lift the view off the map. Similarly, when the user drops the annotation, the class performs a drop animation. Even if you don’t perform any animations, call the inherited version of this method to update the [`dragState`](mkannotationview/dragstate-swift.property.md) property.

Don’t try to stop a new drag operation by changing the state from [`MKAnnotationView.DragState.starting`](mkannotationview/dragstate-swift.enum/starting.md) to [`MKAnnotationView.DragState.none`](mkannotationview/dragstate-swift.enum/none.md). If you don’t want your annotation view to be draggable, set the [`isDraggable`](mkannotationview/isdraggable.md) property to [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `newDragState`: The new drag state for the annotation view.
- `animated`: If  , the map view animates the change to the new drag state; otherwise, the map view makes the change without animations.

## See Also

- [var isDraggable: Bool](mkannotationview/isdraggable.md)
  A Boolean value that indicates whether the annotation view is draggable.
- [var dragState: MKAnnotationView.DragState](mkannotationview/dragstate-swift.property.md)
  The drag state of the annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/setdragstate(_:animated:))*