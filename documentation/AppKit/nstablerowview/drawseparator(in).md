# drawSeparator(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the horizontal separator between table rows.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func drawSeparator(in dirtyRect: NSRect)
```

```objc
- (void) drawSeparatorInRect:(NSRect) dirtyRect;
```

#### Discussion

By default, the separator is only drawn if the enclosing table’s [`gridStyleMask`](../nstableview/gridstylemask.md) is set to include a horizontal separator.

The separator should be drawn at the bottom of the row view, indicating a separation from this row and the next.

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
- [func drawSelection(in: NSRect)](./drawselection%28in%29.md)
  Draws the selected row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/drawseparator(in:))*