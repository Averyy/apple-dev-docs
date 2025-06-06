# NSFont.Weight

**Framework**: AppKit  
**Kind**: struct

System-defined font-weight values.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Weight
```

## Topics

### Font Weights
- [static let ultraLight: NSFont.Weight](nsfont/weight/ultralight.md)
  The font weight for system ultra light font.
- [static let thin: NSFont.Weight](nsfont/weight/thin.md)
  The font weight for system thin font.
- [static let light: NSFont.Weight](nsfont/weight/light.md)
  The font weight for system light font.
- [static let regular: NSFont.Weight](nsfont/weight/regular.md)
  The font weight for system regular font.
- [static let medium: NSFont.Weight](nsfont/weight/medium.md)
  The font weight for system medium font.
- [static let semibold: NSFont.Weight](nsfont/weight/semibold.md)
  The font weight for system semibold font.
- [static let bold: NSFont.Weight](nsfont/weight/bold.md)
  The font weight for system bold font.
- [static let heavy: NSFont.Weight](nsfont/weight/heavy.md)
  The font weight for system heavy font.
- [static let black: NSFont.Weight](nsfont/weight/black.md)
  The font weight for system black font.
### Initializers
- [init(CGFloat)](nsfont/weight/init(_:).md)
- [init(rawValue: CGFloat)](nsfont/weight/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [NSFont.TextStyle](nsfont/textstyle.md)
  Constants that specify the preferred text styles you use with fonts.
- [NSFont.TextStyleOptionKey](nsfont/textstyleoptionkey.md)
  The options that you apply when requesting the font or font descriptor of a preferred text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/weight)*