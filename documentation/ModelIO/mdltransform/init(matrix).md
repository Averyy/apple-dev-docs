# init(matrix:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

Initializes a transform object with the specified transform matrix.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(matrix: matrix_float4x4)
```

```objc
- (instancetype) initWithMatrix:(matrix_float4x4) matrix;
```

#### Return Value

A new transform object.

#### Discussion

A transform matrix defines the local coordinate space transformations for a 3D object—that is, its position, orientation, shear, and scale.

After initializing a transform object from a matrix, you can use the [`translation`](./translation.md), [`rotation`](./rotation.md), [`shear`](./shear.md), and [`scale`](./scale.md) properties to individually work with those factors of the transform (or the corresponding methods listed in Using Factors of an Animated Transform to associate time-based transformation with each factor). To work with the complete transform matrix defined by those factors, use the [`matrix`](../mdltransformcomponent/matrix.md) property.

The `matrix` parameter must be an invertible, homogeneous affine transform matrix. If you initialize a transform object with a nonaffine transform matrix, attempts to retrieve its translation, rotation, shear, or scale factors instead return identity values.

## Parameters

- `matrix`: A transform matrix that defines a local coordinate space relative to a parent coordinate space.

## See Also

### Creating a Transform Object
- [convenience init(identity: ())](./init%28identity%29.md)
  Initializes a transform object to the identity transformation.
- [convenience init(transformComponent: any MDLTransformComponent)](./init%28transformcomponent%29.md)
  Initializes a transform object to match the specified transform component.
- [convenience init(matrix: matrix_float4x4, resetsTransform: Bool)](./init%28matrix,resetstransform%29.md)
- [convenience init(transformComponent: any MDLTransformComponent, resetsTransform: Bool)](./init%28transformcomponent,resetstransform%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransform/init(matrix:))*