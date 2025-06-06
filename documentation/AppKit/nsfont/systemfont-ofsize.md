# systemFont(ofSize:)

**Framework**: AppKit  
**Kind**: method

Returns the standard system font with the specified size.

**Availability**:
- macOS ?+

## Declaration

```swift
class func systemFont(ofSize fontSize: CGFloat) -> NSFont
```

#### Return Value

A font object containing the system font at the specified size.

#### Discussion

Use the returned font for standard interface items, including button labels, menu items, and so on that use the default font appearance.

## Parameters

- `fontSize`: The desired font size specified in points. If you specify   or a negative number for this parameter, the method returns the system font at the default size.

## See Also

- [init?(name: String, size: CGFloat)](nsfont/init(name:size:).md)
  Creates a font object for the specified font name and font size.
- [class func userFixedPitchFont(ofSize: CGFloat) -> NSFont?](nsfont/userfixedpitchfont(ofsize:).md)
  Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), when that font should be fixed-pitch, in the specified size.
- [class func userFont(ofSize: CGFloat) -> NSFont?](nsfont/userfont(ofsize:).md)
  Returns the font used by default for documents and other text under the user’s control (that is, text whose font the user can normally change), in the specified size.
- [class func preferredFont(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFont](nsfont/preferredfont(fortextstyle:options:).md)
  Returns the font associated with the text style.
- [class func systemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/systemfont(ofsize:weight:).md)
  Returns the standard system font with the specified size and weight.
- [class func boldSystemFont(ofSize: CGFloat) -> NSFont](nsfont/boldsystemfont(ofsize:).md)
  Returns the standard system font in boldface type with the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/monospacedsystemfont(ofsize:weight:).md)
  Returns a monospace version of the system font with the specified size and weight.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](nsfont/monospaceddigitsystemfont(ofsize:weight:).md)
  Returns a version of the standard system font that contains monospaced digit glyphs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/systemfont(ofsize:))*