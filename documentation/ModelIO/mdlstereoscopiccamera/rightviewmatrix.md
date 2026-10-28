# rightViewMatrix

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The transformation matrix that determines the position and orientation of the camera’s right viewpoint relative to a scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rightViewMatrix: matrix_float4x4 { get }
```

```objc
@property (nonatomic, readonly) matrix_float4x4 rightViewMatrix;
```

## Discussion

Model I/O  automatically generates this matrix from the camera’s position and orientation, additionally using the [`interPupillaryDistance`](./interpupillarydistance.md) and [`rightVergence`](./rightvergence.md) properties to account for the offset and angle of a stereoscopic camera’s left viewpoint.

A renderer uses this matrix, along with the [`rightProjectionMatrix`](./rightprojectionmatrix.md) property and model matrices derived from the camera’s position and orientation (the [`transform`](../mdlobject/transform.md) property) and the content to be rendered, to transform vertex data to the renderer’s 2D screen space at render time.

## See Also

### Generating View and Projection Matrices
- [var leftViewMatrix: matrix_float4x4](./leftviewmatrix.md)
  The transformation matrix that determines the position and orientation of the camera’s left viewpoint relative to a scene.
- [var leftProjectionMatrix: matrix_float4x4](./leftprojectionmatrix.md)
  The transformation matrix that determines the extent of a scene visible to the camera’s left viewpoint.
- [var rightProjectionMatrix: matrix_float4x4](./rightprojectionmatrix.md)
  The transformation matrix that determines the extent of a scene visible to the camera’s right viewpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlstereoscopiccamera/rightviewmatrix)*