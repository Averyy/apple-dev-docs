# PhotogrammetrySession.Result

**Framework**: RealityKit  
**Kind**: enum

An object that holds the created 3D object.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum Result
```

#### Overview

When [`PhotogrammetrySession`](photogrammetrysession.md) completes a [`PhotogrammetrySession.Request`](photogrammetrysession/request.md), it publishes a [`PhotogrammetrySession.Output.requestComplete(_:_:)`](photogrammetrysession/output/requestcomplete(_:_:).md) message to output, and includes the created object as the associated value of the result parameter. The result type corresponds to the request type. For example, a [`PhotogrammetrySession.Request.modelFile(url:detail:geometry:)`](photogrammetrysession/request/modelfile(url:detail:geometry:).md) request results in the session publishing a [`PhotogrammetrySession.Result.modelFile(_:)`](photogrammetrysession/result/modelfile(_:).md).

## Topics

### Types of output
- [PhotogrammetrySession.Result.modelFile(_:)](photogrammetrysession/result/modelfile(_:).md)
  The result of a request for a USDZ file.
- [PhotogrammetrySession.Result.modelEntity(_:)](photogrammetrysession/result/modelentity(_:).md)
  The result of a request for an in-memory entity.
- [PhotogrammetrySession.Result.bounds(_:)](photogrammetrysession/result/bounds(_:).md)
  The result of a request for a bounding box.
### Enumeration Cases
- [case pointCloud(PhotogrammetrySession.PointCloud)](photogrammetrysession/result/pointcloud(_:).md)
  The result of a request for a point cloud.
- [case poses(PhotogrammetrySession.Poses)](photogrammetrysession/result/poses(_:).md)
  Once initial photogrammetric calculations are complete, a data structure  mapping each sample ID (or index if a folder was used) to the 6DOF algorithmically estimated pose of that sample is returned.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [PhotogrammetrySession.PointCloud](photogrammetrysession/pointcloud.md)
  A sparse point cloud data structure output as the payload of a `.pointCloud` request. A point cloud is an array of `PointCloud.Point` instances.
- [PhotogrammetrySession.Error](photogrammetrysession/error.md)
  The errors that can occur during reconstruction in a photogrammetry session.
- [PhotogrammetrySession.Pose](photogrammetrysession/pose.md)
  A 6DOF pose relative to the estimated coordinate system.
- [PhotogrammetrySession.Poses](photogrammetrysession/poses.md)
  Once initial photogrammetric calculations are complete, a data structure mapping the sample ID (or index if a folder was used) to the 6DOF algorithmically estimated pose of that sample is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/result)*