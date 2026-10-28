# usingType(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a version of the color object that is compatible with the specified color type.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func usingType(_ type: NSColor.ColorType) -> NSColor?
```

```objc
- (NSColor *) colorUsingType:(NSColorType) type;
```

## Return Value

A compatible color object, or `nil` if a compatible color object is not available.

## Discussion

Before accessing the details of an [`NSColor`](../nscolor.md) object, use this method to ensure that you have an object capable of returning those details. For example, before you access the component values, make sure you have a color object of type [`NSColor.ColorType.componentBased`](./colortype/componentbased.md). For some types of colors, conversions to a compatible color type may be possible.

## Parameters

- `type`: The type of color object that you want. For example, if you want a color object containing RGB components, specify [`NSColor.ColorType.componentBased`](./colortype/componentbased.md).

## See Also

### Working with the color space
- [var type: NSColor.ColorType](./type.md)
  The type of the color object.
- [NSColor.ColorType](./colortype.md)
  Constants that indicate the color’s type, and which methods may be called on the color object.
- [var colorSpace: NSColorSpace](./colorspace.md)
  The color space associated with the color.
- [struct NSColorSpaceName](../nscolorspacename.md)
  Constants that specify color space names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/usingtype(_:))*