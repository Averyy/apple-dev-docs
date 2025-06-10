# Font

**Framework**: SwiftUI  
**Kind**: struct

An environment-dependent font.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct Font
```

#### Overview

The system resolves a font’s value at the time it uses the font in a given environment because [`Font`](font.md) is a late-binding token.

## Topics

### Getting standard fonts
- [static let extraLargeTitle2: Font](font/extralargetitle2.md)
  Create a font with the second level extra large title text style.
- [static let extraLargeTitle: Font](font/extralargetitle.md)
  Create a font with the extra large title text style.
- [static let largeTitle: Font](font/largetitle.md)
  A font with the large title text style.
- [static let title: Font](font/title.md)
  A font with the title text style.
- [static let title2: Font](font/title2.md)
  Create a font for second level hierarchical headings.
- [static let title3: Font](font/title3.md)
  Create a font for third level hierarchical headings.
- [static let headline: Font](font/headline.md)
  A font with the headline text style.
- [static let subheadline: Font](font/subheadline.md)
  A font with the subheadline text style.
- [static let body: Font](font/body.md)
  A font with the body text style.
- [static let callout: Font](font/callout.md)
  A font with the callout text style.
- [static let caption: Font](font/caption.md)
  A font with the caption text style.
- [static let caption2: Font](font/caption2.md)
  Create a font with the alternate caption text style.
- [static let footnote: Font](font/footnote.md)
  A font with the footnote text style.
### Getting system fonts
- [static func system(Font.TextStyle, design: Font.Design?, weight: Font.Weight?) -> Font](font/system(_:design:weight:).md)
  Gets a system font that uses the specified style, design, and weight.
- [static func system(size: CGFloat, weight: Font.Weight?, design: Font.Design?) -> Font](font/system(size:weight:design:)-697b2.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
- [Font.Design](font/design.md)
  A design to use for fonts.
- [Font.TextStyle](font/textstyle.md)
  A dynamic text style to use for fonts.
- [struct Weight](font/weight.md)
  A weight to use for fonts.
### Creating custom fonts
- [static func custom(String, fixedSize: CGFloat) -> Font](font/custom(_:fixedsize:).md)
  Create a custom font with the given `name` and a fixed `size` that does not scale with Dynamic Type.
- [static func custom(String, size: CGFloat, relativeTo: Font.TextStyle) -> Font](font/custom(_:size:relativeto:).md)
  Create a custom font with the given `name` and `size` that scales relative to the given `textStyle`.
- [static func custom(String, size: CGFloat) -> Font](font/custom(_:size:).md)
  Create a custom font with the given `name` and `size` that scales with the body text style.
### Getting a font from another font
- [init(CTFont)](font/init(_:).md)
  Creates a custom font from a platform font instance.
### Styling a font
- [func bold() -> Font](font/bold.md)
  Adds bold or emphasized styling to the font.
- [func italic() -> Font](font/italic.md)
  Adds italics to the font.
- [func monospaced() -> Font](font/monospaced.md)
  Returns a fixed-width font from the same family as the base font.
- [func monospacedDigit() -> Font](font/monospaceddigit.md)
  Returns a modified font that uses fixed-width digits, while leaving other characters proportionally spaced.
- [func smallCaps() -> Font](font/smallcaps.md)
  Adjusts the font to enable all small capitals.
- [func lowercaseSmallCaps() -> Font](font/lowercasesmallcaps.md)
  Adjusts the font to enable lowercase small capitals.
- [func uppercaseSmallCaps() -> Font](font/uppercasesmallcaps.md)
  Adjusts the font to enable uppercase small capitals.
- [func weight(Font.Weight) -> Font](font/weight(_:).md)
  Sets the weight of the font.
- [func width(Font.Width) -> Font](font/width(_:).md)
  Sets the width of the font.
- [struct Width](font/width.md)
  A width to use for fonts that have multiple widths.
- [func leading(Font.Leading) -> Font](font/leading(_:).md)
  Adjusts the line spacing of a font.
- [Font.Leading](font/leading.md)
  A line spacing adjustment that you can apply to a font.
### Deprecated symbols
- [static func system(Font.TextStyle, design: Font.Design) -> Font](font/system(_:design:).md)
  Gets a system font with the given text style and design.
- [static func system(size: CGFloat, weight: Font.Weight, design: Font.Design) -> Font](font/system(size:weight:design:)-73a88.md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
### Structures
- [struct Context](font/context.md)
  Information used to resolve a font.
- [struct Resolved](font/resolved.md)
  A concrete font value.
### Instance Methods
- [func bold(Bool) -> Font](font/bold(_:).md)
  Adds or removes bold or emphasized styling on the font.
- [func italic(Bool) -> Font](font/italic(_:).md)
  Adds/removes italics on the font.
- [func lowercaseSmallCaps(Bool) -> Font](font/lowercasesmallcaps(_:).md)
  Adjusts the font to enable/disable lowercase small capitals.
- [func monospaced(Bool) -> Font](font/monospaced(_:).md)
  Returns a font adding or removing fixed-width design from the same family as the base font.
- [func pointSize(CGFloat) -> Font](font/pointsize(_:).md)
  Sets the point size of the font explicitly.
- [func resolve(in: Font.Context) -> Font.Resolved](font/resolve(in:).md)
  Evaluates this font to a resolved font given the current context.
- [func scaled(by: CGFloat) -> Font](font/scaled(by:).md)
  Scales the point size of the font.
- [func smallCaps(Bool) -> Font](font/smallcaps(_:).md)
  Adjusts the font to enable/disable all small capitals.
- [func uppercaseSmallCaps(Bool) -> Font](font/uppercasesmallcaps(_:).md)
  Adjusts the font to enable/disable uppercase small capitals.
### Type Properties
- [static var `default`: Font](font/default.md)
  The effective SwiftUI font used in any given environment.
### Type Methods
- [static system(size:weight:design:)](font/system(size:weight:design:).md)
  Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Applying custom fonts to text](applying-custom-fonts-to-text.md)
  Add and use a font in your app that scales with Dynamic Type.
- [func font(Font?) -> some View](view/font(_:).md)
  Sets the default font for text in this view.
- [func fontDesign(Font.Design?) -> some View](view/fontdesign(_:).md)
  Sets the font design of the text in this view.
- [func fontWeight(Font.Weight?) -> some View](view/fontweight(_:).md)
  Sets the font weight of the text in this view.
- [func fontWidth(Font.Width?) -> some View](view/fontwidth(_:).md)
  Sets the font width of the text in this view.
- [var font: Font?](environmentvalues/font.md)
  The default font of this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font)*