# expansionFrame(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Returns the expansion cell frame for the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func expansionFrame(withFrame cellFrame: NSRect, in view: NSView) -> NSRect
```

#### Return Value

The expansion cell frame for the receiver. If the frame is not too small, return an empty rect ([`NSZeroRect`](https://developer.apple.com/documentation/Foundation/NSZeroRect)), and no expansion tool tip view will be shown.

#### Discussion

This method allows the cell to return an expansion cell frame if `cellFrame` is too small for the entire contents in the view. When the mouse is hovered over the cell in certain controls, the full cell contents are shown in a special floating tool tip view. By default, `NSCell` returns `NSZeroRect`, while some subclasses (such as `NSTextFieldCell`) will return the proper frame when required.

## Parameters

- `cellFrame`: The frame for the receiver.
- `view`: The view in which the receiver will be drawn.

## See Also

- [func draw(withExpansionFrame: NSRect, in: NSView)](nscell/draw(withexpansionframe:in:).md)
  Instructs the receiver to draw in an expansion frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/expansionframe(withframe:in:))*