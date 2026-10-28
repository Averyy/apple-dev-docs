# drawBackground(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the background of the row in the rectangle.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func drawBackground(in dirtyRect: NSRect)
```

```objc
- (void) drawBackgroundInRect:(NSRect) dirtyRect;
```

## Discussion

Overriding this method allows an application to draw a custom background for a table row view.

By default, this method draws the background color or group row style as appropriate for the row. This method also draws the “below look” for a drop target if [`isTargetForDropOperation`](./istargetfordropoperation.md) is [`true`](../../Swift/true.md).

## Parameters

- `dirtyRect`: The rectangle that requires drawing.

## See Also

### Overriding Row View Display Characteristics
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color of the row.
- [func drawDraggingDestinationFeedback(in: NSRect)](./drawdraggingdestinationfeedback%28in%29.md)
  Draws the row’s dragging destination feedback when the entire row is a drop target.
- [func drawSelection(in: NSRect)](./drawselection%28in%29.md)
  Draws the selected row.
- [func drawSeparator(in: NSRect)](./drawseparator%28in%29.md)
  Draws the horizontal separator between table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/drawbackground(in:))*