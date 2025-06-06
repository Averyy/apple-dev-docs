# PhotogrammetrySession.Pose

**Framework**: RealityKit  
**Kind**: struct

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
- [let rotation: simd_quatf](photogrammetrysession/pose/rotation.md)
  Rotation (orientation) of the pose relative to the reference coordinate system.
- [var transform: Transform](photogrammetrysession/pose/transform.md)
  A unit scale transform that represents a 6DoF pose.
- [let translation: SIMD3<Float>](photogrammetrysession/pose/translation.md)
  Position of the pose relative to the reference coordinate system.

## See Also

- [PhotogrammetrySession.Result](photogrammetrysession/result.md)
  An object that holds the created 3D object.
- [PhotogrammetrySession.PointCloud](photogrammetrysession/pointcloud.md)
  A sparse point cloud data structure output as the payload of a `.pointCloud` request. A point cloud is an array of `PointCloud.Point` instances.
- [PhotogrammetrySession.Error](photogrammetrysession/error.md)
  The errors that can occur during reconstruction in a photogrammetry session.
- [PhotogrammetrySession.Poses](photogrammetrysession/poses.md)
  Once initial photogrammetric calculations are complete, a data structure mapping the sample ID (or index if a folder was used) to the 6DOF algorithmically estimated pose of that sample is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/pose)*