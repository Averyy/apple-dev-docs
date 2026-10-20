# NSFont.Weight

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

System-defined font-weight values.

**Availability**:
- macOS

## Declaration

```swift
struct Weight
```

```c
typedef CGFloat NSFontWeight;
```

## Topics

### Font Weights
- [static let ultraLight: NSFont.Weight](./weight/ultralight.md)
  The font weight for system ultra light font.
- [static let thin: NSFont.Weight](./weight/thin.md)
  The font weight for system thin font.
- [static let light: NSFont.Weight](./weight/light.md)
  The font weight for system light font.
- [static let regular: NSFont.Weight](./weight/regular.md)
  The font weight for system regular font.
- [static let medium: NSFont.Weight](./weight/medium.md)
  The font weight for system medium font.
- [static let semibold: NSFont.Weight](./weight/semibold.md)
  The font weight for system semibold font.
- [static let bold: NSFont.Weight](./weight/bold.md)
  The font weight for system bold font.
- [static let heavy: NSFont.Weight](./weight/heavy.md)
  The font weight for system heavy font.
- [static let black: NSFont.Weight](./weight/black.md)
  The font weight for system black font.
### Initializers
- [init(CGFloat)](./weight/init%28_%29.md)
- [init(rawValue: CGFloat)](./weight/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
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
- [NSFont.TextStyle](./textstyle.md)
  Constants that specify the preferred text styles you use with fonts.
- [NSFont.TextStyleOptionKey](./textstyleoptionkey.md)
  The options that you apply when requesting the font or font descriptor of a preferred text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/weight)*