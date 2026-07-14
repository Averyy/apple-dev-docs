# Introducing Compute Graph

**Framework**: Reality Composer Pro

Use Reality Composer Pro Compute Graph to build custom particle simulations with a node-based graph.

#### Overview

Compute Graph is a standalone node-based framework for constructing particle simulations and general-purpose GPU compute graphs that work with RealityKit. Compute Graph is designed for developers who need granular control over how particles and compute work runs.

Unlike the [`Creating particle systems in Reality Composer Pro`](creating-particle-systems-in-reality-composer-pro.md), which provides a high-level interface for common particle effects, Compute Graph gives you direct control over the GPU compute pipeline. Use Compute Graph when you need custom simulation behavior that the built-in Particle Emitter component doesn’t support.

Use Compute Graph instead of Particle Emitter when you need:

- Custom per-particle logic that isn’t exposed as a Particle Emitter property, for example, sampling a texture to drive color, running custom physics forces, or terminating particles based on a condition you compute yourself.
- A GPU compute pipeline that isn’t strictly “particles” at all — Compute Graph is general-purpose GPU compute, not only a particle system.
- Fine control over performance — you decide exactly what runs in each stage, rather than depending on a fixed set of emitter properties.

Like other Reality Composer Pro graphs, Compute Graph is a node-and-connection-based workflow designer. Before working with Compute Graph, review the general navigation and features of the Reality Composer Pro Graph Editor in [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md).

#### Add a Compute Graph to Your Project

In the Reality Composer Pro Project Browser, click **+** and then select **Compute Graph**. Give the Compute Graph a name, and then double-click it to open it.

Alternatively, Control-click inside a folder, and then click **New** > **Compute Graph**. Give the Compute Graph a name, and then double-click it to open it.

