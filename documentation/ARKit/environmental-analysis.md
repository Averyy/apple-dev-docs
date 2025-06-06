# Environmental Analysis

**Framework**: ARKit

Analyze the video from the cameras and the accompanying data, and use ray-casting and depth-map information to determine the location of items.

## Topics

### Video Frame Analysis
- [Displaying a point cloud using scene depth](displaying-a-point-cloud-using-scene-depth.md)
  Present a visualization of the physical environment by placing points based a scene’s depth data.
- [Creating a fog effect using scene depth](creating-a-fog-effect-using-scene-depth.md)
  Apply virtual fog to the physical environment.
- [class ARFrame](arframe.md)
  A video image captured as part of a session with position-tracking information.
- [class ARPointCloud](arpointcloud.md)
  A collection of points in the world coordinate space of the AR session.
- [class ARDepthData](ardepthdata.md)
  An object that describes the distance to regions of the real world from the plane of the camera.
### Raycasting
- [Placing objects and handling 3D interaction](placing-objects-and-handling-3d-interaction.md)
  Place virtual content at tracked, real-world locations, and enable the user to interact with virtual content by using gestures.
- [class ARRaycastQuery](arraycastquery.md)
  A mathematical ray you use to find 3D positions on real-world surfaces.
- [class ARTrackedRaycast](artrackedraycast.md)
  A raycast query that ARKit repeats in succession to give you refined results over time.
- [class ARRaycastResult](arraycastresult.md)
  Information about a real-world surface found by examining a point on the screen.
### Hit-Testing
- [class ARHitTestResult](arhittestresult.md)
  Information about a real-world surface found by examining a point on the screen.

## See Also

- [Content Anchors](content-anchors.md)
  Identify items in the physical environment, including planar surfaces, images, physical objects, body positions, and faces.
- [Camera, Lighting, and Effects](camera-lighting-and-effects.md)
  Determine the camera position and lighting for the current session, and apply effects, such as occlusion, to elements of the environment.
- [Data Management](data-management.md)
  Obtain detailed information about skeletal and face geometry, and saved world data.
- [Creating USD files for Apple devices](../RealityKit/creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/environmental-analysis)*