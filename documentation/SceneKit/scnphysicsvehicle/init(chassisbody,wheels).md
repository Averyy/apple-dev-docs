# init(chassisBody:wheels:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a vehicle behavior.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
convenience init(chassisBody: SCNPhysicsBody, wheels: [SCNPhysicsVehicleWheel])
```

```objc
+ (instancetype) vehicleWithChassisBody:(SCNPhysicsBody *) chassisBody wheels:(NSArray<SCNPhysicsVehicleWheel *> *) wheels;
```

## Return Value

A new vehicle behavior.

## Discussion

Each object in the `wheels` array associates a node with the wheel to serve as its visual representation and defines properties for the wheel’s physical characteristics. Each wheel object must reference a unique node, which should be a child of the node containing the physics body used for the vehicle’s chassis. Typically, you load a node hierarchy representing the vehicle and all of its wheels from a scene file and then designate which nodes serve as the body and wheels.

For a behavior to take effect, you must add it to the physics simulation by calling the [`addBehavior(_:)`](../scnphysicsworld/addbehavior%28_%29.md) method on your scene’s [`SCNPhysicsWorld`](../scnphysicsworld.md) object.

## Parameters

- `chassisBody`: A physics body to serve as the vehicle’s chassis.
- `wheels`: An array of [`SCNPhysicsVehicleWheel`](../scnphysicsvehiclewheel.md) objects representing the vehicle’s wheels. A vehicle must have at least one wheel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/init(chassisbody:wheels:))*