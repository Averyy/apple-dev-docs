# convertFontTraits(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Converts font traits to a new traits mask value.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func convertFontTraits(_ traits: NSFontTraitMask) -> NSFontTraitMask
```

```objc
- (NSFontTraitMask) convertFontTraits:(NSFontTraitMask) traits;
```

## Return Value

The new traits mask value to be used by [`convert(_:)`](./convert%28_%29.md).

## Discussion

This method is intended to be invoked to query the font traits while the action message (usually [`changeFont:`](../../ObjectiveC/nsobject-swift.class/changefont_.md)) is being invoked when the current font action is either [`NSFontAction.addTraitFontAction`](../nsfontaction/addtraitfontaction.md) or [`NSFontAction.removeTraitFontAction`](../nsfontaction/removetraitfontaction.md).

## Parameters

- `traits`: The current font traits.

## See Also

### Converting Fonts Manually
- [func convert(NSFont, toFace: String) -> NSFont?](./convert%28_,toface%29.md)
  Returns a font whose traits are as similar as possible to those of the given font except for the typeface, which is changed to the given typeface.
- [func convert(NSFont, toFamily: String) -> NSFont](./convert%28_,tofamily%29.md)
  Returns a font whose traits are as similar as possible to those of the given font except for the font family, which is changed to the given family.
- [func convert(NSFont, toHaveTrait: NSFontTraitMask) -> NSFont](./convert%28_,tohavetrait%29.md)
  Returns a new version of the font object containing a single additional trait.
- [func convert(NSFont, toNotHaveTrait: NSFontTraitMask) -> NSFont](./convert%28_,tonothavetrait%29.md)
  Returns a new version of a font object without the specified traits.
- [func convert(NSFont, toSize: CGFloat) -> NSFont](./convert%28_,tosize%29.md)
  Returns a font object whose traits are the same as those of the given font, except for the size, which is changed to the given size.
- [func convertWeight(Bool, of: NSFont) -> NSFont](./convertweight%28_,of%29.md)
  Returns a font object whose weight is greater or lesser than that of the given font.
- [var currentFontAction: NSFontAction](./currentfontaction.md)
  The current font conversion action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/convertfonttraits(_:))*