# Object capture

**Framework**: RealityKit

Create 3D objects from a series of photographs using photogrammetry.

#### Overview

In iOS 17 and macOS 12 and later, you can create 3D objects from photographs using a process called photogrammetry. You provide RealityKit Object Capture with a series of well-lit photographs taken from many different angles. It analyzes the overlap area between different images to match up landmarks and produces a 3D model of the photographed object.

## Topics

### Model creation
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
- [struct ObjectCaptureView](objectcaptureview.md)
  A view that guides a user through capturing images for object capture.
- [class ObjectCaptureSession](objectcapturesession.md)
  A session object that monitors and controls image capture for photogrammetry.
- [struct ObjectCapturePointCloudView](objectcapturepointcloudview.md)
  Renders the current state of the point cloud from an object capture session.

## See Also

- [Designing RealityKit content with Reality Composer Pro](../visionOS/designing-realitykit-content-with-reality-composer-pro.md)
  Design RealityKit scenes for your visionOS app.
- [Swift Splash](../visionOS/swift-splash.md)
  Use RealityKit to create an interactive ride in visionOS.
- [Diorama](../visionOS/diorama.md)
  Design scenes for your visionOS app using Reality Composer Pro.
- [Composing interactive 3D content with RealityKit and Reality Composer Pro](composing-interactive-3d-content-with-realitykit-and-reality-composer-pro.md)
  Build an interactive scene using an animation timeline.
- [Presenting an artist’s scene](presenting-an-artists-scene.md)
  Display a scene from Reality Composer Pro in visionOS.
- [Reality Composer](realitykit-reality-composer.md)
  A visual editor for RealityKit AR scenes.
- [USD Assets](realitykit-usd-assets.md)
  Import and use 3D scenes by importing USD files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realitykit-object-capture)*