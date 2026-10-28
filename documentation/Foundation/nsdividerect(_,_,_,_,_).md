# NSDivideRect(_:_:_:_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Divides a rectangle into two new rectangles.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSDivideRect(_ inRect: NSRect, _ slice: UnsafeMutablePointer<NSRect>, _ rem: UnsafeMutablePointer<NSRect>, _ amount: Double, _ edge: NSRectEdge)
```

```c
extern void NSDivideRect(NSRect inRect, NSRect *slice, NSRect *rem, CGFloat amount, NSRectEdge edge);
```

## Discussion

Creates two rectangles—`slice` and `rem`—from `inRect`, by dividing `inRect` with a line that’s parallel to the side of `inRect` specified by `edge`. The size of `slice` is determined by `amount`, which specifies the distance from `edge`.

`slice` and `rem` must not be `NULL`.

For more information, see [`NSRectEdge`](./nsrectedge.md).

## See Also

### Managing Rectangles
- [func NSContainsRect(NSRect, NSRect) -> Bool](./nscontainsrect%28_,_%29.md)
  Returns a Boolean value that indicates whether one rectangle completely encloses another.
- [func NSEqualRects(NSRect, NSRect) -> Bool](./nsequalrects%28_,_%29.md)
  Returns a Boolean value that indicates whether the two rectangles are equal.
- [func NSIsEmptyRect(NSRect) -> Bool](./nsisemptyrect%28_%29.md)
  Returns a Boolean value that indicates whether a given rectangle is empty.
- [func NSHeight(NSRect) -> Double](./nsheight%28_%29.md)
  Returns the height of a given rectangle.
- [func NSInsetRect(NSRect, Double, Double) -> NSRect](./nsinsetrect%28_,_,_%29.md)
  Insets a rectangle by a specified amount.
- [func NSIntegralRect(NSRect) -> NSRect](./nsintegralrect%28_%29.md)
  Adjusts the sides of a rectangle to integer values.
- [func NSIntegralRectWithOptions(NSRect, AlignmentOptions) -> NSRect](./nsintegralrectwithoptions%28_,_%29.md)
  Adjusts the sides of a rectangle to integral values using the specified options.
- [func NSIntersectionRect(NSRect, NSRect) -> NSRect](./nsintersectionrect%28_,_%29.md)
  Calculates the intersection of two rectangles.
- [func NSIntersectsRect(NSRect, NSRect) -> Bool](./nsintersectsrect%28_,_%29.md)
  Returns a Boolean value that indicates whether two rectangles intersect.
- [func NSMakeRect(Double, Double, Double, Double) -> NSRect](./nsmakerect%28_,_,_,_%29.md)
  Creates a new `NSRect` from the specified values.
- [func NSMaxX(NSRect) -> Double](./nsmaxx%28_%29.md)
  Returns the largest x coordinate of a given rectangle.
- [func NSMaxY(NSRect) -> Double](./nsmaxy%28_%29.md)
  Returns the largest y coordinate of a given rectangle.
- [func NSMidX(NSRect) -> Double](./nsmidx%28_%29.md)
  Returns the x coordinate of a given rectangle’s midpoint.
- [func NSMidY(NSRect) -> Double](./nsmidy%28_%29.md)
  Returns the y coordinate of a given rectangle’s midpoint.
- [func NSMinX(NSRect) -> Double](./nsminx%28_%29.md)
  Returns the smallest x coordinate of a given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdividerect(_:_:_:_:_:))*