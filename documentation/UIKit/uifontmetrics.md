# UIFontMetrics

**Framework**: UIKit  
**Kind**: class

A utility object for obtaining custom fonts that scale to support Dynamic Type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class UIFontMetrics
```

## Mentions

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)

#### Overview

Use a [`UIFontMetrics`](uifontmetrics.md) object to support scalable custom fonts in your app. You create a font metrics object that specifies the font style—for example, body or title—that you want to use in your app. You then pass your custom font to the [`scaledFont(for:)`](uifontmetrics/scaledfont(for:).md) method (or one of the other methods of this class) to obtain a font object that is based on your custom font, has the appropriate style information, and automatically scales to match the current Dynamic Type settings.

## Topics

### Creating a Font Metrics Object
- [init(forTextStyle: UIFont.TextStyle)](uifontmetrics/init(fortextstyle:).md)
  Creates a font metrics object for the specified text style.
- [class var `default`: UIFontMetrics](uifontmetrics/default.md)
  The default font metrics object for content.
- [UIFont.TextStyle](uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.
### Creating Scaled Fonts
- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [func scaledFont(for: UIFont) -> UIFont](uifontmetrics/scaledfont(for:).md)
  Returns a version of the specified font that adopts the current font metrics.
- [func scaledFont(for: UIFont, compatibleWith: UITraitCollection?) -> UIFont](uifontmetrics/scaledfont(for:compatiblewith:).md)
  Returns a version of the specified font that adopts the current font metrics and supports the specified traits.
- [func scaledFont(for: UIFont, maximumPointSize: CGFloat) -> UIFont](uifontmetrics/scaledfont(for:maximumpointsize:).md)
  Returns a version of the specified font that adopts the current font metrics and is constrained to the specified maximum size.
- [func scaledFont(for: UIFont, maximumPointSize: CGFloat, compatibleWith: UITraitCollection?) -> UIFont](uifontmetrics/scaledfont(for:maximumpointsize:compatiblewith:).md)
  Returns a version of the specified font that adopts the current font metrics and is constrained to the specified traits and size.
### Scaling Layout Values
- [func scaledValue(for: CGFloat) -> CGFloat](uifontmetrics/scaledvalue(for:).md)
  Scales an arbitrary layout value based on the current Dynamic Type settings.
- [func scaledValue(for: CGFloat, compatibleWith: UITraitCollection?) -> CGFloat](uifontmetrics/scaledvalue(for:compatiblewith:).md)
  Scales an arbitrary layout value based on the current Dynamic Type settings and the specified traits.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Adding a Custom Font to Your App](adding-a-custom-font-to-your-app.md)
  Add a custom font to your app and use it in your app’s interface.
- [class UIFont](uifont.md)
  An object that provides access to the font’s characteristics.
- [class UIFontDescriptor](uifontdescriptor.md)
  A collection of attributes that describes a font.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontmetrics)*