# slideDraggedImage(to:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Slides the image to a specified location.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func slideDraggedImage(to screenPoint: NSPoint)
```

#### Discussion

This method can be used to adjust the location to which the dragged image will slide back if the drag is rejected.

It should only be invoked from within the destination’s implementation of prepareForDragOperation:, and will only have effect if the destination rejects the drag.

This method is invoked after the user has released the image but before it is removed from the screen.

##### Special Considerations

This method has been available since OS X v 10.0, however it was not implemented until OS X v 10.5. Previous to that version, it did nothing.

## Parameters

- `screenPoint`: A point that specifies a location in the screen coordinate system.

## See Also

- [var animatesToDestination: Bool](nsdragginginfo/animatestodestination.md)
  A Boolean value that indicates whether the dragging formation animates while the drag is over the destination.
- [var draggingFormation: NSDraggingFormation](nsdragginginfo/draggingformation.md)
  The formation of the dragging items while the drag is over the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/slidedraggedimage(to:))*