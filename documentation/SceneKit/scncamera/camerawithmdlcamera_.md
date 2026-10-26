# cameraWithMDLCamera:

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a camera from the specified Model I/O camera object.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```objc
+ (instancetype) cameraWithMDLCamera:(MDLCamera *) mdlCamera;
```

#### Return Value

A new camera object.

#### Discussion

The Model I/O framework provides universal support for import, export, description, and processing of several 3D asset file formats and related resources. (For details, see [Model I/O](../../ModelIO/ModelIO.md).) The [`MDLCamera`](../../ModelIO/mdlcamera.md) class is a generic description of a viewpoint on a scene, supporting a superset of the attributes described by the [`SCNCamera`](../scncamera.md) class.

## Parameters

- `mdlCamera`: A Model I/O camera object.

## See Also

### Creating a Camera
- [+ camera](./camera.md)
  Creates a new camera object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/camerawithmdlcamera:)*