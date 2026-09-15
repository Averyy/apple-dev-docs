# Creating a procedural Shader Graph material

**Framework**: Reality Composer Pro

Learn how to build an organic, pulsing, color-shifting material in the Reality Composer Pro 3 Shader Graph.

#### Overview

This walkthrough goes beyond [`Designing materials with Shader Graph`](designing-materials-with-shader-graph.md) and guides you through using Reality Composer Pro 3’s Shader Graph to create an advanced, dynamic material with animated special effects.

The graph blends two contrasting colors — a **Foreground** and **Background** color — across the surface. The graph uses an animated cellular (Worley) noise pattern, so the boundary between the two colors looks organic instead of like a hard edge, and quietly pulses over time instead of sitting still.

The same pulsing value also does two more things: it nudges the surface roughness up and down, and it nudges each point on the mesh slightly outward and back along its own surface normal, so the object looks like it’s subtly breathing rather than being a static prop.

Structurally, the graph has two independent outputs that both come from the same core calculation:

- A **Surface Shader** branch (a `PreviewSurface` node) that controls color and material response to light.
- A **Geometry Modifier** branch that displaces the mesh itself.

Both branches read from the same animated noise value, which is why the color shift and the surface bulge stay in sync. The image below shows the completed graph. The remainder of the article describes how to create it and what each node does to create the completed effect.

![A screenshot of the completed Shader Graph material created in this walkthrough.](/images/RealityComposerPro/ShaderGraphAdv1@2x.png)

#### Review Shader Graph Basics

If you’re new to Reality Composer Pro 3’s Shader Graph editor, see [`Designing materials with Shader Graph`](designing-materials-with-shader-graph.md) and [`Building materials in Reality Composer Pro`](building-materials-in-reality-composer-pro.md) to learn the basics of creating materials and using the Shader Graph.

#### Build the Animated Worley Noise Pattern

Add a **Position** node. Leave its coordinate-space dropdown (labeled “object” to the left of the node) set to **Object**, so the pattern stays fixed to the mesh’s own surface instead of sliding around as the entity moves through the world.

Add a **Multiply** node. Connect the Position’s output into one of its inputs.

Add an **Input** node somewhere below Position. In the Inspector, add two inputs. Set the Type for each Input to Color3 (Half). Name one of the Inputs **Foreground** and name the other Input **Background**. Choose a color for **Foreground** and **Background** (ideally contrasting colors). Then, add a third input named **CellDensity**, set its Type to Float and set its Value to 1.5.

> 💡 **Tip**: At this stage in the graph, only CellDensity is being used and the Foreground and Background parameters will be used later.  Each of these parameters are used as inputs to create a unified place to hold them and make them easier to manage. By default, newly created inputs become uniform of the shader. This enables the parameters to be adjusted at runtime.

Drag a connection from **CellDensity** into the Multiply node’s other input.

This parameter scales the position before it reaches the noise node: a higher value packs more, smaller cells into the same surface area, so exposing it as a parameter lets you resize the pattern without editing the graph.

Add a **Worley Noise 3D** node. Connect the Multiply node’s output into the **Position** input of the WorleyNoise3D node. Leave **Jitter** at its default of **1.0**. Jitter controls how irregular the cell placement looks; 0 gives a perfectly even grid of cells, and 1 gives the fully organic, randomized placement used here.

![A screenshot of the first four nodes of the Shader Graph material created in this walkthrough.](/images/RealityComposerPro/ShaderGraphAdv1-a@2x.png)

#### Animate the Pattern Over Time

Add another **Multiply** node. Connect the Worley Noise 3D node’s **Out** into one input, and set the other input’s literal value to **5.0**.

Add a **Time** node. It has no inputs — it just continuously outputs the number of seconds since the app started running.

