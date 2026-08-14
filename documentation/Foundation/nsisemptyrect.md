# NSIsEmptyRect(_:)

**Framework**: Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a given rectangle is empty.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func NSIsEmptyRect(_ aRect: NSRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `aRect` encloses no area at all—that is, if its width or height is 0 or negative, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func NSContainsRect(NSRect, NSRect) -> Bool](nscontainsrect(_:_:).md)
  Returns a Boolean value that indicates whether one rectangle completely encloses another.
- [func NSDivideRect(NSRect, UnsafeMutablePointer<NSRect>, UnsafeMutablePointer<NSRect>, Double, NSRectEdge)](nsdividerect(_:_:_:_:_:).md)
  Divides a rectangle into two new rectangles.
- [func NSEqualRects(NSRect, NSRect) -> Bool](nsequalrects(_:_:).md)
  Returns a Boolean value that indicates whether the two rectangles are equal.
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
- [func NSMinX(NSRect) -> Double](nsminx(_:).md)
  Returns the smallest x coordinate of a given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsisemptyrect(_:))*