# CGRectIntersection(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the intersection of two rectangles.

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
func CGRectIntersection(_ r1: CGRect, _ r2: CGRect) -> CGRect
```

```c
extern CGRect CGRectIntersection(CGRect r1, CGRect r2);
```

## Return Value

A rectangle that represents the intersection of the two specified rectangles. If the two rectangles do not intersect, returns the null rectangle. To check for this condition, use [`CGRectIsNull(_:)`](./cgrectisnull%28_%29.md).

## Discussion

Both rectangles are standardized prior to calculating the intersection.

## Parameters

- `r1`: The first source rectangle.
- `r2`: The second source rectangle.

## See Also

### Modifying Rectangles
- [func CGRectInset(CGRect, CGFloat, CGFloat) -> CGRect](./cgrectinset%28_,_,_%29.md)
  Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
- [func CGRectIntegral(CGRect) -> CGRect](./cgrectintegral%28_%29.md)
  Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [func CGRectOffset(CGRect, CGFloat, CGFloat) -> CGRect](./cgrectoffset%28_,_,_%29.md)
  Returns a rectangle with an origin that is offset from that of the source rectangle.
- [func CGRectStandardize(CGRect) -> CGRect](./cgrectstandardize%28_%29.md)
  Returns a rectangle with a positive width and height.
- [func CGRectUnion(CGRect, CGRect) -> CGRect](./cgrectunion%28_,_%29.md)
  Returns the smallest rectangle that contains the two source rectangles.
- [CGRectDivide](./cgrectdivide.md)
  Divides a source rectangle into two component rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectintersection(_:_:))*