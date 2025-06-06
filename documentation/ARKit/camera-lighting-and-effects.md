# Camera, Lighting, and Effects

**Framework**: ARKit

Determine the camera position and lighting for the current session, and apply effects, such as occlusion, to elements of the environment.

## Topics

### Camera
- [class ARCamera](arcamera.md)
  Information about the camera position and imaging characteristics for a given frame.
### Lighting Effects
- [Adding realistic reflections to an AR experience](adding-realistic-reflections-to-an-ar-experience.md)
  Use ARKit to generate environment probe textures from camera imagery and render reflective virtual objects.
- [class AREnvironmentProbeAnchor](arenvironmentprobeanchor.md)
  An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.
- [class ARLightEstimate](arlightestimate.md)
  Estimated scene lighting information associated with a captured video frame in an AR session.
- [class ARDirectionalLightEstimate](ardirectionallightestimate.md)
  Estimated environmental lighting information associated with a captured video frame in a face-tracking AR session.
### Occlusion
- [Occluding virtual content with people](occluding-virtual-content-with-people.md)
  Cover your app’s virtual content with people that ARKit perceives in the camera feed.
- [Effecting People Occlusion in Custom Renderers](effecting-people-occlusion-in-custom-renderers.md)
  Occlude your app’s virtual content where ARKit recognizes people in the camera feed by using matte generator.
- [Visualizing and interacting with a reconstructed scene](visualizing-and-interacting-with-a-reconstructed-scene.md)
  Estimate the shape of the physical environment using a polygonal mesh.
- [class ARMatteGenerator](armattegenerator.md)
  An object that creates matte textures you use to occlude your app’s virtual content with people, that ARKit recognizes in the camera feed.

## See Also

- [Content Anchors](content-anchors.md)
  Identify items in the physical environment, including planar surfaces, images, physical objects, body positions, and faces.
- [Environmental Analysis](environmental-analysis.md)
  Analyze the video from the cameras and the accompanying data, and use ray-casting and depth-map information to determine the location of items.
- [Data Management](data-management.md)
  Obtain detailed information about skeletal and face geometry, and saved world data.
- [Creating USD files for Apple devices](../RealityKit/creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/camera-lighting-and-effects)*