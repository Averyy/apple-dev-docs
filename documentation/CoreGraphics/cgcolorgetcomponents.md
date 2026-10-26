# CGColorGetComponents

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the values of the color components (including alpha) associated with a color.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern const CGFloat *CGColorGetComponents(CGColorRef color);
```

#### Return Value

An array of intensity values for the color components (including alpha) associated with the specified color. The size of the array is one more than the number of components of the color space for the color.

## Parameters

- `color`: A color.

## See Also

### Examining a Color
- [CGColorEqualToColor](./cgcolorequaltocolor.md)
  Indicates whether two colors are equal.
- [var alpha: CGFloat](./cgcolor/alpha.md)
  Returns the value of the alpha component associated with a color.
- [var colorSpace: CGColorSpace?](./cgcolor/colorspace.md)
  Returns the color space associated with a color.
- [var numberOfComponents: Int](./cgcolor/numberofcomponents.md)
  Returns the number of color components (including alpha) associated with a color.
- [var pattern: CGPattern?](./cgcolor/pattern.md)
  Returns the pattern associated with a color in a pattern color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolorgetcomponents)*