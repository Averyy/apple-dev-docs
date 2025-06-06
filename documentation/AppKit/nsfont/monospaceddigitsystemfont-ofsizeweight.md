# monospacedDigitSystemFont(ofSize:weight:)

**Framework**: AppKit  
**Kind**: method

Returns a version of the standard system font that contains monospaced digit glyphs.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class func monospacedDigitSystemFont(ofSize fontSize: CGFloat, weight: NSFont.Weight) -> NSFont
```

#### Return Value

A font object containing the system font with monospace digits at the specified size and weight.

#### Discussion

The font returned by this method has monospaced digit glyphs. Glyphs for other characters and symbols may be wider or narrower than the monospaced characters. To ensure the font uses fixed spacing for all characters, apply the [`fixedAdvance`](nsfontdescriptor/attributename/fixedadvance.md) attribute to the any strings you render.

## Parameters

- `fontSize`: The desired font size specified in points. If you specify   or a negative number for this parameter, the method returns the system font at the default size.
- `weight`: The desired weight of font lines, specified as one of the constants in  .

## See Also

- [class func preferredFont(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFont](nsfont/preferredfont(fortextstyle:options:).md)
  Returns the font associated with the text style.
- [class func systemFont(ofSize: CGFloat) -> NSFont](nsfont/systemfont(ofsize:).md)
  Returns the standard system font with the specified size.
- [class func systemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/systemfont(ofsize:weight:).md)
  Returns the standard system font with the specified size and weight.
- [class func boldSystemFont(ofSize: CGFloat) -> NSFont](nsfont/boldsystemfont(ofsize:).md)
  Returns the standard system font in boldface type with the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/monospacedsystemfont(ofsize:weight:).md)
  Returns a monospace version of the system font with the specified size and weight.
- [class var systemFontSize: CGFloat](nsfont/systemfontsize.md)
  Returns the size of the standard system font.
- [class var smallSystemFontSize: CGFloat](nsfont/smallsystemfontsize.md)
  Returns the size of the standard small system font.
- [NSFont.Weight](nsfont/weight.md)
  System-defined font-weight values.
- [NSFont.TextStyle](nsfont/textstyle.md)
  Constants that specify the preferred text styles you use with fonts.
- [NSFont.TextStyleOptionKey](nsfont/textstyleoptionkey.md)
  The options that you apply when requesting the font or font descriptor of a preferred text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/monospaceddigitsystemfont(ofsize:weight:))*