Add an **Add** node. Connect the previous Multiply’s output into one input, and the Time node’s output into the other. The result is `(noise × 5.0) + time`. Multiplying by 5 first spreads out the noise values so that neighboring cells end up with very different phases once you take the sine of them (next step). Adding Time shifts that phase continuously, so the whole pattern appears to shimmer and pulse rather than stay fixed.

Add a **Sin** node and connect the Add node’s output into it. This turns the animated value into a smooth oscillation between -1 and 1.

Add a **Remap** node and connect Sin’s **Out** into its **In**. Set **In Low** to **-1.0** and **In High** to **1.0** — this matches the range Sin actually produces. Set **Out Low** to **0.0** and **Out High** to **1.0**, rescaling the oscillation into a plain 0–1 range that’s easy to use as a blend factor, a roughness value, or a displacement strength — which is exactly how the next three sections use it.

![A screenshot of the next five nodes of the Shader Graph material created in this walkthrough.](/images/RealityComposerPro/ShaderGraphAdv1-b@2x.png)

#### Blend Foreground and Background Colors Using the Pattern

Add a **Mix** node, choosing the variant that takes a float and returns a color (it appears on the canvas as `Mix (float → color3h)`).

Add an **Input** node near Mix (or reuse the one you already have). Since you already created **Foreground** and **Background** as inputs while building the noise pattern, this new Input node shows them as outputs alongside **CellDensity** — connect **Foreground** into Mix’s **Foreground** input, and **Background** into Mix’s **Background** input.

Connect the Remap node’s **Out** into Mix’s **Mix** input — this is the blend factor, so the color smoothly shifts between Foreground and Background as the animated pattern rises and falls. Connect Mix’s **Out** into the default `PreviewSurface` node’s **Diffuse Color** input.

![A screenshot of the next three nodes of the Shader Graph material created in this walkthrough.](/images/RealityComposerPro/ShaderGraphAdv1-c@2x.png)

#### Feed the Same Pulse Into Roughness

Drag a second connection directly from the Remap node’s **Out** — the same output you already used for Mix — into `PreviewSurface`‘s **Roughness** input. A single output can feed as many inputs as you want; dragging a new wire from a port that’s already connected doesn’t disturb the existing connection.

Leave the rest of `PreviewSurface` at its defaults: **Metallic** 0.0, **Clearcoat** 0.0, **Clearcoat Roughness** 0.01, **Opacity** 1.0, **Index of Refraction** 1.5, **Ambient Occlusion** 1.0, with **Emissive Color** and **Normal** untouched since this material doesn’t glow or use a normal map.

