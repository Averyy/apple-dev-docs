# components

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the values of the color components (including alpha) associated with a color.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var components: [CGFloat]? { get }
```

## Discussion

An array of intensity values for the color components (including alpha) associated with the specified color. The size of the array is equal to the color’s [`numberOfComponents`](./numberofcomponents.md) value.

## See Also

### Examining a Color
- [var alpha: CGFloat](./alpha.md)
  Returns the value of the alpha component associated with a color.
- [var colorSpace: CGColorSpace?](./colorspace.md)
  Returns the color space associated with a color.
- [var numberOfComponents: Int](./numberofcomponents.md)
  Returns the number of color components (including alpha) associated with a color.
- [var pattern: CGPattern?](./pattern.md)
  Returns the pattern associated with a color in a pattern color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolor/components)*