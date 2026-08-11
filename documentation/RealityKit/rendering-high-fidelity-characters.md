# Rendering high-fidelity characters

**Framework**: RealityKit

Configure material and lighting properties to avoid flat, dull skin and static hair on your characters.

#### Overview

Rendering characters convincingly requires capturing how skin and hair scatter and reflect light, an effect flat shading fails to reproduce. Achieving that level of realism requires a combination of rendering techniques, including subsurface scattering and bent normals for skin, and a dedicated lighting model for hair.

To simulate subsurface scattering similar to skin absorbing and re-emitting light beneath an object’s surface, use [`PhysicallyBasedMaterial`](physicallybasedmaterial.md). The structure uses bent normals to capture how nearby geometry shapes indirect lighting and suppresses specular highlights in self-occluded areas. The [`HairLightingModel`](hairlightingmodel.md) structure provides a dedicated lighting mode for strand-based hair geometry. It accounts for how each strand reflects and transmits light as its angle to the light source changes.

These character rendering features deliver high-fidelity results but can be GPU-intensive when you combine them. Start by measuring which feature accounts for the largest share of that cost, then apply the targeted guidance in the following sections to keep overall thermal impact manageable on device.

#### Manage Bent Normals Cost

Bent normals store the average direction of least occlusion for each surface point. This gives [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) more accurate indirect lighting on characters and allows [`enableSpecularOcclusion`](physicallybasedmaterial/enablespecularocclusion.md) to suppress specular highlights in self-occluded areas. The cost of bent normals is one additional texture sample per fragment but you can reduce that overhead.

Bent normal influence on the final image is low-frequency. A half-resolution map with mipmapping enabled on the [`TextureResource`](textureresource.md) produces results that are visually indistinguishable from a full-resolution one at a fraction of the memory and sampling cost.

#### Manage Subsurface Scattering Cost

Subsurface scattering approximates how light diffuses in from nearby points on the skin. Although this requires more per-fragment sampling than a single-pass surface reflectance, there are several ways to mitigate the cost.

- **Scale subsurface weight by distance.** Reduce [`subsurfaceWeight`](physicallybasedmaterial/subsurfaceweight-swift.property.md) toward `0.0` for characters that are not the focal point of a scene. At low weights the subsurface pass contributes minimally to the final image but still incurs cost. Zeroing it out lets the renderer skip it entirely.
- **Use conservative subsurface radius values.** Large [`subsurfaceRadius`](physicallybasedmaterial/subsurfaceradius-swift.property.md) values widen the scattering kernel and increase per-fragment work. Use the smallest radius that still reads as realistic for the character’s skin tone.
- **Prefer lower-resolution subsurface maps.** Because subsurface scattering results are low-frequency by nature, subsurface color and radius textures tolerate aggressive downsampling. Use half or quarter resolution compared to your base color map, and enable mipmapping on the [`TextureResource`](textureresource.md).
- **Prefer a uniform color for subsurface if thermal budget is tight.** The [`subsurfaceColor`](physicallybasedmaterial/subsurfacecolor-swift.property.md) property accepts a single optional texture or a flat [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor). If you’re near the thermal limit, prefer a uniform color value over a texture to avoid the texture lookup entirely.
- **Limit the number of subsurface textures.** Subsurface scattering can sample multiple textures. If performance cost is high, use fewer textures to reduce the per-fragment sampling cost.

#### Manage Hair Rendering Cost

Hair rendering cost is driven by overdraw from layered hair cards or strands, geometry complexity, and per-fragment lighting calculations.

- **Minimize overlapping translucent hair layers.** Each layer of translucent geometry requires a separate pass through the fragment shader; reducing overlap directly reduces overdraw and per-fragment cost.
- **Use an opaque base layer for the scalp.** Rendering the scalp and inner hair mass as opaque geometry lets the depth buffer cull fragments behind it, reducing overdraw for the translucent layers above.
- **Prefer card-based hair over per-strand geometry.** Hair cards use a fraction of the triangle count of strand-based meshes, significantly reducing vertex processing and rasterization cost.
- **Fit card geometry tightly to the alpha silhouette.** Wide cards with large transparent borders force the GPU to shade pixels the alpha mask discards. Trimming card meshes to the visible hair shape avoids shading those invisible pixels.
- **Limit the lights and environment probes affecting the hair.** Each additional light source adds a full BSDF evaluation per fragment. Restrict how many lights overlap hair geometry and prefer a single baked environment probe where possible.
- **Keep hair vertex and triangle counts low.** Dense strand geometry increases vertex processing cost before shading even begins; use mesh simplification as aggressively as quality allows.
- **Use simpler hair materials for distant characters.** Background or distant characters don’t need the same material complexity as the focal character. Swap to a material with fewer textures, lower resolutions, and fewer layers at distance.
- **Use the lowest texture resolution that still looks acceptable.** Hair textures are often viewed at an angle and at distance, so they tolerate more aggressive downsampling than skin or clothing.
- **Pack multiple material channels into a single texture.** Combining properties such as roughness and specular into a single texture’s channels reduces the number of texture samples per fragment.
- **Prefer uniform values over textures for constant hair properties.** Parameters such as specular intensity, specular shifts, roughness, and backlight that are uniform across the hair mesh are cheaper to evaluate as material constants than as texture samples.

#### Measure the Cost of Each Effect

Each feature’s cost varies by scene, so measure before optimizing to focus your effort on the actual bottleneck.

Add the [`showStatistics`](arview/debugoptions-swift.struct/showstatistics.md) option to your view, as described in [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md), to confirm that your app is GPU limited. Then isolate each feature’s contribution by disabling it individually and comparing render thread time against your baseline measurement:

- To measure the cost of bent normals, temporarily disable [`enableSpecularOcclusion`](physicallybasedmaterial/enablespecularocclusion.md) and remove the bent normal texture.
- To measure the cost of subsurface scattering, set [`subsurfaceWeight`](physicallybasedmaterial/subsurfaceweight-swift.property.md) to `0.0` to isolate the pass as a whole. If it remains costly at a nonzero weight, measure its individual parameters next. Swap [`subsurfaceColor`](physicallybasedmaterial/subsurfacecolor-swift.property.md) between a texture and a flat color, or reduce [`subsurfaceRadius`](physicallybasedmaterial/subsurfaceradius-swift.property.md) to determine which one drives the cost.
- To measure the cost of hair rendering, temporarily hide the hair geometry, or swap it for a simplified stand-in mesh, and compare the difference.

#### Monitor Thermal State

Excessive GPU load from these effects causes noticeable frame drops and device heating. Monitor thermal state using [`thermalState`](https://developer.apple.com/documentation/Foundation/ProcessInfo/thermalState-swift.property) and the thermal state change notification, and reduce or turn off the most expensive character rendering features as the state moves from `.fair` toward `.serious` and `.critical`.

## See Also

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)
  Enhance the appearance of objects in a RealityKit scene with Physically Based Rendering (PBR).
- [Generating procedural textures](../visionOS/generating-procedural-textures-in-visionos.md)
  Display a 3D model that generates procedural textures in a reality view.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/rendering-high-fidelity-characters)*