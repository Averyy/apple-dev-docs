# MDLStereoscopicCamera

**Framework**: Model I/O  
**Kind**: class

A point of view for rendering a stereoscopic display of a 3D scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLStereoscopicCamera
```

#### Overview

This class provides properties related to rendering the scene from two slightly different perspectives to simulate binocular vision. For general and optical properties of a camera, see the superclass [`MDLCamera`](mdlcamera.md).

## Topics

### Modeling Stereoscopic Imaging
- [var interPupillaryDistance: Float](mdlstereoscopiccamera/interpupillarydistance.md)
  The distance, in millimeters, between the stereoscopic camera’s two viewpoints.
- [var overlap: Float](mdlstereoscopiccamera/overlap.md)
  The amount, as a fraction of image width, by which the images from the camera’s two viewpoints overlap.
- [var leftVergence: Float](mdlstereoscopiccamera/leftvergence.md)
  The angle, in degrees, at which the camera’s left viewpoint faces toward a central focal point.
- [var rightVergence: Float](mdlstereoscopiccamera/rightvergence.md)
  The angle, in degrees, at which the camera’s right viewpoint faces toward a central focal point.
### Generating View and Projection Matrices
- [var leftViewMatrix: matrix_float4x4](mdlstereoscopiccamera/leftviewmatrix.md)
  The transformation matrix that determines the position and orientation of the camera’s left viewpoint relative to a scene.
- [var leftProjectionMatrix: matrix_float4x4](mdlstereoscopiccamera/leftprojectionmatrix.md)
  The transformation matrix that determines the extent of a scene visible to the camera’s left viewpoint.
- [var rightViewMatrix: matrix_float4x4](mdlstereoscopiccamera/rightviewmatrix.md)
  The transformation matrix that determines the position and orientation of the camera’s right viewpoint relative to a scene.
- [var rightProjectionMatrix: matrix_float4x4](mdlstereoscopiccamera/rightprojectionmatrix.md)
  The transformation matrix that determines the extent of a scene visible to the camera’s right viewpoint.

## Relationships

### Inherits From
- [MDLCamera](mdlcamera.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLCamera](mdlcamera.md)
  A point of view for rendering a 3D scene, along with a set of parameters describing an intended appearance for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlstereoscopiccamera)*