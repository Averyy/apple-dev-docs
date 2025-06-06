# SCNPhysicsBehavior

**Framework**: SceneKit  
**Kind**: class

The abstract superclass for joints, vehicle simulations, and other high-level behaviors that incorporate multiple physics bodies.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SCNPhysicsBehavior
```

#### Overview

An [`SCNPhysicsBehavior`](scnphysicsbehavior.md) object defines a high-level behavior for one or more physics bodies, modifying the results of the physics simulation. Behaviors include joints that connect multiple bodies so they move together and vehicle definitions that cause a body to roll like a car. You never use this class directly; instead, you instantiate one of the subclasses that defines the kind of behavior you want to add to your physics world. describes the kinds of behaviors you can create in SceneKit.

| Class Name | Description |
| --- | --- |
| [`SCNPhysicsHingeJoint`](scnphysicshingejoint.md) | Connects two bodies and allows them to pivot around each other on a single axis. |
| [`SCNPhysicsBallSocketJoint`](scnphysicsballsocketjoint.md) | Connects two bodies and allows them to pivot around each other in any direction. |
| [`SCNPhysicsSliderJoint`](scnphysicssliderjoint.md) | Connects two bodies and allows them to slide or rotate relative to one another. Slider joints can also work as motors, applying a force or torque between the two bodies. |
| [`SCNPhysicsVehicle`](scnphysicsvehicle.md) | Simulates a physics body as the chassis of a car or other wheeled vehicle. You control a vehicle in terms of steering, braking, and acceleration, and use [`SCNPhysicsVehicleWheel`](scnphysicsvehiclewheel.md) objects to define the appearance and physical properties of each of its wheels. |

To use a physics behavior, you follow these steps:

1. Create [`SCNPhysicsBody`](scnphysicsbody.md) objects and attach them to each node that participates in the behavior.
2. Create and configure a behavior object using one of the subclasses listed in Table 1.
3. Add the behavior to the physics simulation by calling the [`addBehavior(_:)`](scnphysicsworld/addbehavior(_:).md) method on your scene’s [`SCNPhysicsWorld`](scnphysicsworld.md) object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SCNPhysicsBallSocketJoint](scnphysicsballsocketjoint.md)
- [SCNPhysicsConeTwistJoint](scnphysicsconetwistjoint.md)
- [SCNPhysicsHingeJoint](scnphysicshingejoint.md)
- [SCNPhysicsSliderJoint](scnphysicssliderjoint.md)
- [SCNPhysicsVehicle](scnphysicsvehicle.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SCNPhysicsWorld](scnphysicsworld.md)
  The global simulation of collisions, gravity, joints, and other physics effects in a scene.
- [class SCNPhysicsField](scnphysicsfield.md)
  An object that applies forces, such as gravitation, electromagnetism, and turbulence, to physics bodies within a certain area of effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbehavior)*