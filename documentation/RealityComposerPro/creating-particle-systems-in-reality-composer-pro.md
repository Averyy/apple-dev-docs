# Creating particle systems in Reality Composer Pro

**Framework**: Reality Composer Pro

Add Particle Emitters and Particles to scenes to create nearly any type of visual effect.

#### Overview

The Reality Composer Pro Particle Emitter is a component you can add to an entity to create virtually any visual effect that emanates from an entity, such as:

- A campfire or flickering torch
- An explosion or fireworks
- A waterspout or rain shower

Particle Emitter properties appear in the Inspector, divided between two tabs: an **Emitter** tab and a **Particles** tab.

- **Emitter properties** — Emitter properties control the general shape and geometry of the emitter.
- **Particle properties** — Particle properties control the look, color, texture, shape, and other characteristics of emitted particles. In addition, there are two separate types of particles you can configure: **Main** particles and **Secondary** particles (particles spawned by particles).

#### Add a Particle Emitter to an Entity

Control-click World in the Reality Composer Pro Hierarchy, then choose **Add Child Entity** > **Geometry** > **Sphere**. Name the sphere in the Hierarchy and press Enter. The new sphere is selected in the Inspector — if it isn’t, click the sphere in the Viewport to select it. In the Inspector, click **Add Component** and select **Particle Emitter**.

> **Note**: You can start typing “particle” in the search box to quickly find the Particle Emitter component.

![A screenshot of Reality Composer Pro's Add Particle Emitter menu.](/images/RealityComposerPro/ParticleEmitter@2x.png)

#### Configure the Emitter and Main Particles

On the **Emitter** tab, configure the following properties:

- **Emitting** - Toggle to On to turn on the Emitter. While Emitting is on and Simulation State is set to Play, you can run the emitter continuously and watch it in your scene. Click **Play** to simulate the entire scene so you can see the particles as you make changes.
- **Loop** - Toggle to On. This makes the Emitter continuously emit particles.
- **Shape** - Set the shape to Sphere. This emits particles in a spherical pattern.
- **Simulation State** - Set to Play.

> ❗ **Important**: You can leave the simulation playing as you make changes. To move the entity or make other changes outside of the Particle Emitter, stop the simulation first.

In the Inspector, click **Particles** and configure the following properties:

- **Particles** - Leave set to **Main**.
- **Life Span** - Set to 5 seconds. This makes the emitted particles last longer.
- **Size** - Set to .1. The default is .02, so this makes larger particles.
- **Start Color A** - Click the color and use the sliders to change to any color you like. Try red.
- **End Color A** - Change to any color you like. Try yellow.

Watch how your changes affect the particle emitter and emitted particles, then configure the Secondary Particles.

![A screenshot of Reality Composer Pro sample entity emitting particles.](/images/RealityComposerPro/ParticleEmitter2@2x.png)

#### Configure Secondary Particles

If you stopped the simulation, select **Simulate** above the Workspace and then click **Play**. Configure Secondary Particles, which are particles spawned by the Main Particles. In the Inspector, click the **Emitter** tab and toggle **Spawning Enabled** on. Then click the **Particles** tab and switch the **Particles** selector from **Main** to **Secondary**. Configure the following properties for the Secondary Particles:

- **Life Span** - Set to 5 seconds. This makes the emitted particles last longer.
- **Size** - Set to .1.
- **Start Color A** - Click the color and use the sliders to change to any color you like. Try green.
- **End Color A** - Change to any color you like. Try purple.

![A screenshot of Reality Composer Pro sample entity emitting particles.](/images/RealityComposerPro/ParticleEmitter3@2x.png)

The sphere emits streams of particles that change color, beginning with the start color and changing to the end color over its lifetime. When the main particle expires, it emits the secondary particles. The secondary particle goes from its start color to its end color over its lifetime.

#### Explore Additional Properties

The following descriptions cover some of the more common particle emitter and particle properties you can experiment with. For a complete description of all properties, see [`ParticleEmitterComponent`](https://developer.apple.com/documentation/realitykit/particleemittercomponent) and [`ParticleEmitterComponent.ParticleEmitter`](https://developer.apple.com/documentation/realitykit/particleemittercomponent/particleemitter).

#### Review Emitter Properties

- **Emission Direction** - The direction particles are emitted when `birthDirection` is set to World or Local. Defaults to (0, 1, 0).
- **Shape Size** - The size, in meters, of the emitter shape geometry. This controls the dimensions of the region from which particles are spawned, not the size of individual particles.
- **Inherit Transformation** - Determines whether the entity’s transformation also affects the particles.
- **Field Simulation Space** - If set to Local, particles emitted move with the entity. If set to Global, particles the entity emits trail behind its movement.
- **Emission Duration** (seconds) - The number of seconds the emitter emits particles before stopping. This setting is only used when Loop is turned Off.
- **Emission Duration Variation** - Adds or subtracts a random amount of time (between zero and up to plus/minus the specified number) to the Emission Duration value.
- **Shape** - Defines the general shape — such as a sphere, cone, plane, or others — of how particles are emitted. The Emitter Shape is independent of the entity shape. For example, you can create a sphere entity that emits particles in a cone shape. Certain Shape properties only apply to specific shapes — for example, **Torus Radius** only applies when a Torus Shape is selected.
- **Birth Location** - The point of origin for the particles. This determines whether particles are emitted from the surface or from the vertices of the surface.

#### Review Particle Properties

- **Life Span** - The number of seconds the particle lasts.
- **Image** - Browse to and select an image to use for the particle.
- **Size** - The size of the particle. The default is 0.02.
- **Start Color A** - The starting color for the particle.
- **End Color A** - The end color for the particle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/creating-particle-systems-in-reality-composer-pro)*