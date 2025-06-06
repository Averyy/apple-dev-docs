# CGColor

**Framework**: Core Graphics  
**Kind**: class

A set of components that define a color, with a color space specifying how to interpret them.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CGColor
```

#### Overview

`CGColor` is the fundamental data type used internally by Core Graphics to represent colors. `CGColor` objects, and the functions that operate on them, provide a fast and convenient way of managing and setting colors directly, especially colors that are reused (such as black for text).

A color object contains a set of components (such as red, green, and blue) that uniquely define a color, and a color space that specifies how those components should be interpreted.

Color objects provide a fast and convenient way to manage and set colors, especially colors that are used repeatedly. Drawing operations use color objects for setting fill and stroke colors, managing alpha, and setting color with a pattern.

[`CGColor`](cgcolor.md) is derived from [`CFTypeRef`](https://developer.apple.com/documentation/CoreFoundation/CFTypeRef) and inherits the properties that all Core Foundation types have in common.

## Topics

### Creating Colors
- [func copy() -> CGColor?](cgcolor/copy.md)
  Creates a copy of an existing color.
- [func copy(alpha: CGFloat) -> CGColor?](cgcolor/copy(alpha:).md)
  Creates a copy of an existing color, substituting a new alpha value.
- [init(genericCMYKCyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](cgcolor/init(genericcmykcyan:magenta:yellow:black:alpha:).md)
  Creates a color in the Generic CMYK color space.
- [init(gray: CGFloat, alpha: CGFloat)](cgcolor/init(gray:alpha:).md)
  Creates a color in the Generic gray color space.
- [init(genericGrayGamma2_2Gray: CGFloat, alpha: CGFloat)](cgcolor/init(genericgraygamma2_2gray:alpha:).md)
  Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cgcolor/init(red:green:blue:alpha:).md)
  Creates a color in the Generic RGB color space.
- [init(srgbRed: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](cgcolor/init(srgbred:green:blue:alpha:).md)
  Creates a color in the sRGB color space.
- [init?(colorSpace: CGColorSpace, components: UnsafePointer<CGFloat>)](cgcolor/init(colorspace:components:).md)
  Creates a color using a list of intensity values (including alpha) and an associated color space.
- [init?(patternSpace: CGColorSpace, pattern: CGPattern, components: UnsafePointer<CGFloat>)](cgcolor/init(patternspace:pattern:components:).md)
  Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.
### Getting System Colors
- [class var black: CGColor](cgcolor/black.md)
  The black color in the Generic gray color space.
- [class var white: CGColor](cgcolor/white.md)
  The white color in the Generic gray color space.
- [class var clear: CGColor](cgcolor/clear.md)
  The clear color in the Generic gray color space.
### Examining a Color
- [var alpha: CGFloat](cgcolor/alpha.md)
  Returns the value of the alpha component associated with a color.
- [var colorSpace: CGColorSpace?](cgcolor/colorspace.md)
  Returns the color space associated with a color.
- [var components: [CGFloat]?](cgcolor/components.md)
  Returns the values of the color components (including alpha) associated with a color.
- [var numberOfComponents: Int](cgcolor/numberofcomponents.md)
  Returns the number of color components (including alpha) associated with a color.
- [var pattern: CGPattern?](cgcolor/pattern.md)
  Returns the pattern associated with a color in a pattern color space.
### Converting Between Color Spaces
- [class let conversionTRCSize: CFString](cgcolor/conversiontrcsize.md)
- [func converted(to: CGColorSpace, intent: CGColorRenderingIntent, options: CFDictionary?) -> CGColor?](cgcolor/converted(to:intent:options:).md)
  Creates a new color in a different color space that matches the provided color.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgcolor/typeid.md)
  Returns the Core Foundation type identifier for a color data type.
### Type Properties
- [class let conversionBlackPointCompensation: CFString](cgcolor/conversionblackpointcompensation.md)
  An option for whether to apply black point compensation when converting between color profiles.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [class CGColorConversionInfo](cgcolorconversioninfo.md)
  An object that describes how to convert between color spaces for use by other system services.
- [class CGColorSpace](cgcolorspace.md)
  A profile that specifies how to interpret a color value for display.
- [class CGFont](cgfont.md)
  A set of character glyphs and layout information for drawing text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolor)*