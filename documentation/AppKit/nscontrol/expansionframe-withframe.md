# expansionFrame(withFrame:)

**Framework**: AppKit  
**Kind**: method

The frame in which a tool tip can be displayed, if needed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func expansionFrame(withFrame contentFrame: NSRect) -> NSRect
```

#### Return Value

The frame in which the tool tip should be displayed, or [`NSZeroRect`](https://developer.apple.com/documentation/Foundation/NSZeroRect) by default.

#### Discussion

This method lets the control  return an expansion tool tip frame if `contentFrame` is too small for the entire contents in the view. When the pointer hovers over the text in certain controls, the full contents will be shown in a special floating tool tip view. If the frame is big enough to display the contents, return an empty rect from this method and no expansion tool tip view will be shown. Note that some subclasses, such as [`NSTextField`](nstextfield.md), return the proper frame when required.

## Parameters

- `contentFrame`: The frame of the control.

## See Also

- [func draw(withExpansionFrame: NSRect, in: NSView)](nscontrol/draw(withexpansionframe:in:).md)
  Performs custom expansion tool tip drawing.
- [var allowsExpansionToolTips: Bool](nscontrol/allowsexpansiontooltips.md)
  A Boolean value that indicates whether expansion tool tips are shown when the control is hovered over.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/expansionframe(withframe:))*