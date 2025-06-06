# Understanding World Tracking

**Framework**: ARKit

Discover features and best practices for building rear-camera AR experiences.

#### Overview

The basic requirement for any AR experience—and the defining feature of ARKit—is the ability to create and track a correspondence between the real-world space the user inhabits and a virtual space where you can model visual content. When your app displays that content together with a live camera image, the user experiences augmented reality: the illusion that your virtual content is part of the real world.

![Illustration of an iPhone running an app that displays an AR experience using the rear camera. The physical environment is depicted as a living room with a couch, on which, the app displays a virtual character.](https://docs-assets.developer.apple.com/published/06a229139b82f0be0d378e910a318a8b/media-2909114%402x.png)

In all AR experiences, ARKit uses world and camera coordinate systems following a right-handed convention: the y-axis points upward, and (when relevant) the z-axis points toward the viewer and the x-axis points toward the viewer’s right.

Session configurations can change the origin and orientation of the coordinate system with respect to the real world (see [`worldAlignment`](arconfiguration/worldalignment-swift.property.md)). Each anchor in an AR session defines its own local coordinate system, also following the right-handed, z-towards-viewer convention;  for example, the [`ARFaceAnchor`](arfaceanchor.md) class defines a system for locating facial features.

##### Combine Motion Sensing and Scene Analysis

To create a correspondence between real and virtual spaces, ARKit uses a technique called . This process combines information from the iOS device’s motion sensing hardware with computer vision analysis of the scene visible to the device’s camera. ARKit recognizes notable features in the scene image, tracks differences in the positions of those features across video frames, and compares that information with motion sensing data. The result is a high-precision model of the device’s position and motion.

World tracking also analyzes and understands the contents of a scene. Use ray-casting methods (see `Raycasting and Hit-Testing`) to find real-world surfaces corresponding to a point in the camera image. If you enable the [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md) setting in your session configuration, ARKit detects flat surfaces in the camera image and reports their position and sizes. You can use ray-cast results or detected planes to place or interact with virtual content in your scene.

##### Craft an Exceptional Ar Experience

Although world tracking can produce realistic AR experiences with accuracy and precision, it relies on details of the device’s physical environment that are not always consistent and can be difficult to measure in real time without a degree of error. To build high-quality AR experiences, be aware of these caveats and tips.

 World tracking involves image analysis, which requires a clear image. Tracking quality is reduced when the camera can’t see details, such as when the camera is pointed at a blank wall or the scene is too dark.

. World tracking correlates image analysis with device motion. ARKit develops a better understanding of the scene if the device is moving, even if the device moves only subtly. Excessive motion—too far, too fast, or shaking too vigorously—results in a blurred image or too much distance for tracking features between video frames, reducing tracking quality. The [`ARCamera`](arcamera.md) class provides tracking state reason information, which you can use to develop UI that tells a user how to resolve low-quality tracking situations.

 Plane detection results vary over time—when a plane is first detected, its position and extent may be inaccurate. As the plane remains in the scene over time, ARKit refines its estimate of position and extent. When a large flat surface is in the scene, ARKit may continue changing the plane anchor’s position, extent, and transform after you’ve already used the plane to place content.

## See Also

- [class ARWorldTrackingConfiguration](arworldtrackingconfiguration.md)
  A configuration that tracks the position of a device in relation to objects in the environment.
- [class ARGeoTrackingConfiguration](argeotrackingconfiguration.md)
  A configuration that tracks locations with GPS, map data, and a device’s compass.
- [class AROrientationTrackingConfiguration](arorientationtrackingconfiguration.md)
  A configuration that tracks only the device’s orientation using the rear-facing camera.
- [class ARPositionalTrackingConfiguration](arpositionaltrackingconfiguration.md)
  A configuration that tracks only the device’s position in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/understanding-world-tracking)*