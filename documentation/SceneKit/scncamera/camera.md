# camera

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a new camera object.

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
+ (instancetype) camera;
```

## Return Value

A new camera object.

## Discussion

To use the camera to display a scene, attach it to the [`camera`](../scnnode/camera.md) property of a node and then select that node using the [`pointOfView`](../scnscenerenderer/pointofview.md) property of the view (or layer or renderer) rendering the scene.

## See Also

### Creating a Camera
- [+ cameraWithMDLCamera:](./camerawithmdlcamera_.md)
  Creates a camera from the specified Model I/O camera object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/camera)*