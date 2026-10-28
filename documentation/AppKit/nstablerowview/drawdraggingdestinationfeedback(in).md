# drawDraggingDestinationFeedback(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the row’s dragging destination feedback when the entire row is a drop target.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func drawDraggingDestinationFeedback(in dirtyRect: NSRect)
```

```objc
- (void) drawDraggingDestinationFeedbackInRect:(NSRect) dirtyRect;
```

## Discussion

Overriding this method allows an application to draw custom dragging destination feedback when the entire row is a drop target.

This method only is called if [`isTargetForDropOperation`](./istargetfordropoperation.md) is [`true`](../../Swift/true.md), and is only drawn based on the properties set, such as the group row style.

## Parameters

- `dirtyRect`: The rectangle that requires drawing.

## See Also

### Overriding Row View Display Characteristics
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The background color of the row.
- [func drawBackground(in: NSRect)](./drawbackground%28in%29.md)
  Draws the background of the row in the rectangle.
- [func drawSelection(in: NSRect)](./drawselection%28in%29.md)
  Draws the selected row.
- [func drawSeparator(in: NSRect)](./drawseparator%28in%29.md)
  Draws the horizontal separator between table rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/drawdraggingdestinationfeedback(in:))*