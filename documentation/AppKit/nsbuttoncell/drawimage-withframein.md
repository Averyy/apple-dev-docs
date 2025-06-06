# drawImage(_:withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Draws the image associated with the button’s current state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawImage(_ image: NSImage, withFrame frame: NSRect, in controlView: NSView)
```

#### Discussion

This method is called automatically when the button is redrawn; you should not call it directly.

You specify the primary and alternate images for the button using Interface Builder.

## Parameters

- `image`: The image associated with the button’s current state.
- `frame`: The bounding rectangle of the button.
- `controlView`: The control being drawn.

## See Also

- [var alternateImage: NSImage?](nsbuttoncell/alternateimage.md)
  The image the button displays in its alternate state.
- [func drawBezel(withFrame: NSRect, in: NSView)](nsbuttoncell/drawbezel(withframe:in:).md)
  Draws the border of the button using the current bezel style.
- [func drawTitle(NSAttributedString, withFrame: NSRect, in: NSView) -> NSRect](nsbuttoncell/drawtitle(_:withframe:in:).md)
  Draws the button’s title centered vertically in a specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/drawimage(_:withframe:in:))*