# setTitleCell:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the cell used to draw the slider’s title.

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

> **Deprecated**: A slider doesn’t include a title.

## Declaration

```objc
- (void) setTitleCell:(NSCell *) cell;
```

## Discussion

You only need to call this method if the default title cell, `NSTextFieldCell`, doesn’t suit your needs—that is, if you want to display the title in a manner that `NSTextFieldCell` doesn’t permit. When you do choose to override the default, `aCell` should be an instance of a subclass of `NSTextFieldCell`.

## See Also

### Deprecated methods
- [- title](./title.md)
  Returns the slider’s title.
- [- setTitle:](./settitle_.md)
  Sets the title in the bar behind the slider’s knob.
- [- titleCell](./titlecell.md)
  Returns `nil`.
- [- titleFont](./titlefont.md)
  Returns `nil`.
- [- titleColor](./titlecolor.md)
  Returns `nil`.
- [- setTitleFont:](./settitlefont_.md)
  Sets the font used to draw the slider’s title.
- [- setTitleColor:](./settitlecolor_.md)
  Sets the color used to draw the slider’s title.
- [- image](./image.md)
- [- setImage:](./setimage_.md)
- [- setKnobThickness:](./setknobthickness_.md)
  The thickness of the slider knob, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/settitlecell:)*