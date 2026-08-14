# Building a working Compute Graph example

**Framework**: Reality Composer Pro

Combine emission, initialization, simulation, and output nodes into a falling-snow effect colored from a gradient texture.

#### Overview

The example on this page illustrates how to combine emission, initialization, simulation, and output nodes into a complete effect: falling snow. The initialization stage samples each particle’s color from a gradient texture based on its horizontal position.

![A screenshot of a globe using a gradient texture for its particles.](/images/RealityComposerPro/ComputeGraphColorRampGlobe@2x.png)

**To try it yourself:** build a new Compute Graph asset in Reality Composer Pro and wire each stage as shown below. See [`Introducing Compute Graph`](introducing-compute-graph.md) for how to create and attach a Compute Graph. Swap `gradient-sixcolors.png` (in the Sample Texture 2D node of the Initialize stage) for any horizontal gradient texture to restyle the effect without touching a single node.

#### Emit Particles Continuously

Continuous emission keeps a steady snowfall going, while the burst provides an initial gust of particles so the effect doesn’t start sparse.

![A screenshot of the example Compute Graph's Emission stage node and settings.](/images/RealityComposerPro/ComputeGraphColor1@2x.png)

#### Initialize Particle Color From Position

**Decompose float3** extracts each particle’s x position at spawn. A `*` and `+` node rescale that value into the gradient texture’s 0–1 sample coordinate space, and the graph uses the result to sample a six-color rainbow gradient texture. The result is snow that’s naturally colorized left-to-right across the emission volume, entirely from one texture lookup rather than hand-authored per-particle color logic.

![A screenshot of the example Compute Graph's Initialization stage node and settings.](/images/RealityComposerPro/ComputeGraphColor2@2x.png)

#### Simulate Particle Motion

Standard physics integration moves each particle as it falls, updating position and velocity every simulation tick using the gravity and drag values shown below.

![A screenshot of the example Compute Graph's Simulation stage node and settings.](/images/RealityComposerPro/ComputeGraphColor3@2x.png)

#### Fade Particles in and Out

Particles fade in as they spawn and fade out near the end of their life, rendered as billboard quads. The color sampled during initialization persists through this fade, so each particle keeps its gradient-based color for its entire lifetime.

![A screenshot of the example Compute Graph's Output stage node and settings.](/images/RealityComposerPro/ComputeGraphColor4@2x.png)

## See Also

- [Introducing Compute Graph](introducing-compute-graph.md)
  Use Reality Composer Pro Compute Graph to build custom particle simulations with a node-based graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/building-a-working-compute-graph-example)*