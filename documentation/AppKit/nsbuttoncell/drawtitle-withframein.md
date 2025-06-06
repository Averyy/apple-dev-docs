# drawTitle(_:withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Draws the button’s title centered vertically in a specified rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawTitle(_ title: NSAttributedString, withFrame frame: NSRect, in controlView: NSView) -> NSRect
```

#### Return Value

The bounding rectangle for the text of the title.

#### Discussion

This method is called automatically when the button is redrawn; you should not call it directly.

## Parameters

- `title`: The title of the button.
- `frame`: The rectangle in which to draw the title.
- `controlView`: The control being drawn.

## See Also

- [var attributedTitle: NSAttributedString](nsbuttoncell/attributedtitle.md)
  The title displayed by the button when it’s in its normal state as an attributed string.
- [var alternateTitle: String](nsbuttoncell/alternatetitle.md)
  The string displayed by the button when it’s in its alternate state.
- [func drawBezel(withFrame: NSRect, in: NSView)](nsbuttoncell/drawbezel(withframe:in:).md)
  Draws the border of the button using the current bezel style.
- [func drawImage(NSImage, withFrame: NSRect, in: NSView)](nsbuttoncell/drawimage(_:withframe:in:).md)
  Draws the image associated with the button’s current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/drawtitle(_:withframe:in:))*