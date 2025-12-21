# hasAttitudeAndRotationRate

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the controller provides attitude and rotation data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var hasAttitudeAndRotationRate: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the controller provides attitude and rotation rate data; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var attitude: GCQuaternion](gcmotion/attitude.md)
  The attitude of the controller.
- [var rotationRate: GCRotationRate](gcmotion/rotationrate.md)
  The rotation rate of the controller.
- [var hasAttitude: Bool](gcmotion/hasattitude.md)
  A Boolean value that indicates whether the controller provides attitude data.
- [var hasRotationRate: Bool](gcmotion/hasrotationrate.md)
  A Boolean value that indicates whether the controller provides rotation data.
- [var hasGravityAndUserAcceleration: Bool](gcmotion/hasgravityanduseracceleration.md)
  A Boolean value that indicates whether the controller provides gravity and user acceleration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/hasattitudeandrotationrate)*