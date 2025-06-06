# NSFont.TextStyle

**Framework**: AppKit  
**Kind**: struct

Constants that specify the preferred text styles you use with fonts.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct TextStyle
```

#### Discussion

Pass these constants to [`preferredFont(forTextStyle:options:)`](nsfont/preferredfont(fortextstyle:options:).md) or [`preferredFontDescriptor(forTextStyle:options:)`](nsfontdescriptor/preferredfontdescriptor(fortextstyle:options:).md) to retrieve the corresponding font or font descriptor.

## Topics

### Constants
- [static let body: NSFont.TextStyle](nsfont/textstyle/body.md)
  The font you use for body text.
- [static let callout: NSFont.TextStyle](nsfont/textstyle/callout.md)
  The font you use for callouts.
- [static let caption1: NSFont.TextStyle](nsfont/textstyle/caption1.md)
  The font you use for standard captions.
- [static let caption2: NSFont.TextStyle](nsfont/textstyle/caption2.md)
  The font you use for alternate captions.
- [static let footnote: NSFont.TextStyle](nsfont/textstyle/footnote.md)
  The font you use in footnotes.
- [static let headline: NSFont.TextStyle](nsfont/textstyle/headline.md)
  The font you use for headings.
- [static let subheadline: NSFont.TextStyle](nsfont/textstyle/subheadline.md)
  The font you use for subheadings.
- [static let largeTitle: NSFont.TextStyle](nsfont/textstyle/largetitle.md)
  The font you use for large titles.
- [static let title1: NSFont.TextStyle](nsfont/textstyle/title1.md)
  The font you use for first-level hierarchical headings.
- [static let title2: NSFont.TextStyle](nsfont/textstyle/title2.md)
  The font you use for second-level hierarchical headings.
- [static let title3: NSFont.TextStyle](nsfont/textstyle/title3.md)
  The font you use for third-level hierarchical headings.
### Initializers
- [init(rawValue: String)](nsfont/textstyle/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
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
- [NSFont.Weight](nsfont/weight.md)
  System-defined font-weight values.
- [NSFont.TextStyleOptionKey](nsfont/textstyleoptionkey.md)
  The options that you apply when requesting the font or font descriptor of a preferred text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/textstyle)*