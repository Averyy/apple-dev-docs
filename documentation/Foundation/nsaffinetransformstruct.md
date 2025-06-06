# NSAffineTransformStruct

**Framework**: Foundation  
**Kind**: struct

A structure that defines the three-by-three matrix that performs an affine transform between two coordinate systems.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct NSAffineTransformStruct
```

#### Overview

For more details, see [`Cocoa Drawing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290).

## Topics

### Initializers
- [init()](nsaffinetransformstruct/init.md)
  Initializes a zero-filled transformation matrix.
- [init(m11: Double, m12: Double, m21: Double, m22: Double, tX: Double, tY: Double)](nsaffinetransformstruct/init(m11:m12:m21:m22:tx:ty:).md)
### Instance Properties
- [var m11: Double](nsaffinetransformstruct/m11.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var m12: Double](nsaffinetransformstruct/m12.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var m21: Double](nsaffinetransformstruct/m21.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var m22: Double](nsaffinetransformstruct/m22.md)
  An element of the transform matrix that contributes scaling, rotation, and shear.
- [var tX: Double](nsaffinetransformstruct/tx.md)
  An element of the transform matrix that contributes translation.
- [var tY: Double](nsaffinetransformstruct/ty.md)
  An element of the transform matrix that contributes translation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var transformStruct: NSAffineTransformStruct](nsaffinetransform/transformstruct.md)
  The matrix coefficients stored as the transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransformstruct)*