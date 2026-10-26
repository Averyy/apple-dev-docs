# NSPoint

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

A point in a Cartesian coordinate system.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias NSPoint = CGPoint
```

```c
typedef CGPoint NSPoint;
```

#### Discussion

Prior to OS X v10.5 the coordinates were represented by `float` values rather than `CGFloat` values.

When building for 64 bit systems, or building 32 bit like 64 bit, `NSPoint` is typedef’d to `CGPoint`.

## Topics

### Managing Points
- [func NSEqualPoints(NSPoint, NSPoint) -> Bool](./nsequalpoints%28_,_%29.md)
  Returns a Boolean value that indicates whether two points are equal.
- [func NSMakePoint(Double, Double) -> NSPoint](./nsmakepoint%28_,_%29.md)
  Creates a new `NSPoint` from the specified values.
- [func NSPointFromString(String) -> NSPoint](./nspointfromstring%28_%29.md)
  Returns a point from a text-based representation.
- [func NSStringFromPoint(NSPoint) -> String](./nsstringfrompoint%28_%29.md)
  Returns a string representation of a point.
- [func NSPointFromCGPoint(CGPoint) -> NSPoint](./nspointfromcgpoint%28_%29.md)
  Returns an `NSPoint` typecast from a `CGPoint`.
- [func NSPointToCGPoint(NSPoint) -> CGPoint](./nspointtocgpoint%28_%29.md)
  Returns a `CGPoint` typecast from an `NSPoint`.
### Zero Constant
- [let NSZeroPoint: NSPoint](./nszeropoint.md)
  An `NSPoint` structure with both x and y coordinates set to `0`.
### Related Types
- [typealias NSPointArray](./nspointarray.md)
  Type indicating a parameter is array of `NSPoint` structures.
- [typealias NSPointPointer](./nspointpointer.md)
  Type indicating a parameter is a pointer to an `NSPoint` structure.

## See Also

### Geometry
- [struct CGFloat](../CoreFoundation/cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [typealias NSSize](./nssize.md)
  A two-dimensional size.
- [typealias NSRect](./nsrect.md)
  A rectangle.
- [struct AffineTransform](./affinetransform.md)
  A graphics coordinate transformation.
- [struct NSEdgeInsets](./nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.
- [NSAffineTransform](./nsaffinetransform.md)
  A graphics coordinate transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspoint)*