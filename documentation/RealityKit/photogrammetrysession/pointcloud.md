# PhotogrammetrySession.PointCloud

**Framework**: RealityKit  
**Kind**: struct

A sparse point cloud data structure output as the payload of a `.pointCloud` request. A point cloud is an array of `PointCloud.Point` instances.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
struct PointCloud
```

## Topics

### Structures
- [PhotogrammetrySession.PointCloud.Point](photogrammetrysession/pointcloud/point.md)
### Instance Properties
- [let points: [PhotogrammetrySession.PointCloud.Point]](photogrammetrysession/pointcloud/points.md)
  The fixed array of points describing the point cloud.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [PhotogrammetrySession.Result](photogrammetrysession/result.md)
  An object that holds the created 3D object.
- [PhotogrammetrySession.Error](photogrammetrysession/error.md)
  The errors that can occur during reconstruction in a photogrammetry session.
- [PhotogrammetrySession.Pose](photogrammetrysession/pose.md)
  A 6DOF pose relative to the estimated coordinate system.
- [PhotogrammetrySession.Poses](photogrammetrysession/poses.md)
  Once initial photogrammetric calculations are complete, a data structure mapping the sample ID (or index if a folder was used) to the 6DOF algorithmically estimated pose of that sample is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/pointcloud)*