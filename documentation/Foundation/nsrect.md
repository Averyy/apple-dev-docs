# NSRect

**Framework**: Foundation  
**Kind**: typealias

A rectangle.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias NSRect = CGRect
```

#### Discussion

When building for 64 bit systems, or building 32 bit like 64 bit, `NSRect` is typedef’d to `CGRect`.

## Topics

### Managing Rectangles
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
- [func NSMinX(NSRect) -> Double](nsminx(_:).md)
  Returns the smallest x coordinate of a given rectangle.
- [func NSMinY(NSRect) -> Double](nsminy(_:).md)
  Returns the smallest y coordinate of a given rectangle.
- [func NSMouseInRect(NSPoint, NSRect, Bool) -> Bool](nsmouseinrect(_:_:_:).md)
  Returns a Boolean value that indicates whether the point is in the specified rectangle.
- [func NSOffsetRect(NSRect, Double, Double) -> NSRect](nsoffsetrect(_:_:_:).md)
  Offsets the rectangle by the specified amount.
- [func NSPointInRect(NSPoint, NSRect) -> Bool](nspointinrect(_:_:).md)
  Returns a Boolean value that indicates whether a given point is in a given rectangle.
- [func NSRectFromString(String) -> NSRect](nsrectfromstring(_:).md)
  Returns a rectangle from a text-based representation.
- [func NSStringFromRect(NSRect) -> String](nsstringfromrect(_:).md)
  Returns a string representation of a rectangle.
- [func NSRectFromCGRect(CGRect) -> NSRect](nsrectfromcgrect(_:).md)
  Returns an `NSRect` typecast from a `CGRect`.
- [func NSRectToCGRect(NSRect) -> CGRect](nsrecttocgrect(_:).md)
  Returns a `CGRect` typecast from an `NSRect`.
- [func NSUnionRect(NSRect, NSRect) -> NSRect](nsunionrect(_:_:).md)
  Calculates the union of two rectangles.
- [func NSWidth(NSRect) -> Double](nswidth(_:).md)
  Returns the width of the specified rectangle.
### Zero Constant
- [let NSZeroRect: NSRect](nszerorect.md)
  An `NSRect` structure set to `0` in width and height.
### Related Types
- [enum NSRectEdge](nsrectedge.md)
- [struct AlignmentOptions](alignmentoptions.md)
  Values representing alignment operations.
- [typealias NSRectArray](nsrectarray.md)
  Type indicating a parameter is array of `NSRect` structures.
- [typealias NSRectPointer](nsrectpointer.md)
  Type indicating a parameter is a pointer to an `NSRect` structure.

## See Also

- [struct CGFloat](../CoreFoundation/CGFloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [typealias NSPoint](nspoint.md)
  A point in a Cartesian coordinate system.
- [typealias NSSize](nssize.md)
  A two-dimensional size.
- [struct AffineTransform](affinetransform.md)
  A graphics coordinate transformation.
- [struct NSEdgeInsets](nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrect)*