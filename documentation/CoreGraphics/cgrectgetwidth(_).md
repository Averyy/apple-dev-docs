# CGRectGetWidth(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the width of a rectangle.

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
func CGRectGetWidth(_ rect: CGRect) -> CGFloat
```

```c
extern CGFloat CGRectGetWidth(CGRect rect);
```

#### Return Value

The width of the specified rectangle.

#### Discussion

Regardless of whether the width is stored in the [`CGRect`](../CoreFoundation/cgrect.md) data structure as a positive or negative number, this function returns the width as if the rectangle were standardized.  That is, the result is never a negative number.

## Parameters

- `rect`: The rectangle to examine.

## See Also

### Getting Height and Width
- [func CGRectGetHeight(CGRect) -> CGFloat](./cgrectgetheight%28_%29.md)
  Returns the height of a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectgetwidth(_:))*