# NSColor.ColorType

**Framework**: AppKit  
**Kind**: enum

Constants that indicate the color’s type, and which methods may be called on the color object.

**Availability**:
- macOS ?+

## Declaration

```swift
enum ColorType
```

## Topics

### Color Types
- [NSColor.ColorType.componentBased](nscolor/colortype/componentbased.md)
  Colors that include floating-point color components and a color space.
- [NSColor.ColorType.pattern](nscolor/colortype/pattern.md)
  Colors that include an image to be used as a pattern.
- [NSColor.ColorType.catalog](nscolor/colortype/catalog.md)
  Colors that are retrieved from an asset catalog.
### Initializers
- [init?(rawValue: Int)](nscolor/colortype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var type: NSColor.ColorType](nscolor/type.md)
  The type of the color object.
- [func usingType(NSColor.ColorType) -> NSColor?](nscolor/usingtype(_:).md)
  Returns a version of the color object that is compatible with the specified color type.
- [var colorSpace: NSColorSpace](nscolor/colorspace.md)
  The color space associated with the color.
- [struct NSColorSpaceName](nscolorspacename.md)
  Constants that specify color space names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/colortype)*