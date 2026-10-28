# changeFont:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Informs responders of a font change.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (void) changeFont:(id) sender;
```

## Discussion

Generally this change is because the user changed the font either in the selection of a rich text field or in a whole plain text field. Any object that contains a font the user can change must respond to the [`changeFont:`](./changefont_.md) message by sending a [`convert(_:)`](../../AppKit/nsfontmanager/convert%28_%29.md) message back to `sender` (an NSFontManager object) for each font in the selection. For more information, see Responding to Font Changes.

Be aware that [`selectedFont`](../../AppKit/nsfontmanager/selectedfont.md) at this point may return unpredictable results. The font in this property may not be the last font selected, or there may be multiple fonts selected at the time [`changeFont:`](./changefont_.md) is called. The use of [`selectedFont`](../../AppKit/nsfontmanager/selectedfont.md) from within [`changeFont:`](./changefont_.md) is strongly discouraged.

## Parameters

- `sender`: The object that sent the message.

## See Also

### Related Documentation
- [func convert(NSFont, toFamily: String) -> NSFont](../../AppKit/nsfontmanager/convert%28_,tofamily%29.md)
  Returns a font whose traits are as similar as possible to those of the given font except for the font family, which is changed to the given family.
- [func addFontTrait(Any?)](../../AppKit/nsfontmanager/addfonttrait%28_%29.md)
  Adds a trait to the font.
- [func convert(NSFont, toSize: CGFloat) -> NSFont](../../AppKit/nsfontmanager/convert%28_,tosize%29.md)
  Returns a font object whose traits are the same as those of the given font, except for the size, which is changed to the given size.
- [func convert(NSFont, toHaveTrait: NSFontTraitMask) -> NSFont](../../AppKit/nsfontmanager/convert%28_,tohavetrait%29.md)
  Returns a new version of the font object containing a single additional trait.
- [func modifyFont(Any?)](../../AppKit/nsfontmanager/modifyfont%28_%29.md)
  Modifies a trait of the font.
- [func convert(NSFont, toNotHaveTrait: NSFontTraitMask) -> NSFont](../../AppKit/nsfontmanager/convert%28_,tonothavetrait%29.md)
  Returns a new version of a font object without the specified traits.
- [func modifyFontViaPanel(Any?)](../../AppKit/nsfontmanager/modifyfontviapanel%28_%29.md)
  Modifies a font trait using input from the Font panel.
- [func convertWeight(Bool, of: NSFont) -> NSFont](../../AppKit/nsfontmanager/convertweight%28_,of%29.md)
  Returns a font object whose weight is greater or lesser than that of the given font.
- [func convert(NSFont, toFace: String) -> NSFont?](../../AppKit/nsfontmanager/convert%28_,toface%29.md)
  Returns a font whose traits are as similar as possible to those of the given font except for the typeface, which is changed to the given typeface.
- [func removeFontTrait(Any?)](../../AppKit/nsfontmanager/removefonttrait%28_%29.md)
  Removes a trait from the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/changefont:)*