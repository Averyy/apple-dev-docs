# animatesToDestination

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the dragging formation animates while the drag is over the destination.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var animatesToDestination: Bool { get set }
```

#### Discussion

During the conclusion of an accepted drag, if this property is set to [`true`](https://developer.apple.com/documentation/Swift/true), the drag manager will animate each dragging image to their [`NSDraggingFormation.none`](nsdraggingformation/none.md) locations. Otherwise, the drag images are removed without any animation.

This property is inspected between prepareForDragOperation: and performDragOperation:. You should enumerate through the dragging items during performDragOperation: to set the item’s [`draggingFrame`](nsdraggingitem/draggingframe.md) to the correct destinations.

## See Also

- [func slideDraggedImage(to: NSPoint)](nsdragginginfo/slidedraggedimage(to:).md)
  Slides the image to a specified location.
- [var draggingFormation: NSDraggingFormation](nsdragginginfo/draggingformation.md)
  The formation of the dragging items while the drag is over the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/animatestodestination)*