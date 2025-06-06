# mouseEntered(with:frame:in:)

**Framework**: AppKit  
**Kind**: method

Displays the cell component over which the mouse is hovering.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func mouseEntered(with event: NSEvent, frame: NSRect, in view: NSView)
```

#### Discussion

The `NSPathCell` object dynamically animates to display the component that the mouse is hovering over using mouse-entered and mouse-exited events. The control should call these methods to correctly display the hovered component to the user. The control can acquire rectangles to track using [`rect(of:withFrame:in:)`](nspathcell/rect(of:withframe:in:).md).

## Parameters

- `event`: The mouse-entered event.
- `frame`: The frame in which the cell is located.
- `view`: The view in which the cell is located.

## See Also

- [func mouseExited(with: NSEvent, frame: NSRect, in: NSView)](nspathcell/mouseexited(with:frame:in:).md)
  Hides the cell component over which the mouse is hovering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/mouseentered(with:frame:in:))*