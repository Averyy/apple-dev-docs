# init(identity:)

**Framework**: Model I/O  
**Kind**: init

Initializes a transform object to the identity transformation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(identity: ())
```

#### Return Value

A new transform object.

#### Discussion

A transform matrix defines the local coordinate space transformations for a 3D object—that is, its position, orientation, shear, and scale. The identity transform is equivalent to no transformation, so an object affected by the transform uses the same coordinate space as its parent.

After initializing a transform object, you can use the [`translation`](mdltransform/translation.md), [`rotation`](mdltransform/rotation.md), [`shear`](mdltransform/shear.md), and [`scale`](mdltransform/scale.md) properties to individually work with those factors of the transform (or the corresponding methods listed in Using Factors of an Animated Transform to associate time-based transformation with each factor). To work with the complete transform matrix defined by those factors, use the [`matrix`](mdltransformcomponent/matrix.md) property.

## See Also

- [convenience init(matrix: matrix_float4x4)](mdltransform/init(matrix:).md)
  Initializes a transform object with the specified transform matrix.
- [convenience init(transformComponent: any MDLTransformComponent)](mdltransform/init(transformcomponent:).md)
  Initializes a transform object to match the specified transform component.
- [convenience init(matrix: matrix_float4x4, resetsTransform: Bool)](mdltransform/init(matrix:resetstransform:).md)
- [convenience init(transformComponent: any MDLTransformComponent, resetsTransform: Bool)](mdltransform/init(transformcomponent:resetstransform:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/init(identity:))*