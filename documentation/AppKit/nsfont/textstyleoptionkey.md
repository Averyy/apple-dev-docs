# NSFont.TextStyleOptionKey

**Framework**: AppKit  
**Kind**: struct

The options that you apply when requesting the font or font descriptor of a preferred text style.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct TextStyleOptionKey
```

#### Discussion

Pass a dictionary that contains any combination of these keys and their corresponding values to [`preferredFont(forTextStyle:options:)`](nsfont/preferredfont(fortextstyle:options:).md) or [`preferredFontDescriptor(forTextStyle:options:)`](nsfontdescriptor/preferredfontdescriptor(fortextstyle:options:).md) to further configure the returned font or font descriptor.

## Topics

### Initializers
- [init(rawValue: String)](nsfont/textstyleoptionkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/textstyleoptionkey)*