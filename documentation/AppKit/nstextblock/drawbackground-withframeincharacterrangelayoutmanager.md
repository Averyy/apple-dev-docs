# drawBackground(withFrame:in:characterRange:layoutManager:)

**Framework**: AppKit  
**Kind**: method

Called by the layout manager to draw any colors and other decorations before the text is drawn.

**Availability**:
- macOS ?+

## Declaration

```swift
func drawBackground(withFrame frameRect: NSRect, in controlView: NSView, characterRange charRange: NSRange, layoutManager: NSLayoutManager)
```

## Parameters

- `frameRect`: The bounds rectangle in view coordinates.
- `controlView`: The view in which drawing occurs.
- `charRange`: The range of the characters in the   object whose glyphs are to be drawn.
- `layoutManager`: The layout manager controlling the typesetting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/drawbackground(withframe:in:characterrange:layoutmanager:))*