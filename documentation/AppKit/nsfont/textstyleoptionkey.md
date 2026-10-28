# NSFont.TextStyleOptionKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The options that you apply when requesting the font or font descriptor of a preferred text style.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct TextStyleOptionKey
```

```c
typedef NSString * NSFontTextStyleOptionKey;
```

## Discussion

Pass a dictionary that contains any combination of these keys and their corresponding values to [`preferredFont(forTextStyle:options:)`](./preferredfont%28fortextstyle,options%29.md) or [`preferredFontDescriptor(forTextStyle:options:)`](../nsfontdescriptor/preferredfontdescriptor%28fortextstyle,options%29.md) to further configure the returned font or font descriptor.

## Topics

### Initializers
- [init(rawValue: String)](./textstyleoptionkey/init%28rawvalue%29.md)

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
- [NSFont.TextStyle](./textstyle.md)
  Constants that specify the preferred text styles you use with fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/textstyleoptionkey)*