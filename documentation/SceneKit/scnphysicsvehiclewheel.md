# SCNPhysicsVehicleWheel

**Framework**: SceneKit  
**Kind**: class

The appearance and physical characteristics of an individual wheel associated with an physics vehicle behavior.

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
class SCNPhysicsVehicleWheel
```

#### Overview

To use wheels in a vehicle simulation, include them when creating an [`SCNPhysicsVehicle`](scnphysicsvehicle.md) object with the [`init(chassisBody:wheels:)`](scnphysicsvehicle/init(chassisbody:wheels:).md) initializer, then add the vehicle object to your scene’s physics world using the physics world’s [`addBehavior(_:)`](scnphysicsworld/addbehavior(_:).md) method.

##### Creating a Wheel

You create a wheel with an [`SCNNode`](scnnode.md) object whose contents provide the wheel’s visual representation—a geometry that rotates when the simulated vehicle rolls along a surface. The node representing a wheel must be a child of the node containing the physics body that serves as the vehicle’s chassis, and each wheel in a vehicle must reference a unique node. Typically, you load a scene file that contains a node hierarchy representing the vehicle and all of its wheels. Next, you designate which nodes serve as the body and wheels.

Because the [`SCNPhysicsVehicle`](scnphysicsvehicle.md) behavior that a wheel is attached to manages its participation in the physics simulation, you don’t need to attach a physics body to the [`SCNNode`](scnnode.md) object representing a wheel.

##### Changing a Wheels Physical Properties

The properties of a wheel define the geometry of its connection to the vehicle and simulate its size, traction, and suspension. You can change these properties after the wheel and the vehicle containing it have been added to the physics world. In this way, you can simulate effects such as variable suspension and flat tires.

> **Note**:  Vehicles and their wheels have several properties measured in real-world units (meters, centimeters, and newtons) with default values that produce realistic behavior for vehicles of size similar to an average automobile. If you design your scene on a different scale, proportionally change the values of these properties to fit the desired behavior of your app or game.

 Vehicles and their wheels have several properties measured in real-world units (meters, centimeters, and newtons) with default values that produce realistic behavior for vehicles of size similar to an average automobile. If you design your scene on a different scale, proportionally change the values of these properties to fit the desired behavior of your app or game.

## Topics

### Creating a Wheel
- [convenience init(node: SCNNode)](scnphysicsvehiclewheel/init(node:).md)
  Creates a wheel object.
### Managing a Wheel’s Connection to a Vehicle
- [var connectionPosition: SCNVector3](scnphysicsvehiclewheel/connectionposition.md)
  The position of the wheel’s connection to the vehicle’s chassis.
- [var axle: SCNVector3](scnphysicsvehiclewheel/axle.md)
  The direction of the axis that the wheel spins around to move the vehicle.
- [var steeringAxis: SCNVector3](scnphysicsvehiclewheel/steeringaxis.md)
  The direction of the axis that the wheel pivots around to steer the vehicle.
### Simulating Wheel Size
- [var radius: CGFloat](scnphysicsvehiclewheel/radius.md)
  The radius of the wheel.
### Simulating Traction
- [var frictionSlip: CGFloat](scnphysicsvehiclewheel/frictionslip.md)
  The traction between the wheel and any surface in contact with it.
### Simulating Suspension
- [var suspensionStiffness: CGFloat](scnphysicsvehiclewheel/suspensionstiffness.md)
  The spring coefficient of the suspension between the vehicle and the wheel.
- [var suspensionCompression: CGFloat](scnphysicsvehiclewheel/suspensioncompression.md)
  The coefficient that limits the speed of the suspension returning to its rest length when compressed.
- [var suspensionDamping: CGFloat](scnphysicsvehiclewheel/suspensiondamping.md)
  The damping ratio that limits oscillation in the vehicle’s suspension.
- [var maximumSuspensionTravel: CGFloat](scnphysicsvehiclewheel/maximumsuspensiontravel.md)
  The maximum distance that the wheel is allowed to move up or down relative to its connection point, in centimeters.
- [var maximumSuspensionForce: CGFloat](scnphysicsvehiclewheel/maximumsuspensionforce.md)
  The maximum force of the suspension between the vehicle and the wheel, in newtons.
- [var suspensionRestLength: CGFloat](scnphysicsvehiclewheel/suspensionrestlength.md)
  The resting length of the suspension, in meters.
### Inspecting the Wheel Node
- [var node: SCNNode](scnphysicsvehiclewheel/node.md)
  The node providing the wheel’s visual representation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SCNPhysicsVehicle](scnphysicsvehicle.md)
  A physics behavior that modifies a physics body to behave like a car, motorcycle, or other wheeled vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel)*