# pattern

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the pattern associated with a color in a pattern color space.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var pattern: CGPattern? { get }
```

```c
extern CGPatternRefCGColorGetPattern(CGColorRef color);
```

## See Also

### Examining a Color
- [var alpha: CGFloat](./alpha.md)
  Returns the value of the alpha component associated with a color.
- [var colorSpace: CGColorSpace?](./colorspace.md)
  Returns the color space associated with a color.
- [var components: [CGFloat]?](./components.md)
  Returns the values of the color components (including alpha) associated with a color.
- [var numberOfComponents: Int](./numberofcomponents.md)
  Returns the number of color components (including alpha) associated with a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcolor/pattern)*