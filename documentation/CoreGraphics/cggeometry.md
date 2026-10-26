# CGGeometry

**Framework**: Core Graphics  
**Role**: API Collection

Various structures and associated functions for 2D geometric primitives.

#### Overview

The data structure [`CGPoint`](../CoreFoundation/cgpoint.md) represents a point in a two-dimensional coordinate system. The data structure [`CGRect`](../CoreFoundation/cgrect.md) represents the location and dimensions of a rectangle. The data structure [`CGSize`](../CoreFoundation/cgsize.md) represents the dimensions of width and height.

A [`CGPoint`](../CoreFoundation/cgpoint.md), [`CGRect`](../CoreFoundation/cgrect.md), or [`CGSize`](../CoreFoundation/cgsize.md) structure does not explicitly define the unit of measure for its member quantities. A point’s x- and y-coordinates or a size’s width and height are unitless quantities—whether such measurements are treated as pixels, scale-factor-independent points, texture elements (texels), or some other unit depends on the API using the measurement, and on the context in which that API is used. For example, a [`CGRect`](../CoreFoundation/cgrect.md) structure specifying the frame of an [`NSView`](../AppKit/nsview.md) or [`UIView`](../UIKit/uiview.md) object defines the view’s dimensions in points, not pixels. However, the effects of using a [`CGPoint`](../CoreFoundation/cgpoint.md) structure in a [`CGContext`](./cgcontext.md) drawing operation depend on the scale factor associated with that context. Where not otherwise specified, you can assume that a [`CGPoint`](../CoreFoundation/cgpoint.md), [`CGRect`](../CoreFoundation/cgrect.md), or [`CGSize`](../CoreFoundation/cgsize.md) structure is defined in points, not pixels. (For details, see [Drawing and Printing Guide for iOS](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156) or [High Resolution Guidelines for OS X](https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Introduction/Introduction.html#//apple_ref/doc/uid/TP40012302).)

The height and width stored in a [`CGRect`](../CoreFoundation/cgrect.md) data structure can be negative. For example, a rectangle with an origin of `[0.0, 0.0]` and a size of `[10.0,10.0]`  is exactly equivalent to a rectangle with an origin of `[10.0, 10.0]` and a size of `[-10.0,-10.0]`. Your application can standardize a rectangle—that is, ensure that the height and width are stored as positive values—by calling the `CGRectStandardize` function. All functions described in this reference that take [`CGRect`](../CoreFoundation/cgrect.md) data structures as inputs implicitly standardize those rectangles before calculating their results. For this reason, your applications should avoid directly reading and writing the data stored in the [`CGRect`](../CoreFoundation/cgrect.md) data structure. Instead, use the functions described here to manipulate rectangles and to retrieve their characteristics.

## Topics

### Creating a Dictionary Representation from a Geometric Primitive
- [func CGPointCreateDictionaryRepresentation(CGPoint) -> CFDictionary](./cgpointcreatedictionaryrepresentation%28_%29.md)
  Returns a dictionary representation of the specified point.
- [func CGSizeCreateDictionaryRepresentation(CGSize) -> CFDictionary](./cgsizecreatedictionaryrepresentation%28_%29.md)
  Returns a dictionary representation of the specified size.
- [func CGRectCreateDictionaryRepresentation(CGRect) -> CFDictionary](./cgrectcreatedictionaryrepresentation%28_%29.md)
  Returns a dictionary representation of the provided rectangle.
### Creating a Geometric Primitive from a Dictionary Representation
- [func CGPointMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGPoint>) -> Bool](./cgpointmakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a point using the contents of the specified dictionary.
- [func CGSizeMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGSize>) -> Bool](./cgsizemakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a size using the contents of the specified dictionary.
- [func CGRectMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGRect>) -> Bool](./cgrectmakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a rectangle using the contents of the specified dictionary.
### Creating a Geometric Primitive from Values
- [func CGPointMake(CGFloat, CGFloat) -> CGPoint](./cgpointmake%28_,_%29.md)
  Returns a point with the specified coordinates.
- [func CGRectMake(CGFloat, CGFloat, CGFloat, CGFloat) -> CGRect](./cgrectmake%28_,_,_,_%29.md)
  Returns a rectangle with the specified coordinate and size values.
- [func CGSizeMake(CGFloat, CGFloat) -> CGSize](./cgsizemake%28_,_%29.md)
  Returns a size with the specified dimension values.
- [func CGVectorMake(CGFloat, CGFloat) -> CGVector](./cgvectormake%28_,_%29.md)
  Returns a vector with the specified dimension values.
### Modifying Rectangles
- [func CGRectInset(CGRect, CGFloat, CGFloat) -> CGRect](./cgrectinset%28_,_,_%29.md)
  Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
- [func CGRectIntegral(CGRect) -> CGRect](./cgrectintegral%28_%29.md)
  Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [func CGRectIntersection(CGRect, CGRect) -> CGRect](./cgrectintersection%28_,_%29.md)
  Returns the intersection of two rectangles.
- [func CGRectOffset(CGRect, CGFloat, CGFloat) -> CGRect](./cgrectoffset%28_,_,_%29.md)
  Returns a rectangle with an origin that is offset from that of the source rectangle.
- [func CGRectStandardize(CGRect) -> CGRect](./cgrectstandardize%28_%29.md)
  Returns a rectangle with a positive width and height.
- [func CGRectUnion(CGRect, CGRect) -> CGRect](./cgrectunion%28_,_%29.md)
  Returns the smallest rectangle that contains the two source rectangles.
- [CGRectDivide](./cgrectdivide.md)
  Divides a source rectangle into two component rectangles.
### Comparing Values
- [func CGRectEqualToRect(CGRect, CGRect) -> Bool](./cgrectequaltorect%28_,_%29.md)
  Returns whether two rectangles are equal in size and position.
- [func CGRectIntersectsRect(CGRect, CGRect) -> Bool](./cgrectintersectsrect%28_,_%29.md)
  Returns whether two rectangles intersect.
- [CGPointEqualToPoint](./cgpointequaltopoint-c.macro.md)
  Returns whether two points are equal.
- [CGSizeEqualToSize](./cgsizeequaltosize-c.macro.md)
  Returns whether two sizes are equal.
### Checking for Membership
- [func CGRectContainsPoint(CGRect, CGPoint) -> Bool](./cgrectcontainspoint%28_,_%29.md)
  Returns whether a rectangle contains a specified point.
- [func CGRectContainsRect(CGRect, CGRect) -> Bool](./cgrectcontainsrect%28_,_%29.md)
  Returns whether the first rectangle contains the second rectangle.
### Getting Min, Mid, and Max Values
- [func CGRectGetMinX(CGRect) -> CGFloat](./cgrectgetminx%28_%29.md)
  Returns the smallest value for the x-coordinate of the rectangle.
- [func CGRectGetMinY(CGRect) -> CGFloat](./cgrectgetminy%28_%29.md)
  Returns the smallest value for the y-coordinate of the rectangle.
- [func CGRectGetMidX(CGRect) -> CGFloat](./cgrectgetmidx%28_%29.md)
  Returns the x- coordinate that establishes the center of a rectangle.
- [func CGRectGetMidY(CGRect) -> CGFloat](./cgrectgetmidy%28_%29.md)
  Returns the y-coordinate that establishes the center of the rectangle.
- [func CGRectGetMaxX(CGRect) -> CGFloat](./cgrectgetmaxx%28_%29.md)
  Returns the largest value of the x-coordinate for the rectangle.
- [func CGRectGetMaxY(CGRect) -> CGFloat](./cgrectgetmaxy%28_%29.md)
  Returns the largest value for the y-coordinate of the rectangle.
### Getting Height and Width
- [func CGRectGetHeight(CGRect) -> CGFloat](./cgrectgetheight%28_%29.md)
  Returns the height of a rectangle.
- [func CGRectGetWidth(CGRect) -> CGFloat](./cgrectgetwidth%28_%29.md)
  Returns the width of a rectangle.
### Checking Rectangle Characteristics
- [func CGRectIsEmpty(CGRect) -> Bool](./cgrectisempty%28_%29.md)
  Returns whether a rectangle has zero width or height, or is a null rectangle.
- [func CGRectIsNull(CGRect) -> Bool](./cgrectisnull%28_%29.md)
  Returns whether the rectangle is equal to the null rectangle.
- [func CGRectIsInfinite(CGRect) -> Bool](./cgrectisinfinite%28_%29.md)
  Returns whether a rectangle is infinite.
### Data Types
- [struct CGFloat](../CoreFoundation/cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [struct CGPoint](../CoreFoundation/cgpoint.md)
- [struct CGRect](../CoreFoundation/cgrect.md)
- [struct CGSize](../CoreFoundation/cgsize.md)
  A structure that contains width and height values.
- [struct CGVector](../CoreFoundation/cgvector.md)
  A structure that contains a two-dimensional vector.
### Constants
- [let CGRectInfinite: CGRect](./cgrectinfinite.md)
  A rectangle that has infinite extent.
- [Geometric Zeros](./geometric-zeros.md)
  A zero point, zero rectangle, or zero size.
- [let CGRectNull: CGRect](./cgrectnull.md)
  The null rectangle, representing an invalid value.
- [enum CGRectEdge](../CoreFoundation/cgrectedge.md)
- [CGFloat Informational Macros](./cgfloat-informational-macros.md)
  Informational macros for the `CGFloat` type.

## See Also

### Related Documentation
- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
### Reference
- [CGAffineTransform](./cgaffinetransform.md)
  An affine transformation matrix for use in drawing 2D graphics.
- [Core Graphics Structures](./core-graphics-structures.md)
- [Core Graphics Enumerations](./core-graphics-enumerations.md)
- [Core Graphics Constants](./core-graphics-constants.md)
- [Core Graphics Functions](./core-graphics-functions.md)
- [Core Graphics Data Types](./core-graphics-data-types.md)
- [Core Graphics Macros](./core-graphics-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggeometry)*