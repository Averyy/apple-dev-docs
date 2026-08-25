# Lighting a scene with lights and light layers

**Framework**: Reality Composer Pro

Configure lights and light layers to control a scene’s illumination.

#### Overview

A scene’s final look depends on two independent systems working together: the lights you place in it, and the materials that decide whether geometry reacts to those lights. You add light components to entities to define where light comes from and how strong it is, and you choose a material’s [`Building materials in Reality Composer Pro`](building-materials-in-reality-composer-pro.md) to define whether a surface responds to that light at all. Neither system knows about the other’s specific settings, but their combined effect determines everything you see in the viewport. This article describes this connected system piece by piece. Treat lighting and materials as a connected system from the start, and your results become intentional instead of accidental.

> **Note**: To learn about how materials interact with lighting, see [`Configuring how materials respond to light`](configuring-how-materials-respond-to-light.md).

![A screenshot of a 3D scene with multiple light components in Reality Composer Pro.](/images/RealityComposerPro/LightingScene2@2x.png)

#### Choose a Light Type Based on Its Real World Behavior

Reality Composer Pro’s three dynamic light types map closely to real-world light sources, so the best way to choose among them is to think about the kind of light source you’re trying to simulate. A **Directional Light** represents a source so far away that its rays arrive parallel, like sunlight. Because it uses only the entity’s orientation, moving the entity has no visible effect on the light — only rotating it changes the lighting direction.

> 💡 **Tip**: One exception to this behavior is a shadowed directional light with its Shadow Component Projection setting set to Fixed Projection. This lets you manually size and place the shadow frustum in your scene. See [`DirectionalLightComponent.Shadow.ShadowProjectionType`](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/shadowprojectiontype) for more information.

