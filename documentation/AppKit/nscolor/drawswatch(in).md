# drawSwatch(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the current color in the specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func drawSwatch(in rect: NSRect)
```

```objc
- (void) drawSwatchInRect:(NSRect) rect;
```

#### Discussion

Subclasses adorn the rectangle in some manner to indicate the type of color. This method is invoked by color wells, swatches, and other user interface objects that need to display colors.

## Parameters

- `rect`: The rectangle in which to draw the color.

## See Also

### Drawing with colors
- [func set()](./set%28%29.md)
  Sets the color of subsequent drawing to the color that the color object represents.
- [func setFill()](./setfill%28%29.md)
  Sets the fill color of subsequent drawing to the color object’s color.
- [func setStroke()](./setstroke%28%29.md)
  Sets the stroke color of subsequent drawing to the color object’s color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/drawswatch(in:))*