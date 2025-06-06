# convert(_:)

**Framework**: AppKit  
**Kind**: method

Converts the given font according to the object that initiated a font change, typically the Font panel or Font menu.

**Availability**:
- macOS ?+

## Declaration

```swift
func convert(_ fontObj: NSFont) -> NSFont
```

#### Return Value

The converted font, or `aFont` itself if the conversion isn’t possible.

#### Discussion

This method is invoked in response to an action message such as [`addFontTrait(_:)`](nsfontmanager/addfonttrait(_:).md) or [`modifyFontViaPanel(_:)`](nsfontmanager/modifyfontviapanel(_:).md). These initiating methods cause the font manager to query the sender for the action to take and the traits to change. See Converting Fonts Manually for more information.

## Parameters

- `fontObj`: The font to convert.

## See Also

- [func convert(NSFont, toFamily: String) -> NSFont](nsfontmanager/convert(_:tofamily:).md)
  Returns a font whose traits are as similar as possible to those of the given font except for the font family, which is changed to the given family.
- [func convert(NSFont, toSize: CGFloat) -> NSFont](nsfontmanager/convert(_:tosize:).md)
  Returns a font object whose traits are the same as those of the given font, except for the size, which is changed to the given size.
- [func convert(NSFont, toHaveTrait: NSFontTraitMask) -> NSFont](nsfontmanager/convert(_:tohavetrait:).md)
  Returns a new version of the font object containing a single additional trait.
- [func convert(NSFont, toNotHaveTrait: NSFontTraitMask) -> NSFont](nsfontmanager/convert(_:tonothavetrait:).md)
  Returns a new version of a font object without the specified traits.
- [func convertWeight(Bool, of: NSFont) -> NSFont](nsfontmanager/convertweight(_:of:).md)
  Returns a font object whose weight is greater or lesser than that of the given font.
- [func convert(NSFont, toFace: String) -> NSFont?](nsfontmanager/convert(_:toface:).md)
  Returns a font whose traits are as similar as possible to those of the given font except for the typeface, which is changed to the given typeface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager/convert(_:))*