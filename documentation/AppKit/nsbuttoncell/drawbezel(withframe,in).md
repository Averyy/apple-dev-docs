# drawBezel(withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the border of the button using the current bezel style.

**Availability**:
- macOS

## Declaration

```swift
func drawBezel(withFrame frame: NSRect, in controlView: NSView)
```

```objc
- (void) drawBezelWithFrame:(NSRect) frame inView:(NSView *) controlView;
```

#### Discussion

This method is called automatically when the button is redrawn; you should not call it directly.

## Parameters

- `frame`: The bounding rectangle of the button.
- `controlView`: The control being drawn.

## See Also

### Related Documentation
- [var bezelStyle: NSButton.BezelStyle](./bezelstyle.md)
  The appearance of the button’s border, if it has one.
### Drawing the Button Content
- [func drawImage(NSImage, withFrame: NSRect, in: NSView)](./drawimage%28_,withframe,in%29.md)
  Draws the image associated with the button’s current state.
- [func drawTitle(NSAttributedString, withFrame: NSRect, in: NSView) -> NSRect](./drawtitle%28_,withframe,in%29.md)
  Draws the button’s title centered vertically in a specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/drawbezel(withframe:in:))*