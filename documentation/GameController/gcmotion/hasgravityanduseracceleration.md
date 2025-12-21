# hasGravityAndUserAcceleration

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the controller provides gravity and user acceleration data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var hasGravityAndUserAcceleration: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the controller provides both gravity and user acceleration data; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var gravity: GCAcceleration](gcmotion/gravity.md)
  The gravity acceleration vector from the controller’s reference frame.
- [var userAcceleration: GCAcceleration](gcmotion/useracceleration.md)
  The acceleration that the user applies to the controller.
- [var hasAttitude: Bool](gcmotion/hasattitude.md)
  A Boolean value that indicates whether the controller provides attitude data.
- [var hasRotationRate: Bool](gcmotion/hasrotationrate.md)
  A Boolean value that indicates whether the controller provides rotation data.
- [var hasAttitudeAndRotationRate: Bool](gcmotion/hasattitudeandrotationrate.md)
  A Boolean value that indicates whether the controller provides attitude and rotation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/hasgravityanduseracceleration)*