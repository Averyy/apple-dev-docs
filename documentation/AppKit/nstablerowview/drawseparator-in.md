# drawSeparator(in:)

**Framework**: AppKit  
**Kind**: method

Draws the horizontal separator between table rows.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func drawSeparator(in dirtyRect: NSRect)
```

#### Discussion

By default, the separator is only drawn if the enclosing table’s [`gridStyleMask`](nstableview/gridstylemask.md) is set to include a horizontal separator.

The separator should be drawn at the bottom of the row view, indicating a separation from this row and the next.

## Parameters

- `dirtyRect`: The rectangle that requires drawing.

## See Also

- [var backgroundColor: NSColor](nstablerowview/backgroundcolor.md)
  The background color of the row.
- [func drawBackground(in: NSRect)](nstablerowview/drawbackground(in:).md)
  Draws the background of the row in the rectangle.
- [func drawDraggingDestinationFeedback(in: NSRect)](nstablerowview/drawdraggingdestinationfeedback(in:).md)
  Draws the row’s dragging destination feedback when the entire row is a drop target.
- [func drawSelection(in: NSRect)](nstablerowview/drawselection(in:).md)
  Draws the selected row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/drawseparator(in:))*