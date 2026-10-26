# CGRectOffset(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns a rectangle with an origin that is offset from that of the source rectangle.

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
func CGRectOffset(_ rect: CGRect, _ dx: CGFloat, _ dy: CGFloat) -> CGRect
```

```c
extern CGRect CGRectOffset(CGRect rect, CGFloat dx, CGFloat dy);
```

#### Return Value

A rectangle that is the same size as the source, but with its origin offset by `dx` units along the x-axis and `dy` units along the y-axis with respect to the source. Returns a null rectangle if `rect` is a null rectangle.

## Parameters

- `rect`: The source rectangle.
- `dx`: The offset value for the x-coordinate.
- `dy`: The offset value for the  y-coordinate.

## See Also

### Modifying Rectangles
- [func CGRectInset(CGRect, CGFloat, CGFloat) -> CGRect](./cgrectinset%28_,_,_%29.md)
  Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
- [func CGRectIntegral(CGRect) -> CGRect](./cgrectintegral%28_%29.md)
  Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [func CGRectIntersection(CGRect, CGRect) -> CGRect](./cgrectintersection%28_,_%29.md)
  Returns the intersection of two rectangles.
- [func CGRectStandardize(CGRect) -> CGRect](./cgrectstandardize%28_%29.md)
  Returns a rectangle with a positive width and height.
- [func CGRectUnion(CGRect, CGRect) -> CGRect](./cgrectunion%28_,_%29.md)
  Returns the smallest rectangle that contains the two source rectangles.
- [CGRectDivide](./cgrectdivide.md)
  Divides a source rectangle into two component rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectoffset(_:_:_:))*