# CGRectIntersectsRect(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns whether two rectangles intersect.

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
func CGRectIntersectsRect(_ rect1: CGRect, _ rect2: CGRect) -> Bool
```

```c
extern bool CGRectIntersectsRect(CGRect rect1, CGRect rect2);
```

#### Return Value

[`true`](../Swift/true.md) if the two specified rectangles intersect; otherwise, [`false`](../Swift/false.md). The first rectangle intersects the second if the intersection of the rectangles is not equal to the null rectangle.

## Parameters

- `rect1`: The first rectangle to examine.
- `rect2`: The second rectangle to examine.

## See Also

### Comparing Values
- [func CGRectEqualToRect(CGRect, CGRect) -> Bool](./cgrectequaltorect%28_,_%29.md)
  Returns whether two rectangles are equal in size and position.
- [CGPointEqualToPoint](./cgpointequaltopoint-c.macro.md)
  Returns whether two points are equal.
- [CGSizeEqualToSize](./cgsizeequaltosize-c.macro.md)
  Returns whether two sizes are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectintersectsrect(_:_:))*