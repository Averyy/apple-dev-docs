# NSMouseInRect(_:_:_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the point is in the specified rectangle.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSMouseInRect(_ aPoint: NSPoint, _ aRect: NSRect, _ flipped: Bool) -> Bool
```

```c
extern BOOL NSMouseInRect(NSPoint aPoint, NSRect aRect, BOOL flipped);
```

## Return Value

[`true`](../Swift/true.md) if the hot spot of the cursor lies inside a given rectangle, otherwise [`false`](../Swift/false.md).

## Discussion

This method assumes an unscaled and unrotated coordinate system. Specify [`true`](../Swift/true.md) for `flipped` if the underlying view uses a flipped coordinate system.

Point-in-rectangle functions generally assume that the bottom edge of a rectangle is outside of the rectangle boundaries, while the upper edge is inside the boundaries. This method views `aRect` from the point of view of the user—that is, this method always treats the bottom edge of the rectangle as the one closest to the bottom edge of the user’s screen. By making this adjustment, this function ensures consistent mouse-detection behavior from the user’s perspective.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmouseinrect(_:_:_:))*