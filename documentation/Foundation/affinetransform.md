# AffineTransform

**Framework**: Foundation  
**Kind**: struct

A graphics coordinate transformation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
struct AffineTransform
```

## Topics

### Creating Transforms
- [init()](affinetransform/init.md)
  Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees: CGFloat)](affinetransform/init(rotationbydegrees:).md)
  Creates an affine transformation matrix from a rotation angle.
- [init(rotationByRadians: CGFloat)](affinetransform/init(rotationbyradians:).md)
  Creates an affine transformation matrix from a rotation angle.
- [init(scale: CGFloat)](affinetransform/init(scale:).md)
  Creates an affine transformation matrix from scaling a single value.
- [init(scaleByX: CGFloat, byY: CGFloat)](affinetransform/init(scalebyx:byy:).md)
  Creates an affine transformation matrix from scaling values.
- [init(translationByX: CGFloat, byY: CGFloat)](affinetransform/init(translationbyx:byy:).md)
  Creates an affine transformation matrix from translation values.
- [init(m11: CGFloat, m12: CGFloat, m21: CGFloat, m22: CGFloat, tX: CGFloat, tY: CGFloat)](affinetransform/init(m11:m12:m21:m22:tx:ty:).md)
  Creates an affine transformation.
### Getting the Identity Transform
- [static let identity: AffineTransform](affinetransform/identity.md)
  An identity affine transformation matrix.
### Accumulating Tranformations
- [func rotate(byDegrees: CGFloat)](affinetransform/rotate(bydegrees:).md)
  Mutates an affine transformation matrix to apply a rotation.
- [func rotate(byRadians: CGFloat)](affinetransform/rotate(byradians:).md)
  Mutates an affine transformation matrix to apply a rotation.
- [func scale(CGFloat)](affinetransform/scale(_:).md)
  Mutates an affine transformation matrix to apply scaling in both x and y dimensions.
- [func scale(x: CGFloat, y: CGFloat)](affinetransform/scale(x:y:).md)
  Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.
- [func translate(x: CGFloat, y: CGFloat)](affinetransform/translate(x:y:).md)
  Mutates an affine transformation matrix to perform the specified translation.
- [func append(AffineTransform)](affinetransform/append(_:).md)
  Mutates an affine transformation by appending another affine transform.
- [func prepend(AffineTransform)](affinetransform/prepend(_:).md)
  Mutates an affine transformation by prepending another affine transform.
- [func invert()](affinetransform/invert.md)
  Inverts the transformation matrix, if possible.
- [func inverted() -> AffineTransform?](affinetransform/inverted.md)
  Returns an inverted version of the matrix, if possible, or nil if not.
### Transforming Data and Objects
- [func transform(NSPoint) -> NSPoint](affinetransform/transform(_:)-1ozpp.md)
  Applies the affine transform to the specified point.
- [func transform(NSSize) -> NSSize](affinetransform/transform(_:)-6fze6.md)
  Applies the affine transform to the specified size.
### Accessing the Transformation Matrix
- [var m11: CGFloat](affinetransform/m11.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var m12: CGFloat](affinetransform/m12.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var m21: CGFloat](affinetransform/m21.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var m22: CGFloat](affinetransform/m22.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var tX: CGFloat](affinetransform/tx.md)
  An element of the transform matrix that contributes translation.
- [var tY: CGFloat](affinetransform/ty.md)
  An element of the transform matrix that contributes translation.
### Using Reference Types
- [class NSAffineTransform](nsaffinetransform.md)
  A graphics coordinate transformation.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [@frozen struct CGFloat](../CoreFoundation/CGFloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [typealias NSPoint](nspoint.md)
  A point in a Cartesian coordinate system.
- [typealias NSSize](nssize.md)
  A two-dimensional size.
- [typealias NSRect](nsrect.md)
  A rectangle.
- [struct NSEdgeInsets](nsedgeinsets.md)
  A description of the distance between the edges of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/affinetransform)*