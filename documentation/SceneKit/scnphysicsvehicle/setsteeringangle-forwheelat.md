# setSteeringAngle(_:forWheelAt:)

**Framework**: SceneKit  
**Kind**: method

Pivots the specified wheel around its steering axis.

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
func setSteeringAngle(_ value: CGFloat, forWheelAt index: Int)
```

#### Discussion

Steering angles are relative to the wheel’s [`steeringAxis`](scnphysicsvehiclewheel/steeringaxis.md) vector. With the default steering axis of `{0.0, -1.0, 0.0}`, a steering angle of `0.0` represents neutral steering, positive values steer the vehicle to the right, and negative values steer to the left.

## Parameters

- `value`: The angle to set the wheel at relative to its steering axis, in radians.
- `index`: The index, in the vehicle’s   array, of the wheel to be pivoted.

## See Also

- [func applyEngineForce(CGFloat, forWheelAt: Int)](scnphysicsvehicle/applyengineforce(_:forwheelat:).md)
  Applies a force between the specified wheel and the ground under the vehicle.
- [func applyBrakingForce(CGFloat, forWheelAt: Int)](scnphysicsvehicle/applybrakingforce(_:forwheelat:).md)
  Applies a force between the specified wheel and the ground under the vehicle.
- [var speedInKilometersPerHour: CGFloat](scnphysicsvehicle/speedinkilometersperhour.md)
  The vehicle’s ground speed, in kilometers per hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/setsteeringangle(_:forwheelat:))*