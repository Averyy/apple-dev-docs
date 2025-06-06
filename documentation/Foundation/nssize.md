# NSSize

**Framework**: Foundation  
**Kind**: typealias

A two-dimensional size.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias NSSize = CGSize
```

#### Discussion

Normally, the values of `width` and `height` are non-negative. The functions that create an `NSSize` structure do not prevent you from setting a negative value for these attributes. If the value of `width` or `height` is negative, however, the behavior of some methods may be undefined.

##### Special Considerations

Prior to OS X v10.5 the width and height were represented by `float` values rather than `CGFloat` values.

When building for 64 bit systems, or building 32 bit like 64 bit, `NSSize` is typedef’d to `CGSize`.

## Topics

### Managing Sizes
- [func NSEqualSizes(NSSize, NSSize) -> Bool](nsequalsizes(_:_:).md)
  Returns a Boolean that indicates whether two size values are equal.
- [func NSMakeSize(Double, Double) -> NSSize](nsmakesize(_:_:).md)
  Returns a new `NSSize` from the specified values.
- [func NSSizeFromString(String) -> NSSize](nssizefromstring(_:).md)
  Returns an `NSSize` from a text-based representation.
- [func NSStringFromSize(NSSize) -> String](nsstringfromsize(_:).md)
  Returns a string representation of a size.
- [func NSSizeFromCGSize(CGSize) -> NSSize](nssizefromcgsize(_:).md)
  Returns an `NSSize` typecast from a `CGSize`.
- [func NSSizeToCGSize(NSSize) -> CGSize](nssizetocgsize(_:).md)
  Returns a `CGSize` typecast from an `NSSize`.
### Zero Constant
- [let NSZeroSize: NSSize](nszerosize.md)
  An `NSSize` structure set to `0` in both dimensions.
### Related Types
- [typealias NSSizeArray](nssizearray.md)
  Type indicating a parameter is an array of `NSSize` structures.
- [typealias NSSizePointer](nssizepointer.md)
  Type indicating parameter is a pointer to an `NSSize` structure.

## See Also

- [@frozen struct CGFloat](../CoreFoundation/CGFloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [typealias NSPoint](nspoint.md)
  A point in a Cartesian coordinate system.
- [typealias NSRect](nsrect.md)
  A rectangle.
- [struct AffineTransform](affinetransform.md)
  A graphics coordinate transformation.
- [struct NSEdgeInsets](nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssize)*