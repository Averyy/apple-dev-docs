# applyBrakingForce(_:forWheelAt:)

**Framework**: SceneKit  
**Kind**: method

Applies a force between the specified wheel and the ground under the vehicle.

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
func applyBrakingForce(_ value: CGFloat, forWheelAt index: Int)
```

#### Discussion

Applying a braking force causes the wheel to slow down regardless of the direction it’s currently spinning in.

As with all physical quantities in SceneKit, you need not use realistic force measurements in your app—the effects of the physics simulation depend on the relative differences between forces, not on their absolute values. You may use whatever values produce the behavior or gameplay you’re looking for as long as you use them consistently.

Calling this method applies a braking force for one step (or frame) of the physics simulation. To continuously decelerate a vehicle, call this method again on subequent simulation steps (for example, from your scene renderer delegate’s [`renderer(_:updateAtTime:)`](scnscenerendererdelegate/renderer(_:updateattime:).md) method) until the vehicle stops or reaches your desired speed.

## Parameters

- `value`: The magnitude of the torque, in newton-meters.
- `index`: The index of the wheel applying the force.

## See Also

- [func applyEngineForce(CGFloat, forWheelAt: Int)](scnphysicsvehicle/applyengineforce(_:forwheelat:).md)
  Applies a force between the specified wheel and the ground under the vehicle.
- [func setSteeringAngle(CGFloat, forWheelAt: Int)](scnphysicsvehicle/setsteeringangle(_:forwheelat:).md)
  Pivots the specified wheel around its steering axis.
- [var speedInKilometersPerHour: CGFloat](scnphysicsvehicle/speedinkilometersperhour.md)
  The vehicle’s ground speed, in kilometers per hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/applybrakingforce(_:forwheelat:))*