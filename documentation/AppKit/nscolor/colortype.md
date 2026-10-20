# NSColor.ColorType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the color’s type, and which methods may be called on the color object.

**Availability**:
- macOS

## Declaration

```swift
enum ColorType
```

```c
enum NSColorType : NSInteger;
```

## Topics

### Color Types
- [NSColor.ColorType.componentBased](./colortype/componentbased.md)
  Colors that include floating-point color components and a color space.
- [NSColor.ColorType.pattern](./colortype/pattern.md)
  Colors that include an image to be used as a pattern.
- [NSColor.ColorType.catalog](./colortype/catalog.md)
  Colors that are retrieved from an asset catalog.
### Initializers
- [init?(rawValue: Int)](./colortype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with the color space
- [var type: NSColor.ColorType](./type.md)
  The type of the color object.
- [func usingType(NSColor.ColorType) -> NSColor?](./usingtype%28_%29.md)
  Returns a version of the color object that is compatible with the specified color type.
- [var colorSpace: NSColorSpace](./colorspace.md)
  The color space associated with the color.
- [struct NSColorSpaceName](../nscolorspacename.md)
  Constants that specify color space names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/colortype)*