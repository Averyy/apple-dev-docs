# Anchors

**Framework**: RealityKit

Lock virtual content to the real world.

#### Overview

RealityKit anchors all entities in a scene to an anchor target in the same scene, such as the ground, an image, or a position relative to its parent view. RealityKit provides several types you can use as the target for your anchors.

## Topics

### Anchoring components
- [struct AnchoringComponent](anchoringcomponent.md)
  A component that anchors virtual content to a real world target.
- [AnchoringComponent.Target](anchoringcomponent/target-swift.enum.md)
  Defines the kinds of real world objects to which an anchor entity can be tethered.
- [struct ARKitAnchorComponent](arkitanchorcomponent.md)
- [class AnchorEntity](anchorentity.md)
  An anchor that tethers entities to a scene.
- [protocol HasAnchoring](hasanchoring.md)
  An interface that enables anchoring of virtual content to a real-world object in an AR scene.
### Surface anchor characterization
- [AnchoringComponent.Target.Alignment](anchoringcomponent/target-swift.enum/alignment.md)
  Defines the alignment of real-world surfaces to seek as targets.
- [AnchoringComponent.Target.Classification](anchoringcomponent/target-swift.enum/classification.md)
  Defines types of real-world surfaces to seek as targets.
### Hand tracking
- [Happy Beam](../visionOS/happybeam.md)
  Leverage a Full Space to create a fun game using ARKit.
- [AnchoringComponent.Target.HandLocation](anchoringcomponent/target-swift.enum/handlocation.md)
  Defines the locations of tracked hands to look for.
- [AnchoringComponent.Target.Chirality](anchoringcomponent/target-swift.enum/chirality.md)
  Defines the chirality of tracked hands to look for.
### Spatial tracking
- [class SpatialTrackingSession](spatialtrackingsession.md)
  An object that incorporates spatial tracking capabilities into your RealityKit apps.
- [SpatialTrackingSession.Configuration](spatialtrackingsession/configuration.md)
  A type for configuring the spatial tracking session.
- [SpatialTrackingSession.Configuration.AnchorCapability](spatialtrackingsession/configuration/anchorcapability.md)
  A type that defines various anchor tracking capabilities.
- [SpatialTrackingSession.Configuration.SceneUnderstandingCapability](spatialtrackingsession/configuration/sceneunderstandingcapability.md)
  Defines how system behaviors use scene understanding.
- [SpatialTrackingSession.Configuration.Camera](spatialtrackingsession/configuration/camera.md)
  Defines the camera feed the RealityView renders.
- [SpatialTrackingSession.UnavailableCapabilities](spatialtrackingsession/unavailablecapabilities.md)
  A type that contains the unavailable capabilities of the current spatial tracking session.
### Body and face tracking
- [Creating an App for Face-Painting in AR](creating-an-app-for-face-painting-in-ar.md)
  Combine RealityKit’s face detection with PencilKit to implement virtual face-painting.
- [Occluding virtual content with people](../ARKit/occluding-virtual-content-with-people.md)
  Cover your app’s virtual content with people that ARKit perceives in the camera feed.
- [struct BodyTrackingComponent](bodytrackingcomponent.md)
  A component for tracking people in an AR session.
- [class BodyTrackedEntity](bodytrackedentity.md)
  An entity used to animate a virtual character in an AR scene by tracking a real person.
- [protocol HasBodyTracking](hasbodytracking.md)
  An interface that enables the animation of a virtual character by tracking a real person in AR.
### Accessory tracking
- [Tracking a handheld accessory as a virtual sculpting tool](tracking-a-handheld-accessory-as-a-virtual-sculpting-tool.md)
  Use a tracked accessory with Apple Vision Pro to create a virtual sculpture.

## See Also

- [Hello World](../visionOS/World.md)
  Use windows, volumes, and immersive spaces to teach people about the Earth.
- [Enabling video reflections in an immersive environment](../visionOS/enabling-video-reflections-in-an-immersive-environment.md)
  Create a more immersive experience by adding video reflections in a custom environment.
- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Generating interactive geometry with RealityKit](generating-interactive-geometry-with-realitykit.md)
  Create an interactive mesh with low-level mesh and low-level texture.
- [Combining 2D and 3D views in an immersive app](combining-2d-and-3d-views-in-an-immersive-app.md)
  Use attachments to place 2D content relative to 3D content in your visionOS app.
- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [Presenting images in RealityKit](presenting-images-in-realitykit.md)
  Create and display spatial scenes in RealityKit.
- [Models and meshes](scene-content-models-and-meshes.md)
  Display virtual objects in your scene with mesh-based models.
- [Materials, textures, and shaders](scene-content-materials-and-shaders.md)
  Apply textures to the surface of your scene’s 3D objects to give each object a unique appearance.
- [Lights and cameras](scene-content-lights-and-cameras.md)
  Control the lighting and point of view for a scene.
- [Content synchronization](scene-content-content-synchronization.md)
  Synchronize the contents of entities locally or across the network.
- [Audio](scene-content-audio.md)
  Create personalized and realistic spatial audio experiences.
- [Videos](scene-content-videos.md)
  Present videos in your RealityKit experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene-content-anchors)*