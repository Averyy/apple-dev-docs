# ObjectCaptureView

**Framework**: RealityKit  
**Kind**: struct

A view that guides a user through capturing images for object capture.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
@preconcurrency struct ObjectCaptureView<Overlay> where Overlay : View
```

#### Overview

The primary view of the Object Capture front-end 3D UI.  This view is used to present the UI for a given [`ObjectCaptureSession`](objectcapturesession.md). It presents the current state of the wrapped session. The view can be taken down temporarily to show the [`ObjectCapturePointCloudView`](objectcapturepointcloudview.md) or an app’s custom tutorial pages. If a [`ObjectCaptureView`](objectcaptureview.md) is removed from the content view, creating a new [`ObjectCaptureView`](objectcaptureview.md) from the original view’s [`ObjectCaptureSession`](objectcapturesession.md) resumes the in-progress capture session.

## Topics

### Initializers
- [init(session: ObjectCaptureSession)](objectcaptureview/init(session:).md)
  Renders the current state of the provided session.
- [init(session: ObjectCaptureSession, cameraFeedOverlay: () -> Overlay)](objectcaptureview/init(session:camerafeedoverlay:).md)
  Renders the current state of the provided session.
### Instance Properties
- [var body: some View](objectcaptureview/body-swift.property.md)
  The content and behavior of the view.
### Instance Methods
- [func hideObjectReticle(Bool) -> ObjectCaptureView<Overlay>](objectcaptureview/hideobjectreticle(_:).md)
  Hides the object selection reticle when the session is in `.ready` state if set to true. Example: ObjectCaptureView(session: mySession) .hideObjectReticle()
### Type Aliases
- [ObjectCaptureView.Body](objectcaptureview/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](objectcaptureview/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

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
- [class PhotogrammetrySession](photogrammetrysession.md)
  Manages the creation of a 3D model from a set of images.
- [struct PhotogrammetrySample](photogrammetrysample.md)
  An object that represents one image and its corresponding metadata.
- [class ObjectCaptureSession](objectcapturesession.md)
  A session object that monitors and controls image capture for photogrammetry.
- [struct ObjectCapturePointCloudView](objectcapturepointcloudview.md)
  Renders the current state of the point cloud from an object capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcaptureview)*