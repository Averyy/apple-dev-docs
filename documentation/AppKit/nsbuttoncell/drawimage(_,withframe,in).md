# drawImage(_:withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the image associated with the button’s current state.

**Availability**:
- macOS

## Declaration

```swift
func drawImage(_ image: NSImage, withFrame frame: NSRect, in controlView: NSView)
```

```objc
- (void) drawImage:(NSImage *) image withFrame:(NSRect) frame inView:(NSView *) controlView;
```

#### Discussion

This method is called automatically when the button is redrawn; you should not call it directly.

You specify the primary and alternate images for the button using Interface Builder.

## Parameters

- `image`: The image associated with the button’s current state.
- `frame`: The bounding rectangle of the button.
- `controlView`: The control being drawn.

## See Also

### Related Documentation
- [var alternateImage: NSImage?](./alternateimage.md)
  The image the button displays in its alternate state.
### Drawing the Button Content
- [func drawBezel(withFrame: NSRect, in: NSView)](./drawbezel%28withframe,in%29.md)
  Draws the border of the button using the current bezel style.
- [func drawTitle(NSAttributedString, withFrame: NSRect, in: NSView) -> NSRect](./drawtitle%28_,withframe,in%29.md)
  Draws the button’s title centered vertically in a specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/drawimage(_:withframe:in:))*