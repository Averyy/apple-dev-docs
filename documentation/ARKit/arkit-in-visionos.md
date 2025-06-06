# ARKit in visionOS

**Framework**: ARKit

Create immersive augmented reality experiences.

#### Overview

ARKit in visionOS offers a new set of sensing capabilities that you adopt individually in your app, using data providers to deliver updates asynchronously. The available capabilities include:

-  Detect surfaces in a person’s surroundings and use them to anchor content.
-  Determine the position and orientation of Apple Vision Pro relative to its surroundings, and add world anchors to place content.
-  Use a person’s hand and finger positions as input for custom gestures and interactivity.
-  Build a mesh of a person’s physical surroundings and incorporate it into your immersive spaces to support interactions.
-  Look for known images in a person’s surroundings and use them as anchor points for custom content.
-  Use 3D reference objects to find and track real-world objects in a person’s environment.
-  Detect and scan QR codes and barcodes in a variety of formats in a person’s surroundings.
- . Use room anchors to identify specific rooms and implement per-room experiences.
-  Understand the lighting characteristics of a room to help improve the appearance of shiny or semi-reflective materials in your virtual content.
-  Access camera frames from a device in several formats.

![An illustration showing a split view of someone using Apple Vision Pro; the left side shows a person’s perspective of the room and the right side depicts ARKit’s perspective of the room. The right side illustrates ARKit’s sensing capabilities, including the detected shape of the room and the individual joints of a person’s hand.](https://docs-assets.developer.apple.com/published/b1742d9029cfb818bd01ad8d395b7e7d/media-4330791%402x.png)

## Topics

### Setup
- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [class ARKitSession](arkitsession.md)
  The main entry point for receiving data from ARKit.
- [protocol DataProvider](dataprovider.md)
  A source of live data from ARKit.
- [enum DataProviderState](dataproviderstate.md)
  The possible states of a data provider.
- [protocol Anchor](anchor.md)
  The identity, location, and orientation of an object in world space.
- [protocol TrackableAnchor](trackableanchor.md)
  An anchor that can gain and lose its tracking state over the course of a session.
### Barcode detection
- [class BarcodeDetectionProvider](barcodedetectionprovider.md)
  An object that provides the real-time position of barcodes the framework detects in a person’s environment.
- [struct BarcodeAnchor](barcodeanchor.md)
  A barcode’s position in a person’s surroundings.
### Camera sampling
- [class CameraFrameProvider](cameraframeprovider.md)
  An object that provides camera streams.
- [struct CameraFrame](cameraframe.md)
  The representation of a camera frame.
- [struct CameraVideoFormat](cameravideoformat.md)
  A structure that represents a camera video format.
### Plane detection
- [Placing content on detected planes](../visionOS/placing-content-on-detected-planes.md)
  Detect horizontal surfaces like tables and floors, as well as vertical planes like walls and doors.
- [class PlaneDetectionProvider](planedetectionprovider.md)
  A source of live data about planes in a person’s surroundings.
- [struct PlaneAnchor](planeanchor.md)
  An anchor that represents horizontal and vertical planes.
### World tracking
- [Tracking specific points in world space](../visionOS/tracking-points-in-world-space.md)
  Retrieve the position and orientation of anchors your app stores in ARKit.
- [class WorldTrackingProvider](worldtrackingprovider.md)
  A source of live data about the device pose and anchors in a person’s surroundings.
- [struct WorldAnchor](worldanchor.md)
  A fixed location in a person’s surroundings.
- [struct DeviceAnchor](deviceanchor.md)
  The position and orientation of Apple Vision Pro.
### Hand tracking
- [Happy Beam](../visionOS/happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [class HandTrackingProvider](handtrackingprovider.md)
  A source of live data about the position of a person’s hands and hand joints.
- [struct HandAnchor](handanchor.md)
  A hand’s position in a person’s surroundings.
- [struct HandSkeleton](handskeleton.md)
  A collection of joints in a hand.
### Scene reconstruction
- [Incorporating real-world surroundings in an immersive experience](../visionOS/incorporating-real-world-surroundings-in-an-immersive-experience.md)
  Create an immersive experience by making your app’s content respond to the local shape of the world.
- [class SceneReconstructionProvider](scenereconstructionprovider.md)
  A source of live data about the shape of a person’s surroundings.
- [struct MeshAnchor](meshanchor.md)
  A volume of space that contains a mesh of a person’s surroundings.
### Image tracking
- [Tracking and altering images](tracking-and-altering-images.md)
  Create images from rectangular shapes found in the user’s environment, and augment their appearance.
- [Detecting Images in an AR Experience](detecting-images-in-an-ar-experience.md)
  React to known 2D images in the user’s environment, and use their positions to place AR content.
- [Tracking preregistered images in 3D space](../visionOS/tracking-images-in-3d-space.md)
  Place content based on the current position of a known image in a person’s surroundings.
- [class ImageTrackingProvider](imagetrackingprovider.md)
  A source of live data about a 2D image’s position in a person’s surroundings.
- [struct ImageAnchor](imageanchor.md)
  A 2D image’s position in a person’s surroundings.
- [struct ReferenceImage](referenceimage.md)
  A 2D image the system uses as a reference to find the same image in a person’s surroundings.
### Geometry
- [struct GeometryElement](geometryelement.md)
  A container for vertex indices of lines or triangles.
- [struct GeometrySource](geometrysource.md)
  A container for geometrical vector data.
### Lighting estimation
- [class EnvironmentLightEstimationProvider](environmentlightestimationprovider.md)
  A source of live data about lighting information in the environment.
- [struct EnvironmentProbeAnchor](environmentprobeanchor.md)
  An environment probe in the world.
### Object tracking
- [class ObjectTrackingProvider](objecttrackingprovider.md)
  A source of real-time position of reference objects in a person’s environment.
- [struct ObjectAnchor](objectanchor.md)
  A reference object ARKit is tracking.
- [Exploring object tracking with ARKit](../visionOS/exploring_object_tracking_with_arkit.md)
  Find and track real-world objects in visionOS using reference objects trained with Create ML.
- [Implementing object tracking in your visionOS app](../visionOS/implementing-object-tracking-in-your-visionOS-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in your app.
### Room tracking
- [class RoomTrackingProvider](roomtrackingprovider.md)
  A source of real-time information about the room that a person is currently in.
- [struct RoomAnchor](roomanchor.md)
  The representation of a room ARKit is currently tracking.
- [Building local experiences with room tracking](../visionOS/building_local_experiences_with_room_tracking.md)
  Use room tracking in visionOS to provide custom interactions with physical spaces.

## See Also

- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [class ARKitSession](arkitsession.md)
  The main entry point for receiving data from ARKit.
- [protocol DataProvider](dataprovider.md)
  A source of live data from ARKit.
- [protocol Anchor](anchor.md)
  The identity, location, and orientation of an object in world space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkit-in-visionos)*