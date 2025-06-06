# Simulations and motion

**Framework**: RealityKit

Simulate physical interactions between entities or systems.

#### Overview

RealityKit simulates physical interactions between virtual objects in your scene, as well as between virtual objects and detected surfaces in the real world, such as floors, walls, or tabletops. On devices with a LiDAR Scanner, RealityKit can even simulate interactions between virtual objects and scanned real-world geometry.

## Topics

### Simulation setup
- [Designing scene hierarchies for efficient physics simulation](designing-scene-hierarchies-for-efficient-physics-simulation.md)
  Configure your RealityKit scenes to avoid performance bottlenecks.
- [Handling different-sized objects in physics simulations](handling-different-sized-objects-in-physics-simulations.md)
  Set up a scene hierarchy for accurate physics simulations.
- [struct PhysicsSimulationComponent](physicssimulationcomponent.md)
  A component that controls localized physics simulations.
### Simulation-related notifications
- [enum PhysicsSimulationEvents](physicssimulationevents.md)
  Types of events that fire during physics simulations
### Physical properties
- [struct PhysicsBodyComponent](physicsbodycomponent.md)
  A component that defines an entity’s behavior in physics body simulations.
- [class PhysicsMaterialResource](physicsmaterialresource.md)
  Material properties, like friction, of a physically simulated object.
- [enum PhysicsBodyMode](physicsbodymode.md)
  The ways that a physics body can move in response to physical forces.
- [struct PhysicsMassProperties](physicsmassproperties.md)
  Mass properties of a physics body.
### Physics motion
- [struct PhysicsMotionComponent](physicsmotioncomponent.md)
  A component that controls the motion of the body in physics simulations.
- [struct ImpulseAction](impulseaction.md)
  An action that applies an impulse to the physics body at its center of mass when played as an animation.
### Particle simulation
- [Simulating particles in your visionOS app](simulating-particles-in-your-visionos-app.md)
  Add a range of visual effects to a RealityKit view by attaching a particle emitter component to an entity.
- [struct ParticleEmitterComponent](particleemittercomponent.md)
  A component that emits particles.
- [ParticleEmitterComponent.ParticleEmitter](particleemittercomponent/particleemitter.md)
- [ParticleEmitterComponent.Presets](particleemittercomponent/presets.md)
  Initial configurations that can be set when starting a new simulation.
### Entity compliance
- [protocol HasPhysicsBody](hasphysicsbody.md)
  An interface that enables physics simulations based on the rules of Newtonian mechanics.
- [protocol HasPhysicsMotion](hasphysicsmotion.md)
  An interface that provides velocity properties for physics simulations.
- [protocol HasPhysics](hasphysics.md)
  An interface that combines the physics body and physics motion interfaces.

## See Also

- [Collision detection](physics-collision-detection.md)
  Determine when entities collide with each other or the environment.
- [Force effects](physics-force-effects.md)
  Control the movement of virtual objects with forces.
- [Physics joints and pins](physics-joints-and-pins.md)
  Simulate joint physics that connect virtual objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physics-simulations-and-motion)*