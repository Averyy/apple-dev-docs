# transformStruct

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The matrix coefficients stored as the transformation matrix.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var transformStruct: NSAffineTransformStruct { get set }
```

```objc
@property NSAffineTransformStruct transformStruct;
```

#### Discussion

The matrix is of the form shown in [Transform Mathematics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Transforms/Transforms.html#//apple_ref/doc/uid/TP40003290-CH204-BCIIICJI), and the six-element structure defined by the [`NSAffineTransformStruct`](../nsaffinetransformstruct.md) structure is of the form:

```objc
{m11, m12, m21, m22, tX, tY}
```

The [`NSAffineTransformStruct`](../nsaffinetransformstruct.md) structure is an alternate representation of a transformation matrix that can be used to specify matrix values directly.

## See Also

### Related Documentation
- [convenience init(transform: NSAffineTransform)](./init%28transform%29.md)
  Initializes the receiver’s matrix using another transform object.
### Accessing the Transformation Matrix
- [struct NSAffineTransformStruct](../nsaffinetransformstruct.md)
  A structure that defines the three-by-three matrix that performs an affine transform between two coordinate systems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsaffinetransform/transformstruct)*