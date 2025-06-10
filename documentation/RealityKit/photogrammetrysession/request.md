# PhotogrammetrySession.Request

**Framework**: RealityKit  
**Kind**: enum

An object that configures a photogrammetry session reconstruction request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum Request
```

## Mentions

- [Creating 3D objects from photographs](creating-3d-objects-from-photographs.md)

#### Overview

Create a [`PhotogrammetrySession.Request`](photogrammetrysession/request.md) for each 3D object you want to construct from the same set of photographs. You might, for example, create a session with two requests, one to generate a low-resolution preview object in memory, and a second to generate a high-resolution final object saved to the file system.

Before creating an instance of this class,  check [`isSupported`](photogrammetrysession/issupported.md) to ensure object capture is available on the current device.

For more information on using [`PhotogrammetrySession`](photogrammetrysession.md), see [`Creating 3D objects from photographs`](creating-3d-objects-from-photographs.md).

## Topics

### Creating the request
- [init(modelFile: URL)](photogrammetrysession/request/init(modelfile:).md)
  Creates an instance based on the contents of a USDZ file.
### Specifying the output
- [case modelFile(url: URL, detail: PhotogrammetrySession.Request.Detail, geometry: PhotogrammetrySession.Request.Geometry?)](photogrammetrysession/request/modelfile(url:detail:geometry:).md)
  An object-creation request saved to a USDZ file or a folder (for OBJ output).
- [case modelEntity(detail: PhotogrammetrySession.Request.Detail, geometry: PhotogrammetrySession.Request.Geometry?)](photogrammetrysession/request/modelentity(detail:geometry:).md)
  An object-creation request stored in-memory for immediate display.
- [PhotogrammetrySession.Request.bounds](photogrammetrysession/request/bounds.md)
  An object-creation request that returns a box the same size as the created model.
- [PhotogrammetrySession.Request.Detail](photogrammetrysession/request/detail.md)
  Supported levels of detail for a request.
### Transforming the created model
- [PhotogrammetrySession.Request.Geometry](photogrammetrysession/request/geometry.md)
  An object that holds a bounding box and transformation data for a request.
### Enumeration Cases
- [PhotogrammetrySession.Request.pointCloud](photogrammetrysession/request/pointcloud.md)
  The raw detected points from the pictures with no polygons connecting them.
- [PhotogrammetrySession.Request.poses](photogrammetrysession/request/poses.md)
  Requests the estimated pose of the camera in each shot (relative to the common estimated coordinate system shared with the `.bounds` request).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request)*