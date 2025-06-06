# applyEngineForce(_:forWheelAt:)

**Framework**: SceneKit  
**Kind**: method

Applies a force between the specified wheel and the ground under the vehicle.

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
func applyEngineForce(_ value: CGFloat, forWheelAt index: Int)
```

#### Discussion

Applying a positive force turns the wheel in a direction that would move the vehicle forward; applying a negative force moves the vehicle in reverse.

As with all physical quantities in SceneKit, you need not use realistic force measurements in your app—the effects of the physics simulation depend on the relative differences between forces, not on their absolute values. You may use whatever values produce the behavior or gameplay you’re looking for as long as you use them consistently.

Calling this method applies a force for one step (or frame) of the physics simulation. To continuously accelerate a vehicle, call this method again on subequent simulation steps (for example, from your scene renderer delegate’s [`renderer(_:updateAtTime:)`](scnscenerendererdelegate/renderer(_:updateattime:).md) method) until the vehicle reaches your desired speed.

## Parameters

- `value`: The magnitude of the force, in newtons.
- `index`: The index of the wheel applying the force.

## See Also

- [func applyBrakingForce(CGFloat, forWheelAt: Int)](scnphysicsvehicle/applybrakingforce(_:forwheelat:).md)
  Applies a force between the specified wheel and the ground under the vehicle.
- [func setSteeringAngle(CGFloat, forWheelAt: Int)](scnphysicsvehicle/setsteeringangle(_:forwheelat:).md)
  Pivots the specified wheel around its steering axis.
- [var speedInKilometersPerHour: CGFloat](scnphysicsvehicle/speedinkilometersperhour.md)
  The vehicle’s ground speed, in kilometers per hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/applyengineforce(_:forwheelat:))*