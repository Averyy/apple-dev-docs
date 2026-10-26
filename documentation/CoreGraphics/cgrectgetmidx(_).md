# CGRectGetMidX(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the x- coordinate that establishes the center of a rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGRectGetMidX(_ rect: CGRect) -> CGFloat
```

```c
extern CGFloat CGRectGetMidX(CGRect rect);
```

#### Return Value

The x-coordinate of the center of the specified rectangle.

## Parameters

- `rect`: The rectangle to examine.

## See Also

### Getting Min, Mid, and Max Values
- [func CGRectGetMinX(CGRect) -> CGFloat](./cgrectgetminx%28_%29.md)
  Returns the smallest value for the x-coordinate of the rectangle.
- [func CGRectGetMinY(CGRect) -> CGFloat](./cgrectgetminy%28_%29.md)
  Returns the smallest value for the y-coordinate of the rectangle.
- [func CGRectGetMidY(CGRect) -> CGFloat](./cgrectgetmidy%28_%29.md)
  Returns the y-coordinate that establishes the center of the rectangle.
- [func CGRectGetMaxX(CGRect) -> CGFloat](./cgrectgetmaxx%28_%29.md)
  Returns the largest value of the x-coordinate for the rectangle.
- [func CGRectGetMaxY(CGRect) -> CGFloat](./cgrectgetmaxy%28_%29.md)
  Returns the largest value for the y-coordinate of the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectgetmidx(_:))*