Use a Directional Light for outdoor sun or moon lighting, or any scenario where you want uniform lighting across an entire scene regardless of where objects sit within it. See [`DirectionalLightComponent`](https://developer.apple.com/documentation/realitykit/directionallightcomponent) for more information about Directional Lights.

![A screenshot of a Reality Composer scene lit by directional light.](/images/RealityComposerPro/LightingDirectionalLightExample@2x.png)

A **Point Light** radiates in every direction from a single location, like a light bulb or candle flame. Because it uses only the entity’s position, its effect falls off with distance according to its Attenuation property, an Inspector setting that controls how quickly the light’s intensity fades as distance from the source increases.

Attenuation is measured in meters rather than lumens — it sets the distance from the light where its intensity reaches zero, not a real-world brightness value. As a rough intuition builder: a candle lights a radius of about a meter, while stadium lighting can reach 100 to 200 meters. A lamp in a room behaves much closer to the candle end of that range than the stadium end.

See [`PointLightComponent`](https://developer.apple.com/documentation/realitykit/pointlightcomponent) for more information about Point Lights.

![A screenshot of a 3D Reality Composer Scene lit by a point light.](/images/RealityComposerPro/LightingPointLightScene@2x.png)

A **Spot Light** radiates from the entity’s position, but only within a cone pointed along the entity’s orientation, bounded by inner and outer angle settings plus its own Attenuation property. The inner angle marks where full intensity ends; the light fades between the inner and outer angle, reaching zero intensity at the outer angle.

Like Point Lights, Spot Lights have a real-world reference range: a small accent light sits near the dim, narrow end of the spectrum, and a large event light sits near the bright, wide end. Use a Spot Light whenever you need to direct attention at a specific area, such as a flashlight beam or a stage light. See [`SpotLightComponent`](https://developer.apple.com/documentation/realitykit/spotlightcomponent) for more information about Spot Lights.

Spot lights can also be configured to project an image. After placing the Spot Light in your scene, select it. In the Inspector, turn on Casts Projective Textures, then click the Projective Texture field and select a texture asset. From there, you can configure Scale, Offset, and Rotation to change the relative shape and position of the projected image.

![A screenshot of a Reality Composer Scene lit by a spot light.](/images/RealityComposerPro/LightingSpotLightScene@2x.png)

> 💡 **Tip**: The Inspector’s Attenuation field on Point Light and Spot Light maps to the component’s `attenuationRadius` property; as of this writing, there is no separate Inspector control for `attenuationFalloffExponent`. Treat Attenuation as one dial that controls how quickly light intensity drops off with distance, and adjust it by feel while watching the viewport.

#### Choose Dynamic or Static Lighting

Each light component also has a mobility setting that defines it as dynamic or static.

- A dynamic light recalculates its lighting contribution in real time, which is what you want for lights that move or change color during your experience.
- A static light is fixed and eligible for baked lighting techniques elsewhere in your pipeline — a workflow beyond the scope of this article. If you’re unsure which to choose, start with dynamic and revisit the choice only if you have a specific performance or baking requirement.

#### Relate Lights and Materials Before Placing Them

Before adding a single light component, it helps to understand how Reality Composer Pro’s lighting pieces relate to each other. Light types are additive and parallel. You can place any number of Directional, Point, and Spot lights in a scene (be mindful of performance) and their contributions sum together at every point they reach. There’s no exclusivity between them — a scene can mix all three light types freely. As described above, each light type samples a different part of the entity’s Transform — Directional Lights use only orientation, Point Lights use only position, and Spot Lights use both.

![A screenshot of a Reality Composer Pro scene with a point light selected.](/images/RealityComposerPro/LightingPointLightExample@2x.png)

See [`Configuring how materials respond to light`](configuring-how-materials-respond-to-light.md) for how a material’s Shader type determines whether it responds to these lights.

#### Configure Light Layers to Filter Scene Lighting

Light Layers let you control whether lights affect specific entities in a scene. Create a Named Layer File and then assign it to a light’s Light Layer Asset property. Then, you can select individual entities and assign them to light layers, allowing you to filter which lights affect which entities.

> 💡 **Tip**: A new Reality Composer Pro project starts with a default Named Layer File in the Core folder.

A common use case is a cinematic scene, where you might want to cast light onto a specific character without lighting the entire scene.

To create a Named Layer File, in the Project Browser, click **[+]** and then select **Gameplay** > **Named Layer File**. Type a name for the layer file and then press Return.

Next, in the Inspector, enter a name for each layer you want to use.

In your scene, select a light you want to use the Layers file with. Then, in the Inspector, next to **Light Layer Asset**, select your Named Layer File from the menu. This exposes the Active Light Layers. Select the checkbox for each layer you want to enable.

With a Named Layer File created, you can now assign meshes and lights to layers. Add an entity to the scene, and then add a Render Layer Component to that entity. Select the Named Layer File for the Render Layer, and then select each layer the entity belongs to.

![A screenshot of a Reality Composer Pro scene with a Render Layer component shown in the Inspector.](/images/RealityComposerPro/LightingRenderLayer1@2x.png)

#### Control How Lights and Entities Cast Shadows

Getting a shadow to appear requires two settings to agree: one on the light and one on the entity that should show the shadow. Configure both correctly, or no shadow appears.

Directional Light and Spot Light components each expose their own **Casts Shadow** property in the Inspector, along with additional shadow-tuning settings, such as Shadow Depth Bias and Shadow Max Distance for Directional Light. Turn on **Casts Shadow** to tell a light to project shadows from anything blocking its path.

Two additional components affect whether an entity casts shadows. The [`DynamicLightShadowComponent`](https://developer.apple.com/documentation/realitykit/dynamiclightshadowcomponent) component controls whether an entity casts a shadow from dynamic lights; as of this writing, entities cast dynamic-light shadows even without adding this component. In practice, you reach for the Dynamic Light Shadow component mainly when you want to opt an entity out of shadow casting, not to opt it in.

Also add a Model Component ([`ModelComponent`](https://developer.apple.com/documentation/realitykit/modelcomponent)) to the entity, since a shadow needs actual geometry to cast it.

Add these components to each individual entity as needed because they are not inherited by an entity’s children. As a result, a hierarchy of meshes needs the component on every mesh entity that should participate.

#### Use Shadow Cascades for Directional Lights

Shadow Cascades are available to Directional Lights and control how sharp the shadow looks. Set Cascades to Fixed and then specify a number; the higher the number, the sharper the shadow. Set Cascades to Automatic and RealityKit dynamically balances sharpness with performance.

> 💡 **Tip**: Shadow Cascades can be expensive and may not yield a significant quality improvement in certain camera and light configurations. They’re most effective in large scenes with a high dynamic range in scene depth, such as when the camera shows both near and distant objects to the viewer.

#### Tune Shadow Quality for Performance

In the Shadow Component for Spot Lights, use a Medium or High Shadow Quality setting to create softer shadows.

> 💡 **Tip**: Depending on how you use them, Low and Medium Shadow Quality can yield similar results, making Medium a good balance between quality and performance. Using a High Shadow Quality can impact performance. Use High Quality sparingly. Limit High Quality shadows to a single light source in a scene.

Increasing the **Light Size** increases the size of the source light with commensurate effects on cast shadows. **Depth Bias** affects how shadows are cast from light striking surfaces from different angles. Both can be used to subtly tune how your shadows look.

For Directional Lights, as of this writing the Maximum Distance property defaults to 10 meters; use the lowest possible value that still tightly fits the area where you want shadows, to improve shadow quality and sharpness.

#### Simulate Shadows Without a Light Source

Reality Composer Pro also offers [`GroundingShadowComponent`](https://developer.apple.com/documentation/realitykit/groundingshadowcomponent), which produces a simulated effect that behaves as if a light source were positioned directly overhead. The component works independently of any actual light in your scene and doesn’t depend on the **Casts Shadow** setting on any light.

Select an entity and then add the Grounding Shadow component to enable it. This also exposes **Casts Shadow**, **Receives Shadow**, and **Fade Behavior** settings for objects near physical surfaces. See [`GroundingShadowComponent`](https://developer.apple.com/documentation/realitykit/groundingshadowcomponent) for more information.

Like [`DynamicLightShadowComponent`](https://developer.apple.com/documentation/realitykit/dynamiclightshadowcomponent), the Grounding Shadow component requires [`ModelComponent`](https://developer.apple.com/documentation/realitykit/modelcomponent) on the entity, and you add it to each entity individually rather than applying it to a hierarchy. Reach for grounding shadows when you want a plausible contact shadow under an object without configuring or even needing a real light to produce it.

#### Add Environment Lighting for Indirect Light

Direct lights — Directional, Point, and Spot — model light coming from a specific source. Indirect environment lighting fills in everything else: the ambient bounce light that a real environment produces from every surface around it. Reality Composer Pro adds this through an Image Based Light  Component and an Image Based Light Receiver Component.

Add an Image Based Light Component to a source entity to produce indirect light. It holds the lighting-environment data itself, exposed in the Inspector as a Type property and an Intensity Exponent property that scales the environment’s contribution. This component’s lighting is additive with every other light in your scene — it doesn’t replace or override your Directional, Point, or Spot lights; it supplements them with soft, ambient-feeling illumination.

See [`ImageBasedLightComponent`](https://developer.apple.com/documentation/realitykit/imagebasedlightcomponent) to learn more.

Add an Image Based Light Receiver Component to any entity you want a particular image-based light to illuminate, configured with a single Entity property that references the source entity carrying the Image Based Light Component.

> **Note**: This explicit link means an image-based light only affects entities that opt in. Placing an Image Based Light Component in a scene doesn’t automatically light everything in it. See [`ImageBasedLightReceiverComponent`](https://developer.apple.com/documentation/realitykit/imagebasedlightreceivercomponent) for more information.

#### Use Virtual Environment Probes for Indirect Lighting

For fully virtual environments, add a [`VirtualEnvironmentProbeComponent`](https://developer.apple.com/documentation/realitykit/virtualenvironmentprobecomponent) to give objects believable indirect lighting, precalculated from an [`EnvironmentResource`](https://developer.apple.com/documentation/realitykit/environmentresource) you configure.

![A screenshot of a Reality Composer Pro scene with a Virtual Environment Probe selected and its properties displayed in the Inspector.](/images/RealityComposerPro/LightingVirtualEnvProbe1@2x.png)

RealityKit combines the light from the Virtual Environment Probe with other lights in the scene to calculate an entity’s final lighting. Whether you need to place probes explicitly depends on the kind of space your content runs in.

> 💡 **Tip**: Because probes bake lighting ahead of time rather than computing it live, they avoid the runtime cost of real-time global illumination calculations.

Add a Virtual Environment Probe Component to your scene, and then select a Data type (Single, Blend, or None). Pick a color and use the Parallax Bounds fields to configure the x, y, and z axes in meters to define the area you want to light. Click the Capture Probe button. Reality Composer Pro generates a folder named `Captured Cubemaps` and stores the captured preview files there.

In visionOS’s Shared Space, visionOS composites your content with the person’s physical surroundings through passthrough. ARKit is designed to supply environment lighting derived from the person’s real-world surroundings in this configuration, so a probe usually isn’t necessary.

In a fully virtual environment, there’s no physical surrounding for ARKit to sample, so you place a Virtual Environment Probe to supply that lighting yourself. See  [`VirtualEnvironmentProbeComponent`](https://developer.apple.com/documentation/realitykit/virtualenvironmentprobecomponent) for more information.

#### Preview Lighting While Iterating

Once your lights and materials are in place, Reality Composer Pro gives you several ways to see exactly what they’re doing, closing the loop between configuring lighting and confirming it looks right.

The Lighting Environment Settings control in the viewport toolbar, marked with a sun icon, lets you create or select a lighting-environment asset that previews how your scene looks under different ambient conditions. Reality Composer Pro automatically enables this preview for any asset that doesn’t carry its own light, so you always have some illumination to evaluate your materials against. Treat this control as an authoring-time convenience for the viewport rather than a component that ships with your experience.

![A screenshot highlighting the Reality Composer Pro 3D Light Environment Settings control.](/images/RealityComposerPro/LightingPreview1@2x.png)

Use Debug Views (the icon to the right of the Light Environment Settings) to reveal otherwise invisible light properties.

- Turning on the Point Light Debug View draws a sphere around each Point Light showing its effective range based on its Attenuation setting, giving you a direct, visual check on the Attenuation value.
- Turning on the Spot Light Debug View draws the inner and outer cone boundaries so you can see exactly which surfaces a spotlight’s beam reaches before you commit to its placement.
- Turning on the Directional Light Debug View shows directional indicator arrows and the color of the Directional Light in your scene.

Rendering Visualization Modes go a step further by isolating individual lighting contributions.

- The Lighting Diffuse mode shows only the diffuse component of your lighting
- The Lighting Specular mode shows only the specular highlights, letting you inspect each contribution independently rather than trying to judge them together in the final composited image.

These modes are especially useful for diagnosing whether a Lit Shader Graph material is actually receiving light. See [`Configuring how materials respond to light`](configuring-how-materials-respond-to-light.md) for more on Lighting Model/surface output mismatches. Move through these modes whenever a scene’s lighting doesn’t match your expectations — they typically make it obvious whether the problem is a light’s placement, its Attenuation, or a material’s Shader configuration.

## See Also

- [Configuring how materials respond to light](configuring-how-materials-respond-to-light.md)
  Match how a material reacts to the lights in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/lighting-a-scene-with-lights-and-light-layers)*