# drawDraggingDestinationFeedback(in:)

**Framework**: AppKit  
**Kind**: method

Draws the row’s dragging destination feedback when the entire row is a drop target.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func drawDraggingDestinationFeedback(in dirtyRect: NSRect)
```

#### Discussion

Overriding this method allows an application to draw custom dragging destination feedback when the entire row is a drop target.

This method only is called if [`isTargetForDropOperation`](nstablerowview/istargetfordropoperation.md) is [`true`](https://developer.apple.com/documentation/swift/true), and is only drawn based on the properties set, such as the group row style.

## Parameters

- `dirtyRect`: The rectangle that requires drawing.

## See Also

- [var backgroundColor: NSColor](nstablerowview/backgroundcolor.md)
  The background color of the row.
- [func drawBackground(in: NSRect)](nstablerowview/drawbackground(in:).md)
  Draws the background of the row in the rectangle.
- [func drawSelection(in: NSRect)](nstablerowview/drawselection(in:).md)
  Draws the selected row.
- [func drawSeparator(in: NSRect)](nstablerowview/drawseparator(in:).md)
  Draws the horizontal separator between table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/drawdraggingdestinationfeedback(in:))*