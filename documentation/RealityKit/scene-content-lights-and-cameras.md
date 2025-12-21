# Lights and cameras

**Framework**: RealityKit

Control the lighting and point of view for a scene.

#### Overview

In RealityKit, cameras define the point of view from which RealityKit renders a scene. In AR mode, RealityKit creates and controls the camera for you based on the location and orientation of the device. In non-AR mode, you can control the camera by adding an entity that holds one of the camera components below and changing its [`Transform`](transform.md).

Lighting and shadows are an essential part of creating immersive and realistic experiences. You can craft dynamic and visually appealing environments that respond naturally to the viewer’s movement and other actions by strategically placing and configuring lights and cameras.

## Topics

### Cameras
- [struct PerspectiveCameraComponent](perspectivecameracomponent.md)
  A component that defines a virtual camera and its controls.
- [struct OrthographicCameraComponent](orthographiccameracomponent.md)
  A component that defines an orthographic virtual camera and its settings.
- [enum CameraFieldOfViewOrientation](camerafieldofvieworientation.md)
  The orientations that a camera’s field-of-view degrees can apply.
- [struct ProjectiveTransformCameraComponent](projectivetransformcameracomponent.md)
  A component that defines a virtual camera with a custom projection matrix.
- [class PerspectiveCamera](perspectivecamera.md)
  A virtual camera that establishes the rendering perspective.
### Point lights
- [struct PointLightComponent](pointlightcomponent.md)
  A component that defines a point light source.
### Directional lights and their shadows
- [struct DirectionalLightComponent](directionallightcomponent.md)
  A component that defines a directional light source.
- [DirectionalLightComponent.Shadow](directionallightcomponent/shadow.md)
  A directional light component that adds shadows to entities that it illuminates
- [DirectionalLightComponent.Shadow.ShadowProjectionType](directionallightcomponent/shadow/shadowprojectiontype.md)
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](directionallightcomponent/shadow/shadowmapcullmode.md)
### Spotlights and their shadows
- [struct SpotLightComponent](spotlightcomponent.md)
  A component that defines a spotlight source.
- [SpotLightComponent.Shadow](spotlightcomponent/shadow.md)
  A spotlight component that adds shadows to entities that it illuminates.
- [SpotLightComponent.Shadow.ShadowClippingPlane](spotlightcomponent/shadow/shadowclippingplane.md)
  An object that specifies the mode of a shadow clipping plane.
- [SpotLightComponent.Shadow.ShadowMapCullMode](spotlightcomponent/shadow/shadowmapcullmode.md)
### Image-based lights
- [struct ImageBasedLightComponent](imagebasedlightcomponent.md)
- [ImageBasedLightComponent.Source](imagebasedlightcomponent/source-swift.enum.md)
- [struct ImageBasedLightReceiverComponent](imagebasedlightreceivercomponent.md)
### General shadows
- [struct GroundingShadowComponent](groundingshadowcomponent.md)
  A component that controls an entity’s grounding shadow.
- [struct DynamicLightShadowComponent](dynamiclightshadowcomponent.md)
  A component that controls an entity’s shadow from dynamic (virtual) lights.
### Environment
- [class EnvironmentResource](environmentresource.md)
  An environmental resource that contains background and lighting information for a scene.
- [struct EnvironmentLightingConfigurationComponent](environmentlightingconfigurationcomponent.md)
  A component that scales the amount of light that an entity receives from its environment.
- [struct VirtualEnvironmentProbeComponent](virtualenvironmentprobecomponent.md)
  A component that provides environment lighting for entities you place within the same virtual world.
- [VirtualEnvironmentProbeComponent.Probe](virtualenvironmentprobecomponent/probe.md)
  A sample of the environment around a point in a scene the system uses for environment-based lighting.
- [VirtualEnvironmentProbeComponent.Source](virtualenvironmentprobecomponent/source-swift.enum.md)
  Options that define the source of diffuse and specular lighting for environment lighting calculations.
### Entity compliance
- [protocol HasPerspectiveCamera](hasperspectivecamera.md)
  An interface that enables you to configure a virtual camera that you can use to define the rendering perspective when you’re not in an AR session.
- [class PointLight](pointlight.md)
  An entity that produces an omnidirectional light for virtual objects.
- [protocol HasPointLight](haspointlight.md)
  An interface that defines a point light source component.
- [class SpotLight](spotlight.md)
  An entity that illuminates virtual content in a cone-shaped volume.
- [protocol HasSpotLight](hasspotlight.md)
  An interface that defines a spot light source component.
- [class DirectionalLight](directionallight.md)
  An entity that casts a virtual light in a particular direction.
- [protocol HasDirectionalLight](hasdirectionallight.md)
  An interface that defines a directional light source component.

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
- [Responding to gestures on an entity](responding-to-gestures-on-an-entity.md)
  Respond to gestures performed on RealityKit entities using input target and collision components.
- [Models and meshes](scene-content-models-and-meshes.md)
  Display virtual objects in your scene with mesh-based models.
- [Materials, textures, and shaders](scene-content-materials-and-shaders.md)
  Apply textures to the surface of your scene’s 3D objects to give each object a unique appearance.
- [Anchors](scene-content-anchors.md)
  Lock virtual content to the real world.
- [Content synchronization](scene-content-content-synchronization.md)
  Synchronize the contents of entities locally or across the network.
- [Audio](scene-content-audio.md)
  Create personalized and realistic spatial audio experiences.
- [Videos](scene-content-videos.md)
  Present videos in your RealityKit experiences.
- [Images](scene-content-images.md)
  Present images and spatial scenes in your RealityKit experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene-content-lights-and-cameras)*