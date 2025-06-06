# Physics Simulation

**Framework**: SceneKit

Add dynamic behaviors to scene elements; detect contacts and collisions; simulate realistic effects like gravity, springs, and vehicles.

## Topics

### Physics Bodies
- [class SCNPhysicsBody](scnphysicsbody.md)
  The physics simulation attributes attached to a scene graph node.
- [class SCNPhysicsShape](scnphysicsshape.md)
  An abstraction of a physics body’s solid volume for tuning collision detection.
### Collision and Contact Detection
- [protocol SCNPhysicsContactDelegate](scnphysicscontactdelegate.md)
  Methods you can implement to respond when a contact or collision occurs between two physics bodies in a scene.
- [class SCNPhysicsContact](scnphysicscontact.md)
  Detailed information about a contact between two physics bodies in a scene’s physics simulation.
### Physics in a Scene
- [class SCNPhysicsWorld](scnphysicsworld.md)
  The global simulation of collisions, gravity, joints, and other physics effects in a scene.
- [class SCNPhysicsField](scnphysicsfield.md)
  An object that applies forces, such as gravitation, electromagnetism, and turbulence, to physics bodies within a certain area of effect.
- [class SCNPhysicsBehavior](scnphysicsbehavior.md)
  The abstract superclass for joints, vehicle simulations, and other high-level behaviors that incorporate multiple physics bodies.
### Joints
- [class SCNPhysicsHingeJoint](scnphysicshingejoint.md)
  A physics behavior that connects two bodies and allows them to pivot around each other on a single axis.
- [class SCNPhysicsSliderJoint](scnphysicssliderjoint.md)
  A physics behavior that connects two bodies and allows them to slide against each other and rotate around their connecting points.
- [class SCNPhysicsBallSocketJoint](scnphysicsballsocketjoint.md)
  A physics behavior that connects two physics bodies and allows them to pivot around each other in any direction.
- [class SCNPhysicsConeTwistJoint](scnphysicsconetwistjoint.md)
### Vehicle Simulation
- [class SCNPhysicsVehicle](scnphysicsvehicle.md)
  A physics behavior that modifies a physics body to behave like a car, motorcycle, or other wheeled vehicle.
- [class SCNPhysicsVehicleWheel](scnphysicsvehiclewheel.md)
  The appearance and physical characteristics of an individual wheel associated with an physics vehicle behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/physics-simulation)*