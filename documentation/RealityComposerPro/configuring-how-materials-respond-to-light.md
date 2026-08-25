# Configuring how materials respond to light

**Framework**: Reality Composer Pro

Match how a material reacts to the lights in a scene.

#### Overview

A scene’s final appearance depends on both the lights you place in the scene and how the materials in that scene respond to them. Lights control the direction, strength, and sources of your lighting, and you choose a material’s Shader type (see [`Building materials in Reality Composer Pro`](building-materials-in-reality-composer-pro.md)) to define whether a surface responds to that light at all. Portal materials skip lighting calculations entirely, because they reveal a different scene through a boundary instead of shading a surface. This article describes how to configure material lighting properties and how they interact with the lighting in your scene. To learn about the different types of lights, how to place and configure them, and how to configure Light Layers to control scene lighting, see [`Lighting a scene with lights and light layers`](lighting-a-scene-with-lights-and-light-layers.md).

![A screenshot of a Reality Composer Pro 3 scene with an object selected and its material and light layer properties showing in the Inspector.](/images/RealityComposerPro/LightingMaterialExample1@2x.png)

#### Match a Materials Shader Type to Its Lighting Response

Every material in Reality Composer Pro has a Shader type in the Inspector, and the value you choose there is the single biggest factor in whether that material responds to the lights you just placed. Think of the five available Shader types as a decision table for lighting behavior: Portal (described in the [`Overview`](configuring-how-materials-respond-to-light#Overview.md)), Physically Based, Unlit, [`Use Occlusion materials to hide content and control light`](configuring-how-materials-respond-to-light#Use-Occlusion-materials-to-hide-content-and-control-light.md), and [`Use Shader Graph materials to customize lighting`](configuring-how-materials-respond-to-light#Use-Shader-Graph-materials-to-customize-lighting.md).

#### Use Physically Based Materials for Realistic Lighting

Physically Based materials interact naturally with all scene lighting through accurate physical shading models, making them the right choice whenever you want a surface to react realistically to your lights. See [`PhysicallyBasedMaterial`](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial) for more information.

#### Use Unlit Materials to Ignore Lighting Altogether

Unlit materials are unaffected by scene lighting, consistently rendering their raw, unshaded color. Reach for them when you want a surface’s appearance to stay constant regardless of lighting, as in user interface elements or emissive surfaces. See [`UnlitMaterial`](https://developer.apple.com/documentation/realitykit/unlitmaterial) for more information.

#### Use Occlusion Materials to Hide Content and Control Light

Occlusion materials render as invisible while still occluding geometry behind them. You can use them to hide virtual content. For example, if an object has an Occlusion material on it and the object is in front of virtual content, both the Occlusion material and everything behind it disappear from view. The viewer sees passthrough video for those pixels. Use Occlusion materials when you want “real” objects to interact with virtual content realistically. Selecting Occlusion as the Shader removes all PBR controls from the Inspector, leaving only Face Culling. Developers typically use Occlusion materials in passthrough AR to mask real-world objects so virtual objects appear to render behind them. Reality Composer Pro offers two Shader Graph node variants for Occlusion, each with different lighting behavior: the Occlusion Surface (RealityKit) node doesn’t receive dynamic lighting, while the Shadow Receiving Occlusion Surface (RealityKit) node does. See [`OcclusionMaterial`](https://developer.apple.com/documentation/realitykit/occlusionmaterial) and its [`receivesDynamicLighting`](https://developer.apple.com/documentation/realitykit/occlusionmaterial/receivesdynamiclighting) property for more information.

#### Use Shader Graph Materials to Customize Lighting

Shader Graph materials are the custom option: you choose the lighting response explicitly instead of relying on a fixed default baked into the material type. Every Shader Graph material has a Lighting Model property, part of the material’s Descriptor. It has four possible values: Unspecified, Lit, Unlit, and Hair.

- Unspecified lets RealityKit infer the lighting model from the surface output node in the graph.
- Lit gives the graph the same physically based shading as the Physically Based material type. In addition, if you choose Lit, further sub-properties like Diffuse Model and Specular Model give you finer control over how the material scatters and reflects light, but the defaults work well for most surfaces.
- Unlit gives the graph the same raw-color behavior as the Unlit material type
- Hair applies anisotropic shading tuned for strand-like geometry. See [`Designing materials with Shader Graph`](designing-materials-with-shader-graph.md) and [`ShaderGraphMaterial`](https://developer.apple.com/documentation/realitykit/shadergraphmaterial) for more information.

> ❗ **Important**: The Lighting Model must agree with the graph’s actual surface output node. If you set Lighting Model to Lit but wire up an unlit surface output — or the reverse — Reality Composer Pro treats the surface output node as the source of truth and ignores the conflicting Lighting Model selection, so keep the two in sync.

#### Consume Indirect and Environment Lighting in a Material

The same Shader type decision described in the previous sections gates indirect and environment lighting. The [`receivesDynamicLighting`](https://developer.apple.com/documentation/realitykit/occlusionmaterial/receivesdynamiclighting) setting also lets an Occlusion material receive dynamic lighting and shadows from scene light sources while remaining invisible. Physically Based materials and Lit Shader Graph materials fold indirect lighting into the same PBR shading math used for direct light, acting as another contributing input and not a separate calculation. For a Lit material, RealityKit supplies indirect lighting from two sources: an [`ImageBasedLightComponent`](https://developer.apple.com/documentation/realitykit/imagebasedlightcomponent) and a Virtual Environment Probe. An [`ImageBasedLightComponent`](https://developer.apple.com/documentation/realitykit/imagebasedlightcomponent) supplies indirect lighting to entities that also carry an [`ImageBasedLightReceiverComponent`](https://developer.apple.com/documentation/realitykit/imagebasedlightreceivercomponent) pointing back at the source entity. See [`Lighting a scene with lights and light layers`](lighting-a-scene-with-lights-and-light-layers.md) for more information about Virtual Environment Probes and Image Based Light Components. Once indirect light reaches a surface, doc://com.apple.documentation/documentation/realitykit/PhysicallyBasedMaterial/ambientOcclusion controls how much of it the surface actually receives, simulating the soft shadowing that occurs in surface crevices by attenuating ambient light reception.

> 💡 **Tip**: For a Lit Shader Graph material, the Lighting Model’s Descriptor exposes a related Apply Bent Normal setting with three states. This setting lets the graph supply a bent normal — a normal direction shifted away from occluded regions — to improve how accurately the graph samples that indirect light. The Lighting Model’s Descriptor also exposes Diffuse Model and Specular Model sub-properties alongside Apply Bent Normal. Rather than affecting which lighting data the material reads, these determine what shading math the material applies to the light it already receives.

![A screenshot of a Reality Composer Pro 3 scene with an object selected and the Lighting Model and related properties showing in the Inspector.](/images/RealityComposerPro/LightingMaterialExample2@2x.png)

For example, choosing a Diffuse Model like Lambertian, Hammon, or Oren Nayar, or a Specular Model like GGX, Sheen, or Anisotropic GGX, changes how that same incoming lighting data becomes a final shaded color.

## See Also

- [Lighting a scene with lights and light layers](lighting-a-scene-with-lights-and-light-layers.md)
  Configure lights and light layers to control a scene’s illumination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/configuring-how-materials-respond-to-light)*