# currentFontAction

**Framework**: AppKit  
**Kind**: property

The current font conversion action.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var currentFontAction: NSFontAction { get }
```

#### Discussion

The value of this property represents the current font action used by the [`convert(_:)`](nsfontmanager/convert(_:).md) method. This property is intended to be used to query the font conversion action while the action message (usually [`changeFont:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/changeFont:)) is being invoked.

## See Also

- [func convert(NSFont, toFace: String) -> NSFont?](nsfontmanager/convert(_:toface:).md)
  Returns a font whose traits are as similar as possible to those of the given font except for the typeface, which is changed to the given typeface.
- [func convert(NSFont, toFamily: String) -> NSFont](nsfontmanager/convert(_:tofamily:).md)
  Returns a font whose traits are as similar as possible to those of the given font except for the font family, which is changed to the given family.
- [func convert(NSFont, toHaveTrait: NSFontTraitMask) -> NSFont](nsfontmanager/convert(_:tohavetrait:).md)
  Returns a new version of the font object containing a single additional trait.
- [func convert(NSFont, toNotHaveTrait: NSFontTraitMask) -> NSFont](nsfontmanager/convert(_:tonothavetrait:).md)
  Returns a new version of a font object without the specified traits.
- [func convert(NSFont, toSize: CGFloat) -> NSFont](nsfontmanager/convert(_:tosize:).md)
  Returns a font object whose traits are the same as those of the given font, except for the size, which is changed to the given size.
- [func convertWeight(Bool, of: NSFont) -> NSFont](nsfontmanager/convertweight(_:of:).md)
  Returns a font object whose weight is greater or lesser than that of the given font.
- [func convertFontTraits(NSFontTraitMask) -> NSFontTraitMask](nsfontmanager/convertfonttraits(_:).md)
  Converts font traits to a new traits mask value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/currentfontaction)*