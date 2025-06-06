# drawSwatch(in:)

**Framework**: AppKit  
**Kind**: method

Draws the current color in the specified rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
func drawSwatch(in rect: NSRect)
```

#### Discussion

Subclasses adorn the rectangle in some manner to indicate the type of color. This method is invoked by color wells, swatches, and other user interface objects that need to display colors.

## Parameters

- `rect`: The rectangle in which to draw the color.

## See Also

- [func set()](nscolor/set.md)
  Sets the color of subsequent drawing to the color that the color object represents.
- [func setFill()](nscolor/setfill.md)
  Sets the fill color of subsequent drawing to the color object’s color.
- [func setStroke()](nscolor/setstroke.md)
  Sets the stroke color of subsequent drawing to the color object’s color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/drawswatch(in:))*