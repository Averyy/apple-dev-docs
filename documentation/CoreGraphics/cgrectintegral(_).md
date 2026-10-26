# CGRectIntegral(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the smallest rectangle that results from converting the source rectangle values to integers.

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
func CGRectIntegral(_ rect: CGRect) -> CGRect
```

```c
extern CGRect CGRectIntegral(CGRect rect);
```

#### Return Value

A rectangle with the smallest integer values for its origin and size that contains the source rectangle. That is, given a rectangle with fractional origin or size values, `CGRectIntegral` rounds the rectangle’s origin downward and its size upward to the nearest whole integers, such that the result contains the original rectangle. Returns a null rectangle if `rect` is a null rectangle.

## Parameters

- `rect`: The source rectangle.

## See Also

### Modifying Rectangles
- [func CGRectInset(CGRect, CGFloat, CGFloat) -> CGRect](./cgrectinset%28_,_,_%29.md)
  Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectintegral(_:))*