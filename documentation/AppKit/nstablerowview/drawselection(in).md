# drawSelection(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the selected row.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func drawSelection(in dirtyRect: NSRect)
```

```objc
- (void) drawSelectionInRect:(NSRect) dirtyRect;
```

## Discussion

This method is only called if the selection should be drawn.

The selection will automatically be alpha-blended if the selection is animating in or out.

The default selection drawn is dependent on the [`selectionHighlightStyle`](../nstableview/selectionhighlightstyle-swift.property.md).

## Parameters

- `dirtyRect`: The rectangle that requires drawing.

## See Also

### Overriding Row View Display Characteristics
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color of the row.
- [func drawBackground(in: NSRect)](./drawbackground%28in%29.md)
  Draws the background of the row in the rectangle.
- [func drawDraggingDestinationFeedback(in: NSRect)](./drawdraggingdestinationfeedback%28in%29.md)
  Draws the row’s dragging destination feedback when the entire row is a drop target.
- [func drawSeparator(in: NSRect)](./drawseparator%28in%29.md)
  Draws the horizontal separator between table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/drawselection(in:))*