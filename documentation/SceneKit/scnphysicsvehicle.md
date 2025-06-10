# SCNPhysicsVehicle

**Framework**: SceneKit  
**Kind**: class

A physics behavior that modifies a physics body to behave like a car, motorcycle, or other wheeled vehicle.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class SCNPhysicsVehicle
```

#### Overview

To build a vehicle, designate an [`SCNPhysicsBody`](scnphysicsbody.md) object as its chassis and an array of [`SCNPhysicsVehicleWheel`](scnphysicsvehiclewheel.md) objects as its wheels. For each wheel, you define physical characteristics such as suspension and traction, and associate a node in your scene to provide the wheel’s size and visual representation. After you construct a vehicle, you can control it in terms of acceleration, braking, and steering.

Although it’s also possible to use a set of physics bodies and joints to collectively simulate a wheeled vehicle, the [`SCNPhysicsVehicle`](scnphysicsvehicle.md) class implements a higher-level simulation that provides realistic vehicle behavior with more efficient simulation performance.

## Topics

### Creating a Vehicle
- [convenience init(chassisBody: SCNPhysicsBody, wheels: [SCNPhysicsVehicleWheel])](scnphysicsvehicle/init(chassisbody:wheels:).md)
  Creates a vehicle behavior.
### Working with a Vehicle’s Physical Characteristics
- [var chassisBody: SCNPhysicsBody](scnphysicsvehicle/chassisbody.md)
  The physics body representing the vehicle’s chassis.
- [var wheels: [SCNPhysicsVehicleWheel]](scnphysicsvehicle/wheels.md)
  An array of [`SCNPhysicsVehicleWheel`](scnphysicsvehiclewheel.md) objects representing the vehicle’s wheels.
### Driving a Vehicle
- [func applyEngineForce(CGFloat, forWheelAt: Int)](scnphysicsvehicle/applyengineforce(_:forwheelat:).md)
  Applies a force between the specified wheel and the ground under the vehicle.
- [func applyBrakingForce(CGFloat, forWheelAt: Int)](scnphysicsvehicle/applybrakingforce(_:forwheelat:).md)
  Applies a force between the specified wheel and the ground under the vehicle.
- [func setSteeringAngle(CGFloat, forWheelAt: Int)](scnphysicsvehicle/setsteeringangle(_:forwheelat:).md)
  Pivots the specified wheel around its steering axis.
- [var speedInKilometersPerHour: CGFloat](scnphysicsvehicle/speedinkilometersperhour.md)
  The vehicle’s ground speed, in kilometers per hour.

## Relationships

### Inherits From
- [SCNPhysicsBehavior](scnphysicsbehavior.md)
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

- [class SCNPhysicsVehicleWheel](scnphysicsvehiclewheel.md)
  The appearance and physical characteristics of an individual wheel associated with an physics vehicle behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle)*