# AffineTransform

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A graphics coordinate transformation.

**Availability**:
- macOS 10.10+

## Declaration

```swift
struct AffineTransform
```

## Topics

### Creating Transforms
- [init()](./affinetransform/init%28%29.md)
  Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees: CGFloat)](./affinetransform/init%28rotationbydegrees%29.md)
  Creates an affine transformation matrix from a rotation angle.
- [init(rotationByRadians: CGFloat)](./affinetransform/init%28rotationbyradians%29.md)
  Creates an affine transformation matrix from a rotation angle.
- [init(scale: CGFloat)](./affinetransform/init%28scale%29.md)
  Creates an affine transformation matrix from scaling a single value.
- [init(scaleByX: CGFloat, byY: CGFloat)](./affinetransform/init%28scalebyx,byy%29.md)
  Creates an affine transformation matrix from scaling values.
- [init(translationByX: CGFloat, byY: CGFloat)](./affinetransform/init%28translationbyx,byy%29.md)
  Creates an affine transformation matrix from translation values.
- [init(m11: CGFloat, m12: CGFloat, m21: CGFloat, m22: CGFloat, tX: CGFloat, tY: CGFloat)](./affinetransform/init%28m11,m12,m21,m22,tx,ty%29.md)
  Creates an affine transformation.
### Getting the Identity Transform
- [static let identity: AffineTransform](./affinetransform/identity.md)
  An identity affine transformation matrix.
### Accumulating Tranformations
- [func rotate(byDegrees: CGFloat)](./affinetransform/rotate%28bydegrees%29.md)
  Mutates an affine transformation matrix to apply a rotation.
- [func rotate(byRadians: CGFloat)](./affinetransform/rotate%28byradians%29.md)
  Mutates an affine transformation matrix to apply a rotation.
- [func scale(CGFloat)](./affinetransform/scale%28_%29.md)
  Mutates an affine transformation matrix to apply scaling in both x and y dimensions.
- [func scale(x: CGFloat, y: CGFloat)](./affinetransform/scale%28x,y%29.md)
  Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.
- [func translate(x: CGFloat, y: CGFloat)](./affinetransform/translate%28x,y%29.md)
  Mutates an affine transformation matrix to perform the specified translation.
- [func append(AffineTransform)](./affinetransform/append%28_%29.md)
  Mutates an affine transformation by appending another affine transform.
- [func prepend(AffineTransform)](./affinetransform/prepend%28_%29.md)
  Mutates an affine transformation by prepending another affine transform.
- [func invert()](./affinetransform/invert%28%29.md)
  Inverts the transformation matrix, if possible.
- [func inverted() -> AffineTransform?](./affinetransform/inverted%28%29.md)
  Returns an inverted version of the matrix, if possible, or nil if not.
### Transforming Data and Objects
- [func transform(NSPoint) -> NSPoint](./affinetransform/transform%28_%29-1ozpp.md)
  Applies the affine transform to the specified point.
- [func transform(NSSize) -> NSSize](./affinetransform/transform%28_%29-6fze6.md)
  Applies the affine transform to the specified size.
### Accessing the Transformation Matrix
- [var m11: CGFloat](./affinetransform/m11.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var m12: CGFloat](./affinetransform/m12.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var m21: CGFloat](./affinetransform/m21.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var m22: CGFloat](./affinetransform/m22.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var tX: CGFloat](./affinetransform/tx.md)
  An element of the transform matrix that contributes translation.
- [var tY: CGFloat](./affinetransform/ty.md)
  An element of the transform matrix that contributes translation.
### Using Reference Types
- [class NSAffineTransform](./nsaffinetransform.md)
  A graphics coordinate transformation.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [ReferenceConvertible](./referenceconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Geometry
- [struct CGFloat](../CoreFoundation/cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [typealias NSPoint](./nspoint.md)
  A point in a Cartesian coordinate system.
- [typealias NSSize](./nssize.md)
  A two-dimensional size.
- [typealias NSRect](./nsrect.md)
  A rectangle.
- [struct NSEdgeInsets](./nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform)*