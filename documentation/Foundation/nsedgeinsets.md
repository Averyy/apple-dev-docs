# NSEdgeInsets

**Framework**: Foundation  
**Kind**: struct

A description of the distance between the edges of two rectangles.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct NSEdgeInsets
```

#### Overview

Edge insets describe the distance between the edges of one rectangle to a related rectangle that can be described by measuring a constant but edge-specific distance from each edge.

A common use for this structure is to describe the relationship between a view’s frame and its alignment rectangle.

## Topics

### Creating an edge insets structure
- [init(top: Double, left: Double, bottom: Double, right: Double)](nsedgeinsets/init(top:left:bottom:right:).md)
  Creates an edge insets structure with the specified inset values.
- [func NSEdgeInsetsMake(Double, Double, Double, Double) -> NSEdgeInsets](nsedgeinsetsmake(_:_:_:_:).md)
  Creates an edge insets structure with the specified inset values.
- [init()](nsedgeinsets/init.md)
  Creates an edge insets structure.
### Specifying the edge insets
- [var bottom: Double](nsedgeinsets/bottom.md)
  The distance from the bottom of the source rectangle to the bottom of the result rectangle.
- [var left: Double](nsedgeinsets/left.md)
  The distance from the left side of the source rectangle to the left side of the result rectangle.
- [var right: Double](nsedgeinsets/right.md)
  The distance from the right side of the source rectangle to the right side of the result rectangle.
- [var top: Double](nsedgeinsets/top.md)
  The distance from the top of the source rectangle to the top of the result rectangle.
### Comparing edge insets
- [func NSEdgeInsetsEqual(NSEdgeInsets, NSEdgeInsets) -> Bool](nsedgeinsetsequal(_:_:).md)
  Returns a Boolean value that indicates whether two edge insets structures are equal.
### Getting the zero constant
- [let NSEdgeInsetsZero: NSEdgeInsets](nsedgeinsetszero.md)
  An edge insets structure with a zero inset on each edge.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [@frozen struct CGFloat](../CoreFoundation/CGFloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [typealias NSPoint](nspoint.md)
  A point in a Cartesian coordinate system.
- [typealias NSSize](nssize.md)
  A two-dimensional size.
- [typealias NSRect](nsrect.md)
  A rectangle.
- [struct AffineTransform](affinetransform.md)
  A graphics coordinate transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsedgeinsets)*