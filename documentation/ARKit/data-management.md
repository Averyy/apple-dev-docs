# Data Management

**Framework**: ARKit

Obtain detailed information about skeletal and face geometry, and saved world data.

## Topics

### Body Data
- [Capturing Body Motion in 3D](capturing-body-motion-in-3d.md)
  Track a person in the physical environment and visualize their motion by applying the same body movements to a virtual character.
- [class ARBody2D](arbody2d.md)
  The screen-space representation of a person ARKit recognizes in the camera feed.
- [class ARSkeleton3D](arskeleton3d.md)
  The skeleton of a human body that ARKit tracks in 3D space.
- [class ARSkeleton2D](arskeleton2d.md)
  An object that describes the locations of a body’s joints in the camera feed.
- [class ARSkeleton](arskeleton.md)
  The interface for the skeleton of a tracked body.
- [class ARSkeletonDefinition](arskeletondefinition.md)
  The hierarchy of joints and their names.
### Face Data
- [Tracking and visualizing faces](tracking-and-visualizing-faces.md)
  Detect faces in a front-camera AR experience, overlay virtual content, and animate facial expressions in real-time.
- [Combining user face-tracking and world tracking](combining-user-face-tracking-and-world-tracking.md)
  Track the user’s face in an app that displays an AR experience with the rear camera.
- [class ARFaceGeometry](arfacegeometry.md)
  A 3D mesh describing face topology for use in face-tracking AR sessions.
- [class ARSCNFaceGeometry](arscnfacegeometry.md)
  A SceneKit representation of face topology for use with face information that an AR session provides.
### World Data
- [Saving and loading world data](saving-and-loading-world-data.md)
  Serialize a world-tracking session to resume it later on.
- [class ARWorldMap](arworldmap.md)
  The state in a world-tracking AR session during which a device maps the user’s position in physical space and proximity to anchor objects.

## See Also

- [Content Anchors](content-anchors.md)
  Identify items in the physical environment, including planar surfaces, images, physical objects, body positions, and faces.
- [Environmental Analysis](environmental-analysis.md)
  Analyze the video from the cameras and the accompanying data, and use ray-casting and depth-map information to determine the location of items.
- [Camera, Lighting, and Effects](camera-lighting-and-effects.md)
  Determine the camera position and lighting for the current session, and apply effects, such as occlusion, to elements of the environment.
- [Creating USD files for Apple devices](../RealityKit/creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/data-management)*