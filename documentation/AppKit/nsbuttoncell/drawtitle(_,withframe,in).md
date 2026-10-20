# drawTitle(_:withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the button’s title centered vertically in a specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func drawTitle(_ title: NSAttributedString, withFrame frame: NSRect, in controlView: NSView) -> NSRect
```

```objc
- (NSRect) drawTitle:(NSAttributedString *) title withFrame:(NSRect) frame inView:(NSView *) controlView;
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

### Related Documentation
- [var attributedTitle: NSAttributedString](./attributedtitle.md)
  The title displayed by the button when it’s in its normal state as an attributed string.
- [var alternateTitle: String](./alternatetitle.md)
  The string displayed by the button when it’s in its alternate state.
### Drawing the Button Content
- [func drawBezel(withFrame: NSRect, in: NSView)](./drawbezel%28withframe,in%29.md)
  Draws the border of the button using the current bezel style.
- [func drawImage(NSImage, withFrame: NSRect, in: NSView)](./drawimage%28_,withframe,in%29.md)
  Draws the image associated with the button’s current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/drawtitle(_:withframe:in:))*