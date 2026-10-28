# applyEngineForce(_:forWheelAt:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Applies a force between the specified wheel and the ground under the vehicle.

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
func applyEngineForce(_ value: CGFloat, forWheelAt index: Int)
```

```objc
- (void) applyEngineForce:(CGFloat) value forWheelAtIndex:(NSInteger) index;
```

## Discussion

Applying a positive force turns the wheel in a direction that would move the vehicle forward; applying a negative force moves the vehicle in reverse.

As with all physical quantities in SceneKit, you need not use realistic force measurements in your app—the effects of the physics simulation depend on the relative differences between forces, not on their absolute values. You may use whatever values produce the behavior or gameplay you’re looking for as long as you use them consistently.

Calling this method applies a force for one step (or frame) of the physics simulation. To continuously accelerate a vehicle, call this method again on subequent simulation steps (for example, from your scene renderer delegate’s [`renderer(_:updateAtTime:)`](../scnscenerendererdelegate/renderer%28_,updateattime%29.md) method) until the vehicle reaches your desired speed.

## Parameters

- `value`: The magnitude of the force, in newtons.
- `index`: The index of the wheel applying the force.

## See Also

### Driving a Vehicle
- [func applyBrakingForce(CGFloat, forWheelAt: Int)](./applybrakingforce%28_,forwheelat%29.md)
  Applies a force between the specified wheel and the ground under the vehicle.
- [func setSteeringAngle(CGFloat, forWheelAt: Int)](./setsteeringangle%28_,forwheelat%29.md)
  Pivots the specified wheel around its steering axis.
- [var speedInKilometersPerHour: CGFloat](./speedinkilometersperhour.md)
  The vehicle’s ground speed, in kilometers per hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/applyengineforce(_:forwheelat:))*