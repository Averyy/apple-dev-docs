# PhotogrammetrySession.Error

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The errors that can occur during reconstruction in a photogrammetry session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
enum Error
```

## Overview

Localize these errors in your app.

## Topics

### Enumeration Cases
- [PhotogrammetrySession.Error.insufficientStorage(requiredBytes:)](./error/insufficientstorage%28requiredbytes%29.md)
  An error that indicates insufficient storage space.
- [PhotogrammetrySession.Error.invalidImages(_:)](./error/invalidimages%28_%29.md)
  An error that represents a problem with the image directory URL.
- [PhotogrammetrySession.Error.invalidOutput(_:)](./error/invalidoutput%28_%29.md)
  An error that represents an invalid output location.
### Instance Properties
- [var localizedDescription: String](./error/localizeddescription.md)
  Retrieve the localized description for this error.

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Obtaining results
- [PhotogrammetrySession.Result](./result.md)
  An object that holds the created 3D object.
- [PhotogrammetrySession.PointCloud](./pointcloud.md)
  A sparse point cloud data structure output as the payload of a `.pointCloud` request. A point cloud is an array of `PointCloud.Point` instances.
- [PhotogrammetrySession.Pose](./pose.md)
  A 6DOF pose relative to the estimated coordinate system.
- [PhotogrammetrySession.Poses](./poses.md)
  Once initial photogrammetric calculations are complete, a data structure mapping the sample ID (or index if a folder was used) to the 6DOF algorithmically estimated pose of that sample is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/error)*