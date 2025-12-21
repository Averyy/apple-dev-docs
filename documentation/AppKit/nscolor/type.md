# type

**Framework**: AppKit  
**Kind**: property

The type of the color object.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var type: NSColor.ColorType { get }
```

#### Discussion

A color object’s type determines which of its methods and properties you may access. For example, if the type is [`NSColor.ColorType.pattern`](nscolor/colortype/pattern.md), you may safely access the [`patternImage`](nscolor/patternimage.md) property.

## See Also

- [func usingType(NSColor.ColorType) -> NSColor?](nscolor/usingtype(_:).md)
  Returns a version of the color object that is compatible with the specified color type.
- [NSColor.ColorType](nscolor/colortype.md)
  Constants that indicate the color’s type, and which methods may be called on the color object.
- [var colorSpace: NSColorSpace](nscolor/colorspace.md)
  The color space associated with the color.
- [struct NSColorSpaceName](nscolorspacename.md)
  Constants that specify color space names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/type)*