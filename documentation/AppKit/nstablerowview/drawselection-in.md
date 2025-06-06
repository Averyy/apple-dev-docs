# drawSelection(in:)

**Framework**: AppKit  
**Kind**: method

Draws the selected row.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func drawSelection(in dirtyRect: NSRect)
```

#### Discussion

This method is only called if the selection should be drawn.

The selection will automatically be alpha-blended if the selection is animating in or out.

The default selection drawn is dependent on the [`selectionHighlightStyle`](nstableview/selectionhighlightstyle-swift.property.md).

## Parameters

- `dirtyRect`: The rectangle that requires drawing.

## See Also

- [var backgroundColor: NSColor](nstablerowview/backgroundcolor.md)
  The background color of the row.
- [func drawBackground(in: NSRect)](nstablerowview/drawbackground(in:).md)
  Draws the background of the row in the rectangle.
- [func drawDraggingDestinationFeedback(in: NSRect)](nstablerowview/drawdraggingdestinationfeedback(in:).md)
  Draws the row’s dragging destination feedback when the entire row is a drop target.
- [func drawSeparator(in: NSRect)](nstablerowview/drawseparator(in:).md)
  Draws the horizontal separator between table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/drawselection(in:))*