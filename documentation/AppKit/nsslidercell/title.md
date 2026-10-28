# title

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the slider’s title.

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

> **Deprecated**: A slider doesn’t include a title.

## Declaration

```objc
- (NSString *) title;
```

## Return Value

The title. The default title is the empty string (`@""`).

## See Also

### Deprecated methods
- [- setTitle:](./settitle_.md)
  Sets the title in the bar behind the slider’s knob.
- [- titleCell](./titlecell.md)
  Returns `nil`.
- [- setTitleCell:](./settitlecell_.md)
  Sets the cell used to draw the slider’s title.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/title)*