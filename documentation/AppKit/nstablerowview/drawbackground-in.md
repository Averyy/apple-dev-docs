# drawBackground(in:)

**Framework**: AppKit  
**Kind**: method

Draws the background of the row in the rectangle.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func drawBackground(in dirtyRect: NSRect)
```

#### Discussion

Overriding this method allows an application to draw a custom background for a table row view.

By default, this method draws the background color or group row style as appropriate for the row. This method also draws the “below look” for a drop target if [`isTargetForDropOperation`](nstablerowview/istargetfordropoperation.md) is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `dirtyRect`: The rectangle that requires drawing.

## See Also

- [var backgroundColor: NSColor](nstablerowview/backgroundcolor.md)
  The background color of the row.
- [func drawDraggingDestinationFeedback(in: NSRect)](nstablerowview/drawdraggingdestinationfeedback(in:).md)
  Draws the row’s dragging destination feedback when the entire row is a drop target.
- [func drawSelection(in: NSRect)](nstablerowview/drawselection(in:).md)
  Draws the selected row.
- [func drawSeparator(in: NSRect)](nstablerowview/drawseparator(in:).md)
  Draws the horizontal separator between table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/drawbackground(in:))*