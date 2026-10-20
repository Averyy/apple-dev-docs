# hasAttitudeAndRotationRate

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the controller provides attitude and rotation data.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.13+ - Deprecated in 11.0
- tvOS 11.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`hasAttitude`](./hasattitude.md) and [`hasRotationRate`](./hasrotationrate.md) methods instead.

## Declaration

```swift
var hasAttitudeAndRotationRate: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasAttitudeAndRotationRate;
```

#### Discussion

[`true`](../../Swift/true.md) if the controller provides attitude and rotation rate data; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var attitude: GCQuaternion](./attitude.md)
  The attitude of the controller.
- [var rotationRate: GCRotationRate](./rotationrate.md)
  The rotation rate of the controller.
### Verifying Capabilities
- [var hasAttitude: Bool](./hasattitude.md)
  A Boolean value that indicates whether the controller provides attitude data.
- [var hasRotationRate: Bool](./hasrotationrate.md)
  A Boolean value that indicates whether the controller provides rotation data.
- [var hasGravityAndUserAcceleration: Bool](./hasgravityanduseracceleration.md)
  A Boolean value that indicates whether the controller provides gravity and user acceleration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/hasattitudeandrotationrate)*