# NSPointInRect(_:_:)

**Framework**: Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a given point is in a given rectangle.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSPointInRect(_ aPoint: NSPoint, _ aRect: NSRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `aPoint` is located within the rectangle represented by `aRect`, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Point-in-rectangle functions generally assume that the “upper” and “left” edges of a rectangle are inside  the rectangle boundaries, while the “lower” and “right” edges are outside the boundaries. This method treats the “upper” and “left” edges of the rectangle as the ones containing the origin of the rectangle.

##### Special Considerations

The meanings of “upper” and “lower” (and “left” and “right”) are relative to the current coordinate system and the location of the rectangle. For a rectangle of positive height located in positive x and y coordinates:

- In the default macOS desktop coordinate system—where the origin is at the bottom left—the rectangle edge closest to the bottom of the screen is the “upper” edge (and is considered inside the rectangle).
- On iOS and in a flipped coordinate system in macOS desktop—where the origin is at the top left—the rectangle edge closest to the bottom of the screen is the “lower” edge (and is considered outside the rectangle).

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointinrect(_:_:))*