# CGRectEqualToRect(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns whether two rectangles are equal in size and position.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: The [`CGRect`](../CoreFoundation/cgrect.md) type adopts the `Equatable` protocol; use the `==` operator instead.

## Declaration

```swift
func CGRectEqualToRect(_ rect1: CGRect, _ rect2: CGRect) -> Bool
```

```c
extern bool CGRectEqualToRect(CGRect rect1, CGRect rect2);
```

#### Return Value

[`true`](../Swift/true.md) if the two specified rectangles have equal size and origin values, or if both rectangles are null rectangles. Otherwise, [`false`](../Swift/false.md).

## Parameters

- `rect1`: The first rectangle to examine.
- `rect2`: The second rectangle to examine.

## See Also

### Comparing Values
- [func CGRectIntersectsRect(CGRect, CGRect) -> Bool](./cgrectintersectsrect%28_,_%29.md)
  Returns whether two rectangles intersect.
- [CGPointEqualToPoint](./cgpointequaltopoint-c.macro.md)
  Returns whether two points are equal.
- [CGSizeEqualToSize](./cgsizeequaltosize-c.macro.md)
  Returns whether two sizes are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectequaltorect(_:_:))*