![A screenshot of the connection from the Remap node's output to the PreviewSurface Roughness input.](/images/RealityComposerPro/ShaderGraphAdv1-d@2x.png)

#### Push the Surface Along Its Normal with the Same Pulse

Add a **Normal** node. Like Position, leave its coordinate-space dropdown set to **Object**.

Add a **Multiply** node. Connect the Remap node’s **Out** into one input, and set the other input’s literal value to **0.1**. This keeps the displacement subtle — without scaling it down, the pulse would shove the surface a full unit outward, which is far too strong.

Add a second **Multiply** node. Connect the Normal node’s output into one input, and the previous Multiply’s output (the scaled-down pulse) into the other. Multiplying a direction vector by a small, animated scalar gives you a vector that points along the surface normal and grows and shrinks over time.

Add a **Geometry Modifier** node (it appears on the canvas as `GeometryModifier`). Connect the second Multiply’s output into its **Model Position Offset** input. Leave **Color**, **Normal**, **Bitangent**, and all eight **Uv** override inputs at their defaults. This graph only needs to offset each point’s position, so it doesn’t use any of the other overrides.

![A screenshot of the last four nodes of the Shader Graph created in this walkthrough.](/images/RealityComposerPro/ShaderGraphAdv1-e@2x.png)

#### Send Both Results to the Output Node

Every new Shader Graph material starts with `PreviewSurface` already wired to the `Output` node’s **Surface Shader** input — confirm that connection is still there. Connect the Geometry Modifier node’s **Out** into the `Output` node’s **Geometry Modifier** input.

Use the Preview tab below the Inspector to check your work. Observe the two colors blending across the surface in an organic cell pattern that pulses on its own, with the surface very subtly swelling and relaxing in time with the color shift.

Refer back to the short video and screenshot of the completed graph shown at the beginning of this article to compare results.

#### Review Each Nodes Role in the Graph

- **Position**: Outputs the position of the point currently being shaded, in the coordinate space you choose (Object space here). It’s the raw input the noise function samples.
- **Input**: Exposes the material’s parameters (**Foreground**, **Background**, **CellDensity**) so you can connect them to other nodes. The same three parameters appear on every Input node in this graph. This graph includes two copies to keep wires short.
- **Multiply / Add**: Generic two-input math nodes. This graph uses four of them: one to scale position by **CellDensity**, one to scale the noise output by 5.0, one to shrink the pulse to 0.1 for displacement, and one to combine the Normal vector with that shrunk pulse.
- **Worley Noise 3D**: Generates cellular noise: think of it as scattering random seed points through space and, at every location, measuring the distance to the nearest seed. That’s what produces the organic, cell-like pattern instead of smooth gradients. **Jitter** controls how randomly the algorithm scatters those seed points. It appears on the canvas as `WorleyNoise3D`.
- **Time**: Outputs elapsed time in seconds, with no inputs. It’s the only thing in the graph that changes on its own, which is what makes everything downstream of it animate.
- **Sin**: Takes the combined noise-and-time value and outputs its sine, producing a smooth, repeating oscillation between -1 and 1.
- **Remap**: Linearly rescales a value from one range to another. Here it converts Sin’s -1-to-1 output into a 0-to-1 value, which is the range every consumer downstream (Mix, Roughness, displacement) expects.
- **Mix**: Blends between two colors using a float factor. **Foreground** and **Background** are the two colors; the remapped noise-and-time value is the blend factor. It appears on the canvas as `Mix (float → color3h)`.
- **Preview Surface**: The physically based surface shader. It reads the mixed color into Diffuse Color and the same remapped value into Roughness, alongside fixed values for the rest of its material properties. It appears on the canvas as `PreviewSurface`.
- **Normal**: Outputs the surface normal direction at the point being shaded, in the coordinate space you choose (Object space here).
- **Geometry Modifier**: Displaces the actual mesh geometry. `Model Position Offset` is the only input this graph drives, moving each point along its normal by a small, animated amount. It appears on the canvas as `GeometryModifier`.
- **Output**: The graph’s root node. `Surface Shader` controls appearance, `Geometry Modifier` controls shape, and `Post Lighting Shader` (unused here) lets you modify the final lit color.

#### Review Shader Graph Possibilities

If you want to experiment further with advanced materials and effects, refer to the following screenshots of additional Shader Graphs and recreate them in Reality Composer Pro 3.

**Disintegration effect**

![A screenshot of the completed Reality Composer Pro 3 Shader Graph to create a disintegrating material effect.](/images/RealityComposerPro/ShaderGraphAdv2@2x.png)

**Force field bubble effect**

![A screenshot of the completed Reality Composer Pro 3 Shader Graph to create a pulsing, force field material effect.](/images/RealityComposerPro/ShaderGraphAdv3@2x.png)

## See Also

- [Building materials in Reality Composer Pro](building-materials-in-reality-composer-pro.md)
  Apply surface properties to 3D entities to control how they look in your scene.
- [Applying materials to an asset](applying-materials-to-an-asset.md)
  Assign and configure surface materials on 3D model assets in Reality Composer Pro.
- [Designing materials with Shader Graph](designing-materials-with-shader-graph.md)
  Create realistic materials with Reality Composer Pro’s Shader Graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/creating-a-procedural-shader-graph-material)*