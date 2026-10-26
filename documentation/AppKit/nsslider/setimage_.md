# setImage:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the image the slider displays in the bar behind its knob.

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

> **Deprecated**: No replacement needed.

## Declaration

```objc
- (void) setImage:(NSImage *) backgroundImage;
```

#### Discussion

The slider may scale and distort `barImage` to fit inside the bar.

The knob may cover part of the image. If you want the image to be visible all the time, you’re better off placing it near the slider.

## Parameters

- `backgroundImage`: The image to set.

## See Also

### Deprecated methods
- [- setKnobThickness:](./setknobthickness_.md)
- [- image](./image.md)
  Returns `nil`.
- [- title](./title.md)
  Returns the slider’s title.
- [- titleCell](./titlecell.md)
  This method has been deprecated. Returns `nil`.
- [- titleColor](./titlecolor.md)
  This method has been deprecated. Returns `nil`.
- [- titleFont](./titlefont.md)
  This method has been deprecated. Returns `nil`.
- [- setTitle:](./settitle_.md)
  Sets the title the slider displays in the bar behind its knob.
- [- setTitleCell:](./settitlecell_.md)
  Sets the cell used to draw the slider’s title.
- [- setTitleColor:](./settitlecolor_.md)
  Sets the color used to draw the slider’s title.
- [- setTitleFont:](./settitlefont_.md)
  Sets the font used to draw the slider’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/setimage:)*