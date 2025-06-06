# UIFont

**Framework**: UIKit  
**Kind**: class

An object that provides access to the font’s characteristics.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class UIFont
```

## Mentions

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
- [Adding a Custom Font to Your App](adding-a-custom-font-to-your-app.md)

#### Overview

Use `UIFont` to access your font’s characteristics within your app. It also provides the system with access to the glyph information, used during layout. Font objects are immutable, so it’s safe to use them from multiple threads in your app.

In Objective-C, don’t create font objects using the `alloc` and `init` methods. Instead, use class methods of [`UIFont`](uifont.md), such as [`preferredFont(forTextStyle:)`](uifont/preferredfont(fortextstyle:).md), to look up and retrieve the desired font object. These methods check for an existing font object with the specified characteristics and return it if it exists. Otherwise, they create a new font object based on the desired font characteristics.

## Topics

### Creating Fonts
- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [class func preferredFont(forTextStyle: UIFont.TextStyle) -> UIFont](uifont/preferredfont(fortextstyle:).md)
  Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [class func preferredFont(forTextStyle: UIFont.TextStyle, compatibleWith: UITraitCollection?) -> UIFont](uifont/preferredfont(fortextstyle:compatiblewith:).md)
  Returns an instance of the system font for the appropriate text style and traits.
- [UIFont.TextStyle](uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.
- [init?(name: String, size: CGFloat)](uifont/init(name:size:).md)
  Creates and returns a font object for the specified font name and size.
- [init(descriptor: UIFontDescriptor, size: CGFloat)](uifont/init(descriptor:size:).md)
  Returns a font that matches the specified font descriptor.
- [func withSize(CGFloat) -> UIFont](uifont/withsize(_:).md)
  Returns a font object that is the same as the font, but has the specified size.
### Creating System Fonts
- [class func systemFont(ofSize: CGFloat) -> UIFont](uifont/systemfont(ofsize:).md)
  Returns the font object for standard interface items in the specified size.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/systemfont(ofsize:weight:).md)
  Returns the font object for standard interface items in the specified size and weight.
- [UIFont.Weight](uifont/weight.md)
  Constants that represent standard typeface styles.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight, width: UIFont.Width) -> UIFont](uifont/systemfont(ofsize:weight:width:).md)
- [UIFont.Width](uifont/width.md)
- [class func boldSystemFont(ofSize: CGFloat) -> UIFont](uifont/boldsystemfont(ofsize:).md)
  Returns the font object for standard interface items in boldface type in the specified size.
- [class func italicSystemFont(ofSize: CGFloat) -> UIFont](uifont/italicsystemfont(ofsize:).md)
  Returns the font object for standard interface items in italic type in the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/monospacedsystemfont(ofsize:weight:).md)
  Returns the fixed-width font for standard interface text in the specified size.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/monospaceddigitsystemfont(ofsize:weight:).md)
  Returns the standard system font with all digits of consistent width.
### Getting the Available Font Names
- [class var familyNames: [String]](uifont/familynames.md)
  Returns an array of font family names available on the system.
- [class func fontNames(forFamilyName: String) -> [String]](uifont/fontnames(forfamilyname:).md)
  Returns an array of font names available in a particular font family.
### Getting Font Name Attributes
- [var familyName: String](uifont/familyname.md)
  The font family name.
- [var fontName: String](uifont/fontname.md)
  The font face name.
### Getting Font Metrics
- [var pointSize: CGFloat](uifont/pointsize.md)
  The font’s point size, or the effective vertical point size for a font with a nonstandard matrix.
- [var ascender: CGFloat](uifont/ascender.md)
  The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [var descender: CGFloat](uifont/descender.md)
  The bottom y-coordinate, offset from the baseline, of the font’s longest descender.
- [var leading: CGFloat](uifont/leading.md)
  The font’s leading information.
- [var capHeight: CGFloat](uifont/capheight.md)
  The font’s cap height information.
- [var xHeight: CGFloat](uifont/xheight.md)
  The x-height of the font.
- [var lineHeight: CGFloat](uifont/lineheight.md)
  The height, in points, of text lines.
### Getting System Font Information
- [class var labelFontSize: CGFloat](uifont/labelfontsize.md)
  The standard font size, in points, for labels.
- [class var buttonFontSize: CGFloat](uifont/buttonfontsize.md)
  The standard font size, in points, for buttons.
- [class var smallSystemFontSize: CGFloat](uifont/smallsystemfontsize.md)
  The size, in points, of the standard small system font.
- [class var systemFontSize: CGFloat](uifont/systemfontsize.md)
  The size, in points, of the standard system font.
### Getting Font Descriptors
- [var fontDescriptor: UIFontDescriptor](uifont/fontdescriptor.md)
  A font descriptor for the font.
- [class UIFontDescriptor](uifontdescriptor.md)
  A collection of attributes that describes a font.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Adding a Custom Font to Your App](adding-a-custom-font-to-your-app.md)
  Add a custom font to your app and use it in your app’s interface.
- [class UIFontDescriptor](uifontdescriptor.md)
  A collection of attributes that describes a font.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [class UIFontMetrics](uifontmetrics.md)
  A utility object for obtaining custom fonts that scale to support Dynamic Type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont)*