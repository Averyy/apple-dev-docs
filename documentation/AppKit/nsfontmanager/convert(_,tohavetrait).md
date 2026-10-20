# convert(_:toHaveTrait:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a new version of the font object containing a single additional trait.

**Availability**:
- macOS

## Declaration

```swift
func convert(_ fontObj: NSFont, toHaveTrait trait: NSFontTraitMask) -> NSFont
```

```objc
- (NSFont *) convertFont:(NSFont *) fontObj toHaveTrait:(NSFontTraitMask) trait;
```

#### Return Value

A font with matching traits including the given trait, or `aFont` if it can’t be converted.

#### Discussion

Using `NSUnboldFontMask` or `NSUnitalicFontMask` removes the bold or italic trait, respectively.

## Parameters

- `fontObj`: The font whose traits are matched.
- `trait`: The new trait; may be any one of the traits described in `Constants`. Using `NSUnboldFontMask` or `NSUnitalicFontMask` removes the bold or italic trait, respectively.

## See Also

### Related Documentation
- [func convert(NSFont) -> NSFont](./convert%28_%29.md)
  Converts the given font according to the object that initiated a font change, typically the Font panel or Font menu.
### Converting Fonts Manually
- [func convert(NSFont, toFace: String) -> NSFont?](./convert%28_,toface%29.md)
  Returns a font whose traits are as similar as possible to those of the given font except for the typeface, which is changed to the given typeface.
- [func convert(NSFont, toFamily: String) -> NSFont](./convert%28_,tofamily%29.md)
  Returns a font whose traits are as similar as possible to those of the given font except for the font family, which is changed to the given family.
- [func convert(NSFont, toNotHaveTrait: NSFontTraitMask) -> NSFont](./convert%28_,tonothavetrait%29.md)
  Returns a new version of a font object without the specified traits.
- [func convert(NSFont, toSize: CGFloat) -> NSFont](./convert%28_,tosize%29.md)
  Returns a font object whose traits are the same as those of the given font, except for the size, which is changed to the given size.
- [func convertWeight(Bool, of: NSFont) -> NSFont](./convertweight%28_,of%29.md)
  Returns a font object whose weight is greater or lesser than that of the given font.
- [var currentFontAction: NSFontAction](./currentfontaction.md)
  The current font conversion action.
- [func convertFontTraits(NSFontTraitMask) -> NSFontTraitMask](./convertfonttraits%28_%29.md)
  Converts font traits to a new traits mask value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/convert(_:tohavetrait:))*