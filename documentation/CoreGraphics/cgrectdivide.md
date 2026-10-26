# CGRectDivide

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Divides a source rectangle into two component rectangles.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void CGRectDivide(CGRect rect, CGRect *slice, CGRect *remainder, CGFloat amount, CGRectEdge edge);
```

#### Discussion

If `rect` is a null rectangle, this function outputs [`CGRectNull`](./cgrectnull.md) for both the `slice` and `remainder` rectangles.

## Parameters

- `rect`: The source rectangle.
- `slice`: On input, a pointer to an uninitialized rectangle. On return, the rectangle is filled in with the specified edge and values that extends the distance beyond the edge specified by the `amount` parameter. Must not be `NULL`.
- `remainder`: On input, a pointer to an uninitialized rectangle. On return, the rectangle contains the portion of the source rectangle that remains after [`CGRectEdge`](../CoreFoundation/cgrectedge.md) produces the “slice” rectangle. Must not be `NULL`.
- `amount`: A distance from the rectangle side that is specified in the `edge` parameter. This distance defines the line, parallel to the specified side, that Core Graphics uses to divide the source rectangle.
- `edge`: An edge value that specifies the side of the rectangle from which the distance passed in the `amount` parameter is measured. [`CGRectDivide`](./cgrectdivide.md) produces a “slice” rectangle that contains the specified edge and extends `amount` distance beyond it.

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
- [func CGRectUnion(CGRect, CGRect) -> CGRect](./cgrectunion%28_,_%29.md)
  Returns the smallest rectangle that contains the two source rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectdivide)*