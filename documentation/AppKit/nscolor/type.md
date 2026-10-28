# type

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of the color object.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var type: NSColor.ColorType { get }
```

```objc
@property (readonly) NSColorType type;
```

## Discussion

A color object’s type determines which of its methods and properties you may access. For example, if the type is [`NSColor.ColorType.pattern`](./colortype/pattern.md), you may safely access the [`patternImage`](./patternimage.md) property.

## See Also

### Working with the color space
- [func usingType(NSColor.ColorType) -> NSColor?](./usingtype%28_%29.md)
  Returns a version of the color object that is compatible with the specified color type.
- [NSColor.ColorType](./colortype.md)
  Constants that indicate the color’s type, and which methods may be called on the color object.
- [var colorSpace: NSColorSpace](./colorspace.md)
  The color space associated with the color.
- [struct NSColorSpaceName](../nscolorspacename.md)
  Constants that specify color space names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/type)*