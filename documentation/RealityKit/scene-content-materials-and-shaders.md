# Materials, textures, and shaders

**Framework**: RealityKit

Apply textures to the surface of your scene’s 3D objects to give each object a unique appearance.

#### Overview

Materials define the appearance of 3D models in RealityKit, by defining how their surfaces interact with light. Materials can also occlude objects behind them, hold shaders, or act as portals to view other worlds with [`PortalMaterial`](portalmaterial.md).

RealityKit includes a few material types to help you get started, including [`SimpleMaterial`](simplematerial.md) for basic color and textures, and [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) for realistic lighting effects such as reflections, roughness, and emission.

## Topics

### Simple materials
- [struct SimpleMaterial](simplematerial.md)
  A basic material that responds to lights in the scene.
- [SimpleMaterial.BaseColor](simplematerial/basecolor-swift.typealias.md)
  The type used to represent base color.
- [SimpleMaterial.Texture](simplematerial/texture.md)
  The type used to represent textures.
- [SimpleMaterial.FaceCulling](simplematerial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [SimpleMaterial.TriangleFillMode](simplematerial/trianglefillmode-swift.typealias.md)
### Unlit materials
- [struct UnlitMaterial](unlitmaterial.md)
  A material that doesn’t respond to lights in the scene.
- [UnlitMaterial.BaseColor](unlitmaterial/basecolor-swift.typealias.md)
  The type used to represent base color.
- [UnlitMaterial.Blending](unlitmaterial/blending-swift.typealias.md)
  The type used to represent opacity information.
- [UnlitMaterial.Texture](unlitmaterial/texture.md)
  The type used to represent textures.
- [UnlitMaterial.FaceCulling](unlitmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [UnlitMaterial.TextureCoordinateTransform](unlitmaterial/texturecoordinatetransform-swift.typealias.md)
  An alias for the texture coordinate transform that’s appropriate for this material class.
- [UnlitMaterial.TriangleFillMode](unlitmaterial/trianglefillmode-swift.typealias.md)
### Realistic materials
- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)
  Enhance the appearance of objects in a RealityKit scene with Physically Based Rendering (PBR).
- [struct PhysicallyBasedMaterial](physicallybasedmaterial.md)
  A material that simulates the appearance of real-world objects.
- [PhysicallyBasedMaterial.BaseColor](physicallybasedmaterial/basecolor-swift.struct.md)
  An object that defines an entity’s base color.
- [PhysicallyBasedMaterial.Roughness](physicallybasedmaterial/roughness-swift.struct.md)
  An object that defines the roughness of an entity’s surface.
- [PhysicallyBasedMaterial.Metallic](physicallybasedmaterial/metallic-swift.struct.md)
  An object that defines the reflectiveness of an entity.
- [PhysicallyBasedMaterial.Normal](physicallybasedmaterial/normal-swift.struct.md)
  An object that specifies an entity’s normal map.
- [PhysicallyBasedMaterial.Blending](physicallybasedmaterial/blending-swift.enum.md)
  The object that defines the transparency of an entity.
- [PhysicallyBasedMaterial.AmbientOcclusion](physicallybasedmaterial/ambientocclusion-swift.struct.md)
  An object that defines the ambient occlusion of an entity’s surface.
- [PhysicallyBasedMaterial.Specular](physicallybasedmaterial/specular-swift.struct.md)
  An object that defines the specular highlights of an entity.
- [PhysicallyBasedMaterial.SheenColor](physicallybasedmaterial/sheencolor.md)
  An object that defines the color of an entity’s sheen.
- [PhysicallyBasedMaterial.Clearcoat](physicallybasedmaterial/clearcoat-swift.struct.md)
  An object that defines the intensity of an entity’s clear, shiny coating.
- [PhysicallyBasedMaterial.ClearcoatRoughness](physicallybasedmaterial/clearcoatroughness-swift.struct.md)
  An object that defines the degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [PhysicallyBasedMaterial.AnisotropyLevel](physicallybasedmaterial/anisotropylevel-swift.struct.md)
  An object that defines the degree to which an entity reflects light to create stretched or oblong highlights.
- [PhysicallyBasedMaterial.AnisotropyAngle](physicallybasedmaterial/anisotropyangle-swift.struct.md)
  An object used to define a material’s anisotropy angle.
- [PhysicallyBasedMaterial.EmissiveColor](physicallybasedmaterial/emissivecolor-swift.struct.md)
  An object that defines the color of the light an entity emits.
- [PhysicallyBasedMaterial.TextureCoordinateTransform](physicallybasedmaterial/texturecoordinatetransform-swift.typealias.md)
  An alias for the texture coordinate transform that’s appropriate for this material class.
- [PhysicallyBasedMaterial.FaceCulling](physicallybasedmaterial/faceculling-swift.typealias.md)
  An alias for the face culling object that’s appropriate for this material class.
- [PhysicallyBasedMaterial.Texture](physicallybasedmaterial/texture.md)
  The texture type to use for materials of this class.
### Portals
- [struct PortalMaterial](portalmaterial.md)
  A material that makes the mesh part a portal to a different world.
- [PortalMaterial.FaceCulling](portalmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [PortalMaterial.TriangleFillMode](portalmaterial/trianglefillmode-swift.typealias.md)
  An alias for the triangle fill mode object that’s appropriate for this material class.
- [struct PortalComponent](portalcomponent.md)
  A component that turns mesh surfaces into portals to a different world.
- [struct WorldComponent](worldcomponent.md)
  A component that defines a portal world.
- [struct PortalCrossingComponent](portalcrossingcomponent.md)
  A component that allows entities to cross portal boundaries.
### Texture resources
- [class TextureResource](textureresource.md)
  A representation of a texture.
- [TextureResource.CreateOptions](textureresource/createoptions.md)
  An object that holds texture resource creation options.
- [TextureResource.SamplingQuality](textureresource/samplingquality.md)
  An object for controlling the texture-sampling quality.
- [TextureResource.MipmapsMode](textureresource/mipmapsmode.md)
  An enumeration for specifying how to allocate and generate mipmaps for a texture.
- [TextureResource.Semantic](textureresource/semantic-swift.enum.md)
  An object for specifying the intended use of a texture.
### Texture drawing
- [Rendering a windowed game in stereo](rendering-a-windowed-game-in-stereo.md)
  Bring an iOS or iPadOS game to visionOS and enhance it.
- [Creating a dynamic height and normal map with low-level texture](creating-a-dynamic-height-map-with-low-level-texture.md)
  Create a low-level texture and update its pixel data on the GPU to form a dynamic height and normal map.
- [class LowLevelTexture](lowleveltexture.md)
  A container for texture data allowing you to create and update textures using your own format.
- [LowLevelTexture.Descriptor](lowleveltexture/descriptor-swift.struct.md)
  An object that you use to configure new `LowLevelTexture` objects.
- [TextureResource.Drawable](textureresource/drawable.md)
  A drawable associated with a drawable queue
- [TextureResource.DrawableQueue](textureresource/drawablequeue-swift.class.md)
  A drawable queue that may be used to update a texture resource dynamically
- [TextureResource.DrawableQueue.Descriptor](textureresource/drawablequeue-swift.class/descriptor.md)
  Describes the texture managed by the drawable queue
### Shaders
- [struct ShaderGraphMaterial](shadergraphmaterial.md)
  A material that comes from a shader graph in a Reality Composer Pro project, or a MaterialX shader.
- [ShaderGraphMaterial.FaceCulling](shadergraphmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [ShaderGraphMaterial.TriangleFillMode](shadergraphmaterial/trianglefillmode-swift.typealias.md)
  An alias for the triangle fill mode object that’s appropriate for this material class.
- [Modifying RealityKit rendering using custom materials](modifying-realitykit-rendering-using-custom-materials.md)
  Write Metal shader functions to implement custom rendering effects.
- [struct CustomMaterial](custommaterial.md)
  A material that works with custom Metal shader functions.
- [CustomMaterial.SurfaceShader](custommaterial/surfaceshader.md)
  The custom material’s surface shader function.
- [CustomMaterial.GeometryModifier](custommaterial/geometrymodifier.md)
  The custom material’s optional shader function that can manipulate an entity’s vertex data.
- [protocol MaterialFunction](materialfunction.md)
  The abstract superclass for objects representing compute functions for RealityKit custom materials .
- [CustomMaterial.Program](custommaterial/program-swift.class.md)
  An object that represents the backing shader compilation required for custom materials.
- [CustomMaterial.Program.Descriptor](custommaterial/program-swift.class/descriptor-swift.struct.md)
  An object that specifies all parameters necessary to initialize `CustomMaterial` programs
- [enum CustomShaderStage](customshaderstage.md)
### Object occlusion
- [struct OcclusionMaterial](occlusionmaterial.md)
  An invisible material that hides objects rendered behind it.
- [OcclusionMaterial.FaceCulling](occlusionmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
### Video materials
- [struct VideoMaterial](videomaterial.md)
  A material that supports animated textures.
- [VideoMaterial.FaceCulling](videomaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [VideoMaterial.TriangleFillMode](videomaterial/trianglefillmode-swift.typealias.md)
### Custom material types
- [CustomMaterial.Custom](custommaterial/custom-swift.struct.md)
  An object that defines the custom properties for the material.
- [CustomMaterial.CustomMaterialTexture](custommaterial/custommaterialtexture.md)
  A texture object that you use to create custom materials.
- [CustomMaterial.LightingModel](custommaterial/lightingmodel-swift.enum.md)
  An object that defines how the framework renders a custom material.
- [CustomMaterial.BaseColor](custommaterial/basecolor-swift.struct.md)
  An object that defines an entity’s base color.
- [CustomMaterial.Roughness](custommaterial/roughness-swift.struct.md)
  An object that defines how the surface of an entity scatters the light it reflects.
- [CustomMaterial.Metallic](custommaterial/metallic-swift.struct.md)
  An object that defines an entity’s reflectiveness.
- [CustomMaterial.Normal](custommaterial/normal-swift.struct.md)
  An object that stores fine surface details for an entity in an image texture.
- [CustomMaterial.EmissiveColor](custommaterial/emissivecolor-swift.struct.md)
  An object that defines the color of the light an entity emits.
- [CustomMaterial.Blending](custommaterial/blending-swift.enum.md)
  An object that specifies the transparency of an entity.
- [CustomMaterial.Opacity](custommaterial/opacity.md)
  An object that defines the transparency options for a custom material.
- [CustomMaterial.AmbientOcclusion](custommaterial/ambientocclusion-swift.struct.md)
  An object that defines an entity’s exposure to ambient light.
- [CustomMaterial.Specular](custommaterial/specular-swift.struct.md)
  An object that defines the specular highlights of an entity.
- [CustomMaterial.Clearcoat](custommaterial/clearcoat-swift.struct.md)
  An object that defines the intensity of an entity’s clear, shiny coating.
- [CustomMaterial.ClearcoatNormal](custommaterial/clearcoatnormal-swift.struct.md)
  An object that defines the clearcoat normal map texture.
- [CustomMaterial.ResourceStorage](custommaterial/resourcestorage.md)
  A container for resources that will be encoded into a CustomMaterial’s custom uniforms argument buffer.
- [CustomMaterial.TextureCoordinateTransform](custommaterial/texturecoordinatetransform-swift.typealias.md)
  The object type that custom material use to hold UV texture coordinates.
- [CustomMaterial.FaceCulling](custommaterial/faceculling-swift.typealias.md)
  The type of object used to control the removal of polygons that aren’t visible to the user.
- [CustomMaterial.Texture](custommaterial/texture.md)
  The object type that custom materials use to hold texture properties.
### Error types
- [enum CustomMaterialError](custommaterialerror.md)
  Errors generated when loading custom material functions.
### Material types
- [protocol Material](material.md)
  A type that describes the material aspects of a mesh, like color and texture.
- [typealias Color](material/color.md)
  An alias for the color type that’s appropriate for the current platform.
- [typealias Parameters](material/parameters.md)
  The parameter type that custom materials uses for properties the framework passes to shader functions.
- [struct MaterialParameterTypes](materialparametertypes.md)
  A set of types that material parameters can use.
- [struct MaterialParameters](materialparameters.md)
- [enum MaterialColorParameter](materialcolorparameter.md)
  The color parameter applied to a material.
- [enum MaterialScalarParameter](materialscalarparameter.md)
  The scalar parameter applied to a material.

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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene-content-materials-and-shaders)*