# setTitleCell:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the cell used to draw the slider’s title.

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

> **Deprecated**: No replacement needed.

## Declaration

```objc
- (void) setTitleCell:(NSCell *) cell;
```

#### Discussion

You only need to invoke this method if the default title cell, `NSTextFieldCell`, doesn’t suit your needs—that is, you want to display the title in a manner that `NSTextFieldCell` doesn’t permit. When you do choose to override the default, `titleCell` should be an instance of a subclass of `NSTextFieldCell`.

## Parameters

- `cell`: The cell used to draw the title.

## See Also

### Deprecated methods
- [- setKnobThickness:](./setknobthickness_.md)
- [- setImage:](./setimage_.md)
  Sets the image the slider displays in the bar behind its knob.
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
- [- setTitleColor:](./settitlecolor_.md)
  Sets the color used to draw the slider’s title.
- [- setTitleFont:](./settitlefont_.md)
  Sets the font used to draw the slider’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/settitlecell:)*