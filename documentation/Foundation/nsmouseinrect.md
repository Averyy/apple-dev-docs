# NSMouseInRect(_:_:_:)

**Framework**: Foundation  
**Kind**: func

Returns a Boolean value that indicates whether the point is in the specified rectangle.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSMouseInRect(_ aPoint: NSPoint, _ aRect: NSRect, _ flipped: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the hot spot of the cursor lies inside a given rectangle, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method assumes an unscaled and unrotated coordinate system. Specify [`true`](https://developer.apple.com/documentation/swift/true) for `flipped` if the underlying view uses a flipped coordinate system.

Point-in-rectangle functions generally assume that the bottom edge of a rectangle is outside of the rectangle boundaries, while the upper edge is inside the boundaries. This method views `aRect` from the point of view of the user—that is, this method always treats the bottom edge of the rectangle as the one closest to the bottom edge of the user’s screen. By making this adjustment, this function ensures consistent mouse-detection behavior from the user’s perspective.

## See Also

- [func NSContainsRect(NSRect, NSRect) -> Bool](nscontainsrect(_:_:).md)
  Returns a Boolean value that indicates whether one rectangle completely encloses another.
- [func NSDivideRect(NSRect, UnsafeMutablePointer<NSRect>, UnsafeMutablePointer<NSRect>, Double, NSRectEdge)](nsdividerect(_:_:_:_:_:).md)
  Divides a rectangle into two new rectangles.
- [func NSEqualRects(NSRect, NSRect) -> Bool](nsequalrects(_:_:).md)
  Returns a Boolean value that indicates whether the two rectangles are equal.
- [func NSIsEmptyRect(NSRect) -> Bool](nsisemptyrect(_:).md)
  Returns a Boolean value that indicates whether a given rectangle is empty.
- [func NSHeight(NSRect) -> Double](nsheight(_:).md)
  Returns the height of a given rectangle.
- [func NSInsetRect(NSRect, Double, Double) -> NSRect](nsinsetrect(_:_:_:).md)
  Insets a rectangle by a specified amount.
- [func NSIntegralRect(NSRect) -> NSRect](nsintegralrect(_:).md)
  Adjusts the sides of a rectangle to integer values.
- [func NSIntegralRectWithOptions(NSRect, AlignmentOptions) -> NSRect](nsintegralrectwithoptions(_:_:).md)
  Adjusts the sides of a rectangle to integral values using the specified options.
- [func NSIntersectionRect(NSRect, NSRect) -> NSRect](nsintersectionrect(_:_:).md)
  Calculates the intersection of two rectangles.
- [func NSIntersectsRect(NSRect, NSRect) -> Bool](nsintersectsrect(_:_:).md)
  Returns a Boolean value that indicates whether two rectangles intersect.
- [func NSMakeRect(Double, Double, Double, Double) -> NSRect](nsmakerect(_:_:_:_:).md)
  Creates a new `NSRect` from the specified values.
- [func NSMaxX(NSRect) -> Double](nsmaxx(_:).md)
  Returns the largest x coordinate of a given rectangle.
- [func NSMaxY(NSRect) -> Double](nsmaxy(_:).md)
  Returns the largest y coordinate of a given rectangle.
- [func NSMidX(NSRect) -> Double](nsmidx(_:).md)
  Returns the x coordinate of a given rectangle’s midpoint.
- [func NSMidY(NSRect) -> Double](nsmidy(_:).md)
  Returns the y coordinate of a given rectangle’s midpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmouseinrect(_:_:_:))*