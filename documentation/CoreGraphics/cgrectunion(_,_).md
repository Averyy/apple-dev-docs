# CGRectUnion(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the smallest rectangle that contains the two source rectangles.

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
func CGRectUnion(_ r1: CGRect, _ r2: CGRect) -> CGRect
```

```c
extern CGRect CGRectUnion(CGRect r1, CGRect r2);
```

## Return Value

The smallest rectangle that completely contains both of the source rectangles.

## Discussion

Both rectangles are standardized prior to calculating the union. If either of the rectangles is a null rectangle, a copy of the other rectangle is returned (resulting in a null rectangle if both rectangles are null). Otherwise a rectangle that completely contains the source rectangles is returned.

## Parameters

- `r1`: The first source rectangle.
- `r2`: The second source rectangle.

## See Also

### Modifying Rectangles
- [func CGRectInset(CGRect, CGFloat, CGFloat) -> CGRect](./cgrectinset%28_,_,_%29.md)
  Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
- [func CGRectIntegral(CGRect) -> CGRect](./cgrectintegral%28_%29.md)
  Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [func CGRectIntersection(CGRect, CGRect) -> CGRect](./cgrectintersection%28_,_%29.md)
  Returns the intersection of two rectangles.
- [func CGRectOffset(CGRect, CGFloat, CGFloat) -> CGRect](./cgrectoffset%28_,_,_%29.md)
  Returns a rectangle with an origin that is offset from that of the source rectangle.
- [func CGRectStandardize(CGRect) -> CGRect](./cgrectstandardize%28_%29.md)
  Returns a rectangle with a positive width and height.
- [CGRectDivide](./cgrectdivide.md)
  Divides a source rectangle into two component rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectunion(_:_:))*