![A screenshot of the Reality Composer Pro default Compute Graph in the Editor.](https://docs-assets.developer.apple.com/published/6ad0750231953d3716812a9065fb70b1/ComputeGraphBaseExample%402x.png)

#### Work Within the Four Stage Run Order

The default Compute Graph node includes four stages — Emission, Initialization, Simulation, and Output. Additional stage types, such as Texture, are available when configuring custom pipelines. The Compute Graph phases run top to bottom.

At the top of each stage is a node called **Constants**.  Constant nodes provide static values that you can feed into other nodes’ parameters. Functionally, Constants are the mechanism for injecting fixed, hardcoded values  into the graph, as opposed to values computed dynamically from other nodes. In the Simulate phase, for example, you can use the Constant to setup the capacity count and a loop toggle. The Output phase Constant contains properties related to the material used by the individual particles.

Add a node to a phase by clicking **+** inside the node. Nodes in each stage run in the order they appear, top to bottom; reorder them with the up and down arrows on a node when a later node depends on an earlier one’s result.

For example, in the Simulation stage, a `force::gravity` node feeding into `element_integrate` must run before a termination check that depends on the resulting position. A **Texture** stage type is also available for custom pipelines that generate textures rather than driving particles directly.

Every parameter is static until you wire a node into its port, which is what makes it dynamic. Compute Graph has no separate “dynamic mode” toggle the way some other tools do.

#### Attach a Compute Graph to an Entity

Select an entity in your scene. In the Inspector, click **Add Component**, and then choose **Compute Simulation**.

Next to **Compute Simulation**, click the field and then choose a Compute Graph.

Attach the Compute Graph to the entity that generates the effect.

![A screenshot of configuring the Compute Simulation component in the Reality Composer Pro Inspector.](https://docs-assets.developer.apple.com/published/6c7e19adde8c5b0e68bbcecbcc1de9e9/ComputeGraph2%402x.png)

#### Explore Built in Node Namespaces

Apple’s Compute Graph framework documents the full built-in node library by namespace, organized into `element::`, `emitter::`, `module::`, `force::`, `output::`, and utility namespaces. See the framework reference ([`Compute Graph`](https://developer.apple.com/documentation/ComputeGraph)) for a complete catalog of nodes in each namespace.

#### Read Current Element State with Element Nodes

Available in any stage, `element::` nodes read data about the particle currently being processed:

- `element::position`, `element::velocity`, `element::size`, and `element::color` return current per-particle values.
- `element::age` and `element::ageOverLifetime` return elapsed time (ageOverLifetime is normalized to 0–1 across the particle’s lifetime, useful for anything that should animate consistently regardless of how long the particle lives).
- `element::lifetime` returns the particle’s total configured lifetime.
- `element::index` returns the particle’s index, useful for deterministic per-particle variation.
- `element::terminate` ends the particle’s life immediately when its boolean input is true — use it for custom termination conditions, such as falling below a floor value or exceeding a distance from origin, instead of relying solely on a fixed lifetime.

See the Element namespace reference ([`element`](https://developer.apple.com/documentation/ComputeGraph/element)) for the full list.

#### Control Emission with Emitter Nodes

- `emitter::continuous` emits particles at a fixed rate.
- `emitter::burst` emits a single burst when the system spawns.
- `emitter::periodicBurst` repeats a burst on an interval, useful for effects like periodic sparks rather than a smooth stream.
- `emitter::setGroup` assigns spawned particles to an element group so other nodes can selectively operate on a subset of particles.

#### Initialize and Simulate with Module and Force Nodes

- `module::` nodes mutate per-particle state directly.
- `setPosition`/`addPosition`, `setVelocity`/`addVelocity`, `setColor`, `setAlpha`, `setSize`, and `setLifetime` set or offset the corresponding property.
- `force::` nodes apply physical forces during Simulation, meant to feed into an integration step: - `gravity` applies a downward force.
- `drag` slows a particle over time.
- `noise` applies a noise-based force for organic motion such as flickering flame or drifting smoke.
- `twist` applies a twisting force around a vertical axis for vortex effects.
- `add` applies an arbitrary constant force vector.

#### Shape Output with Output Nodes

Output nodes shape what’s rendered without modifying the underlying element data. This makes them useful for presentation-only effects that shouldn’t affect simulation physics.

- `output::setColor`, `output::setOpacity`, `output::setScale`, and `output::setSize` override the rendered appearance.
- `fadeInOut` produces a smooth fade-in/fade-out, commonly driven by `element::ageOverLifetime`.
- `growIn` produces a smooth grow-in animation for newly spawned particles.
- `setUV2` through `setUV7` set additional UV coordinate sets for effects that sample multiple textures per particle.

#### Reach for Utility Nodes

- `graph::` nodes are usable in any stage and cover general-purpose operations not specific to a single stage.
- `random::` nodes generate pseudo-random values seeded from the graph’s random number generator — the editor’s **Random (Float3)** node is what you’ll use to add per-particle variation to position, velocity, or color so a whole burst of particles doesn’t look identical.
- `texture_sample` and `texture_sample1d` sample a texture asset, letting you drive per-particle values, typically color, from an image rather than computing them with shader math.

#### Build a Worked Example Falling Snow with a Color Gradient

This example illustrates combining emission, initialization, simulation, and output nodes into a complete effect: falling snow whose color is sampled from a gradient texture based on each particle’s horizontal position.

**Emission stage:**

```None
emitter::continuous (rate: 1000/sec) ──┐
emitter::burst (count: up to 100)      ├──► (spawns particles)
```

Continuous emission keeps a steady snowfall going, while the burst provides an initial gust of particles so the effect doesn’t start sparse.

**Initialization stage:**

```None
spawn_demo() ──► module::setPosition
element::position ──► Decompose float3 ──► (x component)
   │
   ▼
* (float)  [scale x into 0–1 range]
   │
   ▼
+ (float)  [offset to align gradient sample point]
   │
   ▼
texture_sample1d (gradient-sixcolors.png) ──► module::setColor
```

Each particle’s initial color is derived from where it spawns: the x position is extracted with **Decompose float3**, rescaled into the gradient texture’s 0–1 sample coordinate space with a `*` and `+` node, then used to sample a six-color rainbow gradient texture. The result is snow that’s naturally colorized left-to-right across the emission volume, entirely from one texture lookup rather than hand-authored per-particle color logic.

**Simulation stage:**

```None
force::gravity ──► element_integrate ──► module::setPosition / module::setVelocity
```

Standard physics integration moves each particle as it falls, updating position and velocity every simulation tick.

**Output stage:**

```None
element::ageOverLifetime ──► output::fadeInOut ──► output::setOpacity
```

Particles fade in as they spawn and fade out near the end of their life, rendered as billboard quads.

**To try it yourself:** build a new Compute Graph asset in Reality Composer Pro and wire each stage as shown above. Swap `gradient-sixcolors.png` for any horizontal gradient texture to restyle the effect without touching a single node.

#### Add Compute Graph Bundles

Compute Graph Bundles are pre-built node compositions that encapsulate common patterns, making it easier to compose effects without wiring individual nodes.

Once added, a bundle’s composed nodes become available in the insertion menu like any other node, so you can drop in a known-good spawn pattern, force combination, or output treatment and then customize it locally rather than reconstructing it node by node.

Add Compute Graph Bundles from the Reality Composer Pro **Project Settings** menu. Click **Compute Graph Bundle**, click **+**, and then click the folder to find and select a bundle file. Repeat this process to add more bundles.

For complete documentation on Compute Graph nodes, see [`Compute Graph`](https://developer.apple.com/documentation/ComputeGraph).

#### Optimize Your Compute Graphs

- **Set particle capacity to match the effect.** An emitter configured for a far larger particle capacity than it ever actually uses wastes GPU memory — size the capacity to the emission rate and particle lifetime you’ve actually configured (roughly `rate × lifetime`, plus headroom for bursts).
- **Prefer a gradient texture over computed gradient math.** Sampling a small texture, as in the snow example above, is both more efficient than computing equivalent colors procedurally with shader math in the graph, and easier to iterate on — an artist can edit a texture without touching the graph.
- **Keep Output-stage work presentation-only.** Because Output nodes run every render frame for every live particle, avoid putting expensive computation there that could instead run once in Simulation (or once in Initialization, if the value doesn’t need to change over the particle’s life).
- **Use `element::terminate` deliberately.** Precise termination conditions, rather than relying purely on a long fixed lifetime, keep the live particle count, and therefore GPU cost, closer to what’s actually visible on screen.

#### Combine Compute Graph with Your Apps Gameplay Logic

If your effect needs to react to gameplay state — for example, intensifying based on a value a custom system computes in Swift (see [`Systems`](https://developer.apple.com/documentation/RealityKit/ecs-systems)), or only emitting while the app is in a certain mode — drive that through a **Public Input** on the graph. Set the input from your Swift code, or from a Script Graph node through a Set Variable or component write.

Keep Compute Graph focused on simulating and rendering the effect; broader gameplay logic belongs in RealityKit systems or Script Graph, feeding the Compute Graph through its exposed interfaces.

`ComputeGraphSimulation` ([`ComputeGraphSimulation`](https://developer.apple.com/documentation/ComputeGraph/ComputeGraphSimulation)) represents a simulation of particles, which use a single pipeline, built from a `ComputeNodeGraph` ([`ComputeNodeGraph`](https://developer.apple.com/documentation/ComputeGraph/ComputeNodeGraph)) and attached to a RealityKit `Entity` ([`Entity`](https://developer.apple.com/documentation/RealityKit/Entity)) through the Compute Simulation component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/introducing-compute-graph)*