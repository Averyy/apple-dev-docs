# ARCamera

**Framework**: ARKit  
**Kind**: class

Information about the camera position and imaging characteristics for a given frame.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARCamera
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)
- [Understanding World Tracking](understanding-world-tracking.md)

#### Overview

You get camera information from the [`camera`](arframe/camera.md) property of each [`ARFrame`](arframe.md) ARKit delivers.

## Topics

### Handling Tracking Status
- [var trackingState: ARCamera.TrackingState](arcamera/trackingstate-6i3pt.md)
  The general quality of position tracking available when the camera captured a frame.
- [ARCamera.TrackingState](arcamera/trackingstate-swift.enum.md)
  Values for position tracking quality, with possible causes when tracking quality is limited.
### Examining Camera Geometry
- [var transform: simd_float4x4](arcamera/transform.md)
  The position and orientation of the camera in world coordinate space.
- [var eulerAngles: simd_float3](arcamera/eulerangles.md)
  The orientation of the camera, expressed as roll, pitch, and yaw values.
### Examining Imaging Parameters
- [var imageResolution: CGSize](arcamera/imageresolution.md)
  The width and height, in pixels, of the captured camera image.
- [var intrinsics: simd_float3x3](arcamera/intrinsics.md)
  A matrix that converts between the 2D camera plane and 3D world coordinate space.
### Applying Camera Geometry
- [var projectionMatrix: simd_float4x4](arcamera/projectionmatrix.md)
  A transform matrix appropriate for rendering 3D content to match the image captured by the camera.
- [func projectionMatrix(for: UIInterfaceOrientation, viewportSize: CGSize, zNear: CGFloat, zFar: CGFloat) -> simd_float4x4](arcamera/projectionmatrix(for:viewportsize:znear:zfar:).md)
  Returns a transform matrix appropriate for rendering 3D content to match the image captured by the camera, using the specified parameters.
- [func viewMatrix(for: UIInterfaceOrientation) -> simd_float4x4](arcamera/viewmatrix(for:).md)
  Returns a transform matrix for converting from world space to camera space.
- [func projectPoint(simd_float3, orientation: UIInterfaceOrientation, viewportSize: CGSize) -> CGPoint](arcamera/projectpoint(_:orientation:viewportsize:).md)
  Returns the projection of a point from the 3D world space detected by ARKit into the 2D space of a view rendering the scene.
- [func unprojectPoint(CGPoint, ontoPlane: simd_float4x4, orientation: UIInterfaceOrientation, viewportSize: CGSize) -> simd_float3?](arcamera/unprojectpoint(_:ontoplane:orientation:viewportsize:).md)
  Returns the projection of a point from the 2D space of a view rendering the scene onto a plane in the 3D world space detected by ARKit.
### Applying Motion Blur
- [var exposureDuration: TimeInterval](arcamera/exposureduration.md)
  A value you use to effect motion blur when rendering your app’s virtual content.
### Applying Post-Processed Lighting
- [var exposureOffset: Float](arcamera/exposureoffset.md)
  A value you supply to your custom renderer to light your scene.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera)*