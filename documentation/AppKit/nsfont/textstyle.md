# NSFont.TextStyle

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the preferred text styles you use with fonts.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct TextStyle
```

```c
typedef NSString * NSFontTextStyle;
```

## Discussion

Pass these constants to [`preferredFont(forTextStyle:options:)`](./preferredfont%28fortextstyle,options%29.md) or [`preferredFontDescriptor(forTextStyle:options:)`](../nsfontdescriptor/preferredfontdescriptor%28fortextstyle,options%29.md) to retrieve the corresponding font or font descriptor.

## Topics

### Constants
- [static let body: NSFont.TextStyle](./textstyle/body.md)
  The font you use for body text.
- [static let callout: NSFont.TextStyle](./textstyle/callout.md)
  The font you use for callouts.
- [static let caption1: NSFont.TextStyle](./textstyle/caption1.md)
  The font you use for standard captions.
- [static let caption2: NSFont.TextStyle](./textstyle/caption2.md)
  The font you use for alternate captions.
- [static let footnote: NSFont.TextStyle](./textstyle/footnote.md)
  The font you use in footnotes.
- [static let headline: NSFont.TextStyle](./textstyle/headline.md)
  The font you use for headings.
- [static let subheadline: NSFont.TextStyle](./textstyle/subheadline.md)
  The font you use for subheadings.
- [static let largeTitle: NSFont.TextStyle](./textstyle/largetitle.md)
  The font you use for large titles.
- [static let title1: NSFont.TextStyle](./textstyle/title1.md)
  The font you use for first-level hierarchical headings.
- [static let title2: NSFont.TextStyle](./textstyle/title2.md)
  The font you use for second-level hierarchical headings.
- [static let title3: NSFont.TextStyle](./textstyle/title3.md)
  The font you use for third-level hierarchical headings.
### Initializers
- [init(rawValue: String)](./textstyle/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating System Fonts
- [class func preferredFont(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFont](./preferredfont%28fortextstyle,options%29.md)
  Returns the font associated with the text style.
- [class func systemFont(ofSize: CGFloat) -> NSFont](./systemfont%28ofsize%29.md)
  Returns the standard system font with the specified size.
- [class func systemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](./systemfont%28ofsize,weight%29.md)
  Returns the standard system font with the specified size and weight.
- [class func boldSystemFont(ofSize: CGFloat) -> NSFont](./boldsystemfont%28ofsize%29.md)
  Returns the standard system font in boldface type with the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](./monospacedsystemfont%28ofsize,weight%29.md)
  Returns a monospace version of the system font with the specified size and weight.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: NSFont.Weight) -> NSFont](./monospaceddigitsystemfont%28ofsize,weight%29.md)
  Returns a version of the standard system font that contains monospaced digit glyphs.
- [class var systemFontSize: CGFloat](./systemfontsize.md)
  Returns the size of the standard system font.
- [class var smallSystemFontSize: CGFloat](./smallsystemfontsize.md)
  Returns the size of the standard small system font.
- [NSFont.Weight](./weight.md)
  System-defined font-weight values.
- [NSFont.TextStyleOptionKey](./textstyleoptionkey.md)
  The options that you apply when requesting the font or font descriptor of a preferred text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/textstyle)*