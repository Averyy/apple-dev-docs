# chassisBody

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The physics body representing the vehicle’s chassis.

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
var chassisBody: SCNPhysicsBody { get }
```

```objc
@property (nonatomic, readonly) SCNPhysicsBody * chassisBody;
```

#### Discussion

The vehicle’s chassis must be a dynamic body.

## See Also

### Working with a Vehicle’s Physical Characteristics
- [var wheels: [SCNPhysicsVehicleWheel]](./wheels.md)
  An array of [`SCNPhysicsVehicleWheel`](../scnphysicsvehiclewheel.md) objects representing the vehicle’s wheels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/chassisbody)*