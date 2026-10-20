# PhotogrammetrySession.Pose

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A 6DOF pose relative to the estimated coordinate system.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Pose
```

## Topics

### Instance Properties
- [var intrinsics: simd_float3x3?](./pose/intrinsics.md)
  If available, the estimated pinhole camera intrinsics matrix associated with the input image.  If not available, `nil`.
- [var lensDistortionData: LensDistortionData?](./pose/lensdistortiondata.md)
  If available, the estimated lens distortion data for the associated input image.  This can be used to rectify the image for computer vision applications.  If not available, this is nil.
- [let rotation: simd_quatf](./pose/rotation.md)
  Rotation (orientation) of the pose relative to the reference coordinate system.
- [var transform: Transform](./pose/transform.md)
  A unit scale transform that represents a 6DoF pose.
- [let translation: SIMD3<Float>](./pose/translation.md)
  Position of the pose relative to the reference coordinate system.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Obtaining results
- [PhotogrammetrySession.Result](./result.md)
  An object that holds the created 3D object.
- [PhotogrammetrySession.PointCloud](./pointcloud.md)
  A sparse point cloud data structure output as the payload of a `.pointCloud` request. A point cloud is an array of `PointCloud.Point` instances.
- [PhotogrammetrySession.Error](./error.md)
  The errors that can occur during reconstruction in a photogrammetry session.
- [PhotogrammetrySession.Poses](./poses.md)
  Once initial photogrammetric calculations are complete, a data structure mapping the sample ID (or index if a folder was used) to the 6DOF algorithmically estimated pose of that sample is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/pose)*