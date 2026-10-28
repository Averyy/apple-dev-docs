# CGRectInset(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.

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
func CGRectInset(_ rect: CGRect, _ dx: CGFloat, _ dy: CGFloat) -> CGRect
```

```c
extern CGRect CGRectInset(CGRect rect, CGFloat dx, CGFloat dy);
```

## Return Value

A rectangle. The origin value is offset in the x-axis by the distance specified by the `dx` parameter and in the y-axis by the distance specified by the `dy` parameter, and its size adjusted by `(2*dx,2*dy)`, relative to the source rectangle. If `dx` and `dy` are positive values, then the rectangle’s size is decreased. If `dx` and `dy` are negative values, the rectangle’s size is increased.

## Discussion

The rectangle is standardized and then the inset parameters are applied. If the resulting rectangle would have a negative height or width, a null rectangle is returned.

## Parameters

- `rect`: The source [`CGRect`](../CoreFoundation/cgrect.md) structure.
- `dx`: The x-coordinate value to use for adjusting the source rectangle. To create an inset rectangle, specify a positive value. To create a larger, encompassing rectangle, specify a negative value.
- `dy`: The y-coordinate value to use for adjusting the source rectangle. To create an inset rectangle, specify a positive value. To create a larger, encompassing rectangle, specify a negative value.

## See Also

### Modifying Rectangles
- [func CGRectIntegral(CGRect) -> CGRect](./cgrectintegral%28_%29.md)
  Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [func CGRectIntersection(CGRect, CGRect) -> CGRect](./cgrectintersection%28_,_%29.md)
  Returns the intersection of two rectangles.
- [func CGRectOffset(CGRect, CGFloat, CGFloat) -> CGRect](./cgrectoffset%28_,_,_%29.md)
  Returns a rectangle with an origin that is offset from that of the source rectangle.
- [func CGRectStandardize(CGRect) -> CGRect](./cgrectstandardize%28_%29.md)
  Returns a rectangle with a positive width and height.
- [func CGRectUnion(CGRect, CGRect) -> CGRect](./cgrectunion%28_,_%29.md)
  Returns the smallest rectangle that contains the two source rectangles.
- [CGRectDivide](./cgrectdivide.md)
  Divides a source rectangle into two component rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectinset(_:_:_:))*