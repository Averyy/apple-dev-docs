# Content Anchors

**Framework**: ARKit

Identify items in the physical environment, including planar surfaces, images, physical objects, body positions, and faces.

#### Overview

Anchors identify the position of items in your augmented reality session. Use anchors to obtain information about the item itself, or about the thing it represents. For example, use an [`ARPlaneAnchor`](arplaneanchor.md) to determine the location of a planar surface.

## Topics

### Surface Detection
- [Tracking and visualizing planes](tracking-and-visualizing-planes.md)
  Detect surfaces in the physical environment and visualize their shape and location in 3D space.
- [class ARPlaneAnchor](arplaneanchor.md)
  An anchor for a 2D planar surface that ARKit detects in the physical environment.
- [class ARMeshAnchor](armeshanchor.md)
  An anchor for a physical object that ARKit detects and recreates virtually using a polygonal mesh.
### Image Detection
- [Tracking and altering images](tracking-and-altering-images.md)
  Create images from rectangular shapes found in the user’s environment, and augment their appearance.
- [Detecting Images in an AR Experience](detecting-images-in-an-ar-experience.md)
  React to known 2D images in the user’s environment, and use their positions to place AR content.
- [class ARImageAnchor](arimageanchor.md)
  An anchor for a known image that ARKit detects in the physical environment.
- [class ARReferenceImage](arreferenceimage.md)
  A 2D image that you want ARKit to detect in the physical environment.
### Physical Objects
- [Visualizing and interacting with a reconstructed scene](visualizing-and-interacting-with-a-reconstructed-scene.md)
  Estimate the shape of the physical environment using a polygonal mesh.
- [Scanning and Detecting 3D Objects](scanning-and-detecting-3d-objects.md)
  Record spatial features of real-world objects, then use the results to find those objects in the user’s environment and trigger AR content.
- [class ARObjectAnchor](arobjectanchor.md)
  An anchor for a real-world 3D object that ARKit detects in the physical environment.
- [class ARReferenceObject](arreferenceobject.md)
  The description of a 3D object that you want ARKit to detect in the physical environment.
### Body Position Tracking
- [Capturing Body Motion in 3D](capturing-body-motion-in-3d.md)
  Track a person in the physical environment and visualize their motion by applying the same body movements to a virtual character.
- [Rigging a Model for Motion Capture](rigging-a-model-for-motion-capture.md)
  Configure custom 3D models so ARKit’s human body-tracking feature can control them.
- [Validating a Model for Motion Capture](validating-a-model-for-motion-capture.md)
  Verify that your character model matches ARKit’s Motion Capture requirements.
- [class ARBodyAnchor](arbodyanchor.md)
  An anchor that tracks the position and movement of a human body in the rear-facing camera.
### Face Tracking
- [Tracking and visualizing faces](tracking-and-visualizing-faces.md)
  Detect faces in a front-camera AR experience, overlay virtual content, and animate facial expressions in real-time.
- [Combining user face-tracking and world tracking](combining-user-face-tracking-and-world-tracking.md)
  Track the user’s face in an app that displays an AR experience with the rear camera.
- [class ARFaceAnchor](arfaceanchor.md)
  An anchor for a unique face that is visible in the front-facing camera.
### Geotracking
- [Tracking geographic locations in AR](tracking-geographic-locations-in-ar.md)
  Track specific geographic areas of interest and render them in an AR experience.
- [class ARGeoAnchor](argeoanchor.md)
  An anchor that identifies a geographic location using latitude, longitude, and altitude data.
### Multiuser Experiences
- [class ARParticipantAnchor](arparticipantanchor.md)
  An anchor for another user in multiuser augmented reality experiences.
### App Clip Codes
- [Interacting with App Clip Codes in AR](../AppClip/interacting-with-app-clip-codes-in-ar.md)
  Display content and provide services in an AR experience with App Clip Codes.
- [class ARAppClipCodeAnchor](arappclipcodeanchor.md)
  An anchor that tracks the position and orientation of an App Clip Code in the physical environment.
### Text Annotations
- [Creating screen annotations for objects in an AR experience](creating-screen-annotations-for-objects-in-an-ar-experience.md)
  Annotate an AR experience with virtual sticky notes that you display onscreen over real and virtual objects.
- [Recognizing and Labeling Arbitrary Objects](recognizing-and-labeling-arbitrary-objects.md)
  Create anchors that track objects you recognize in the camera feed, using a custom optical-recognition algorithm.
### Common Types
- [class ARAnchor](aranchor.md)
  An object that specifies the position and orientation of an item in the physical environment.
- [protocol ARAnchorCopying](aranchorcopying.md)
  Support for custom anchor subclasses.
- [protocol ARTrackable](artrackable.md)
  An interface for objects that track the location of real-world objects or locations.

## See Also

- [Environmental Analysis](environmental-analysis.md)
  Analyze the video from the cameras and the accompanying data, and use ray-casting and depth-map information to determine the location of items.
- [Camera, Lighting, and Effects](camera-lighting-and-effects.md)
  Determine the camera position and lighting for the current session, and apply effects, such as occlusion, to elements of the environment.
- [Data Management](data-management.md)
  Obtain detailed information about skeletal and face geometry, and saved world data.
- [Creating USD files for Apple devices](../USD/creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/content-anchors)*