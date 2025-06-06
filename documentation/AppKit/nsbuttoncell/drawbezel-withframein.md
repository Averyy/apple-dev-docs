# drawBezel(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Draws the border of the button using the current bezel style.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawBezel(withFrame frame: NSRect, in controlView: NSView)
```

#### Discussion

This method is called automatically when the button is redrawn; you should not call it directly.

## Parameters

- `frame`: The bounding rectangle of the button.
- `controlView`: The control being drawn.

## See Also

- [var bezelStyle: NSButton.BezelStyle](nsbuttoncell/bezelstyle.md)
  The appearance of the button’s border, if it has one.
- [func drawImage(NSImage, withFrame: NSRect, in: NSView)](nsbuttoncell/drawimage(_:withframe:in:).md)
  Draws the image associated with the button’s current state.
- [func drawTitle(NSAttributedString, withFrame: NSRect, in: NSView) -> NSRect](nsbuttoncell/drawtitle(_:withframe:in:).md)
  Draws the button’s title centered vertically in a specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/drawbezel(withframe:in:))*