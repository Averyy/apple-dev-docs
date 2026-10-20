# NSInsetRect(_:_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Insets a rectangle by a specified amount.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSInsetRect(_ aRect: NSRect, _ dX: Double, _ dY: Double) -> NSRect
```

```c
extern NSRect NSInsetRect(NSRect aRect, CGFloat dX, CGFloat dY);
```

#### Return Value

A copy of `aRect`, altered by moving the two sides that are parallel to the y axis inward by `dX`, and the two sides parallel to the x axis inwards by `dY`.

## See Also

### Managing Rectangles
- [func NSContainsRect(NSRect, NSRect) -> Bool](./nscontainsrect%28_,_%29.md)
  Returns a Boolean value that indicates whether one rectangle completely encloses another.
- [func NSDivideRect(NSRect, UnsafeMutablePointer<NSRect>, UnsafeMutablePointer<NSRect>, Double, NSRectEdge)](./nsdividerect%28_,_,_,_,_%29.md)
  Divides a rectangle into two new rectangles.
- [func NSEqualRects(NSRect, NSRect) -> Bool](./nsequalrects%28_,_%29.md)
  Returns a Boolean value that indicates whether the two rectangles are equal.
- [func NSIsEmptyRect(NSRect) -> Bool](./nsisemptyrect%28_%29.md)
  Returns a Boolean value that indicates whether a given rectangle is empty.
- [func NSHeight(NSRect) -> Double](./nsheight%28_%29.md)
  Returns the height of a given rectangle.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinsetrect(_:_:_:))*