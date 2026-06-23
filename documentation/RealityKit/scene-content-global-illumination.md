# Global illumination and baked lighting

**Framework**: RealityKit

Light scenes realistically by precomputing illumination so surfaces pick up bounced color and ambient detail without recalculating it every frame.

#### Overview

This collection gathers the tools for adding precomputed and environment-based lighting to your scenes. Use it to choose how surfaces respond to light, to bake static illumination and capture indirect light that nearby objects can sample, and to generate the surrounding imagery that lights a scene and fills its background. Reach for these features when you want richer, more believable lighting than real-time computation alone provides, while keeping rendering efficient. They suit scenes with mostly fixed lighting, where investing in precomputation pays off in visual quality and performance.

## Topics

### Lighting models
- [enum LightingModel](lightingmodel.md)
  The lighting model used by a [`ShaderGraphMaterial.Program`](shadergraphmaterial/program-swift.struct.md).
- [struct LitLightingModel](litlightingmodel.md)
  Configuration for RealityKit’s physically based lighting model.
- [struct UnlitLightingModel](unlitlightingmodel.md)
  Configuration for an unlit lighting model, which renders without any light interaction.
- [struct HairLightingModel](hairlightingmodel.md)
  Configuration for RealityKit’s hair lighting model.
### Lightmaps and light probes
- [class LightmapResource](lightmapresource.md)
  A resource containing references to lightmap texture atlases and descriptions of how parts of the atlases map to meshes in the scene. At a high level, this resource comprises two parts:
- [struct LightmapComponent](lightmapcomponent.md)
- [class DiffuseProbeResource](diffuseproberesource.md)
  A resource containing baked diffuse lighting data organized as a tetrahedral probe mesh.
- [struct DiffuseLightProbeGroupComponent](diffuselightprobegroupcomponent.md)
  A component that stores diffuse probe data for a spatial region.
- [struct DiffuseLightProbeReceiverComponent](diffuselightprobereceivercomponent.md)
  A component that receives diffuse lighting from a referenced probe group.
### Environment texture generation
- [class ImageBasedLightTextureGenerator](imagebasedlighttexturegenerator.md)
  An object that generates image-based-lighting diffuse and specular cube textures from a skybox.
- [class SkyboxGenerator](skyboxgenerator.md)
  An object that generates a skybox cube texture from an equirectangular source.
- [enum TextureSamplingQuality](texturesamplingquality.md)
  A discrete trade-off between generation time and texture quality, used by [`SkyboxGenerator`](skyboxgenerator.md) and [`ImageBasedLightTextureGenerator`](imagebasedlighttexturegenerator.md).

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
- [Lights and cameras](scene-content-lights-and-cameras.md)
  Control the lighting and point of view for a scene.
- [Content synchronization](scene-content-content-synchronization.md)
  Synchronize the contents of entities locally or across the network.
- [Audio](scene-content-audio.md)
  Create personalized and realistic spatial audio experiences.
- [Videos](scene-content-videos.md)
  Present videos in your RealityKit experiences.
- [Images](scene-content-images.md)
  Present images and spatial scenes in your RealityKit experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene-content-global-illumination)*