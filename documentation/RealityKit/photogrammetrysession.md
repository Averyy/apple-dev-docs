# PhotogrammetrySession

**Framework**: RealityKit  
**Kind**: class

Manages the creation of a 3D model from a set of images.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class PhotogrammetrySession
```

## Mentions

- [Creating 3D objects from photographs](creating-3d-objects-from-photographs.md)

#### Overview

For more information on using [`PhotogrammetrySession`](photogrammetrysession.md), see [`Creating 3D objects from photographs`](creating-3d-objects-from-photographs.md).

## Topics

### Creating the session
- [convenience init(input: URL, configuration: PhotogrammetrySession.Configuration) throws](photogrammetrysession/init(input:configuration:)-wo4e.md)
  Creates a session from a specified directory of images.
- [convenience init<S>(input: S, configuration: PhotogrammetrySession.Configuration) throws](photogrammetrysession/init(input:configuration:)-7glmh.md)
  Creates a session from a sequence of samples.
- [static var isSupported: Bool](photogrammetrysession/issupported.md)
  Returns `true` if the current hardware supports Object Capture.
### Configuring the session
- [var configuration: PhotogrammetrySession.Configuration](photogrammetrysession/configuration-swift.property.md)
  Readonly property  containing the session configuration set in the construction.
- [PhotogrammetrySession.Configuration](photogrammetrysession/configuration-swift.struct.md)
  The configuration parameters for a photogrammetry session.
### Monitoring the session
- [var activeRequests: [PhotogrammetrySession.Request]](photogrammetrysession/activerequests.md)
  The session’s active request objects.
- [var isProcessing: Bool](photogrammetrysession/isprocessing.md)
  The session is actively processing requests.
- [var outputs: PhotogrammetrySession.Outputs](photogrammetrysession/outputs-swift.property.md)
  Returns the outputs message stream which can be asynchronously iterated on.
- [PhotogrammetrySession.Output](photogrammetrysession/output.md)
  Status updates on the object-creation process.
### Controlling object creation
- [func process(requests: [PhotogrammetrySession.Request]) throws](photogrammetrysession/process(requests:).md)
  Starts processing of the provided processing `requests`.  Messages begin to be produced to the `output` publisher.
- [func cancel()](photogrammetrysession/cancel.md)
  Requests cancellation of any running requests.
### Creating requests
- [PhotogrammetrySession.Request](photogrammetrysession/request.md)
  An object that configures a photogrammetry session reconstruction request.
### Obtaining results
- [PhotogrammetrySession.Result](photogrammetrysession/result.md)
  An object that holds the created 3D object.
- [PhotogrammetrySession.PointCloud](photogrammetrysession/pointcloud.md)
  A sparse point cloud data structure output as the payload of a `.pointCloud` request. A point cloud is an array of `PointCloud.Point` instances.
- [PhotogrammetrySession.Error](photogrammetrysession/error.md)
  The errors that can occur during reconstruction in a photogrammetry session.
- [PhotogrammetrySession.Pose](photogrammetrysession/pose.md)
  A 6DOF pose relative to the estimated coordinate system.
- [PhotogrammetrySession.Poses](photogrammetrysession/poses.md)
  Once initial photogrammetric calculations are complete, a data structure mapping the sample ID (or index if a folder was used) to the 6DOF algorithmically estimated pose of that sample is returned.
### Structures
- [PhotogrammetrySession.Limits](photogrammetrysession/limits-swift.struct.md)
  Data structure to observe hardware limits for reconstruction.  Note that these are specific to the device on which the `PhotogrammetrySession` is run.
- [PhotogrammetrySession.Outputs](photogrammetrysession/outputs-swift.struct.md)
  An asynchronous sequence of session-related updates.
### Initializers
- [convenience(input:configuration:)](photogrammetrysession/init(input:configuration:).md)
  Creates a session from a specified directory of images.
### Type Properties
- [static let limits: PhotogrammetrySession.Limits](photogrammetrysession/limits-swift.type.property.md)
  Observer for the device-specific constant hardware limits for reconstruction.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [Capturing photographs for RealityKit Object Capture](capturing-photographs-for-realitykit-object-capture.md)
  Take high-quality images of objects to generate 3D models.
- [Creating 3D objects from photographs](creating-3d-objects-from-photographs.md)
  Construct virtual objects to use in your AR experiences.
- [Scanning objects using Object Capture](scanning-objects-using-object-capture.md)
  Implement a full scanning workflow for capturing objects on iOS devices.
- [Building an object reconstruction app](building-an-object-reconstruction-app.md)
  Reconstruct objects from user-selected input images by using photogrammetry.
- [Creating a Photogrammetry Command-Line App](creating_a_photogrammetry_command-line_app.md)
  Generate 3D objects from images using RealityKit Object Capture.
- [Using object capture assets in RealityKit](using_object_capture_assets_in_realitykit.md)
  Create a chess game using RealityKit and assets created using Object Capture.
- [struct PhotogrammetrySample](photogrammetrysample.md)
  An object that represents one image and its corresponding metadata.
- [struct ObjectCaptureView](objectcaptureview.md)
  A view that guides a user through capturing images for object capture.
- [class ObjectCaptureSession](objectcapturesession.md)
  A session object that monitors and controls image capture for photogrammetry.
- [struct ObjectCapturePointCloudView](objectcapturepointcloudview.md)
  Renders the current state of the point cloud from an object capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession)*