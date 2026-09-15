# Building a working Compute Graph example

**Framework**: Reality Composer Pro

Combine emission, initialization, simulation, and output nodes into a swirling ring of particles colored from a gradient texture.

#### Overview

The example on this page illustrates how to combine emission, initialization, simulation, and output nodes into a complete effect: a gradient spiral of colored particles.

**To try it yourself:** build a new Compute Graph asset in Reality Composer Pro and wire each phase as shown below. See [`Introducing Compute Graph`](introducing-compute-graph.md) for how to create and attach a Compute Graph. Swap `gradient-sixcolors.png` (in the Sample Texture 2D node of the Simulate Phase) for any horizontal gradient texture to restyle the effect without touching a single node.

#### View the Completed Compute Graph

Before you begin, review the complete Compute Graph below to familiarize yourself with each section. Subsequent sections in this article describe each phase in more detail.

![A screenshot of the complete Reality Composer Pro 3 Compute Graph described in this article.](/images/RealityComposerPro/ComputeGraphComplete@2x.png)

#### Emit Particles Continuously

Continuous emission keeps a steady stream of particles going, while the burst provides an initial gust of particles so the effect doesn’t start sparse.

For this example, in the Emitter section, set the `rate (float)` to 20000 and the `maxBurst (float)` to 1000.

![A screenshot of the example Compute Graph's Emitter section node and settings.](/images/RealityComposerPro/ComputeGraph0@2x.png)

#### Initialize Particle Color From Position

For the Set Position part of the Initialize Phase, the nodes grouped inside the comment box labeled Circle turn a single Random Float into a spawn point on a ring. A multiply node scales the random value by 6.28 (2 * pi) into a full-circle angle in radians. Sine and Cosine then feed a Compose float3 with z pinned to 0, producing a unit circle in the XY plane.

A second chain animates the radius. Cosine of Graph Age is rescaled — multiplied by 0.5 and offset by 0.5. This is to normalize the cosine from [-1, 1] to [0, 1]. A Compose float3 broadcasts that value across all three components, and the final Multiply float3 scales the ring uniformly.

The result is particles spawning evenly around a ring that breathes in and out over time, driven entirely by one random number and the graph clock rather than a keyframed emitter shape.

![A screenshot of the example Compute Graph's Initialize Phase, with a series of nodes connecting to the Set Position node.](/images/RealityComposerPro/ComputeGraph1@2x.png)

#### Set Particle Velocity and Lifetime

Still in the Initialize Phase, add and configure nodes as shown below.

For the Set Velocity part of the Initialize Phase, Element Position and Decompose float3 read the spawn point back out, and a Compose float3 reassembles it rotated 90 degrees in the XY plane. The new x takes the decomposed y, the new y takes 0 minus the decomposed x, using the Subtract node, and z stays 0.

Because the spawn point is itself a radius vector from the ring’s center, rotating it 90 degrees yields a tangent. Wiring that tangent into Set Velocity launches every particle along the ring instead of outward from it, so the system reads as a rotating vortex rather than an expanding burst. Swapping which component gets negated reverses the direction of the swirl.

For the Set Lifetime part of the Initialize Phase, a Random node scaled by 5.0 feeds Set Lifetime, giving each particle an independent 0 to 5 second lifespan. Because the durations are decorrelated, the population dissolves and replenishes continuously instead of visibly pulsing as whole generations expire in lockstep.

![A screenshot of the example Compute Graph's Initialize Phase, with a series of nodes connecting to the Set Velocity and Set Lifetime nodes.](/images/RealityComposerPro/ComputeGraph8@2x.png)

Note that in the image above, the y (float) of the Decompose Node connects to the x (float) of the Compose Node.

#### Simulate Particle Motion

In the Simulate Phase, standard physics integration moves each live particle every frame, for as long as it exists. A series of operators feeds into a Sample Texture 2D node, which connects to a gradient texture — a simple `.png` file with the color gradient (shown below). These nodes connect, in turn, to the Set Color node.

![A screenshot of the gradient texture used to create the Compute Graph effects in the example on this page.](/images/RealityComposerPro/ComputeGraphGradientExample@2x.png)

Remove the default Set Gravity node from the Simulate Phase; it’s not needed for this demonstration. Instead, add a Noise Force node.

Decompose float3 extracts each particle’s x position, and a multiply and an add node rescale that value from the ring’s roughly -0.5 to 0.5 range into the gradient texture’s 0 to 1 sample coordinate space, which Sample Texture 2D then uses to look up a six-color rainbow gradient.

Because Set Color sits in the Simulate phase, that lookup re-runs every frame, so the gradient behaves like a fixed field in space that particles take on new colors from as they drift through it. The entire colorization comes from one texture lookup rather than hand-authored per-particle color logic.

For the Noise Force part of the Simulate Phase, the Compose NoiseParams node configures the Noise Force field rather than feeding a computed value into it: `inputScale` at 4.0 on all axes sets how tightly the noise varies across space, `inputBias` stays at zero, and `outputScale` at 0.25 keeps the resulting force gentle.

Paired with Integrate, it layers continuous low-amplitude turbulence over the tangential motion so the orbits never look mechanically perfect.

![A screenshot of the example Compute Graph's Simulate Phase with a series of nodes connected to the Set Color and Noise Force nodes in the Simulate Phase.](/images/RealityComposerPro/ComputeGraphColor2@2x.png)

#### Fade Particles in and Out

In the Output Phase, add a Fade In/Out node. It needs no inputs — it fades each particle in and out automatically, based on that particle’s own age and lifetime, rather than reading a value from an upstream node. The phase’s Constants node also configures the rendered look: this example uses an Octagon topology for each particle’s billboard, with `billboard_material` as the material. The fade affects opacity only; the color sampled during Simulation keeps updating every frame and carries through unchanged as each particle fades in and out.

![A screenshot of the example Compute Graph's Output Phase and settings.](/images/RealityComposerPro/ComputeGraph3@2x.png)

## See Also

- [Introducing Compute Graph](introducing-compute-graph.md)
  Use Reality Composer Pro Compute Graph to build custom particle simulations with a node-based graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/building-a-working-compute-graph-example)*