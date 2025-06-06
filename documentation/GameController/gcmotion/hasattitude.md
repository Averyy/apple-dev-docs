# hasAttitude

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the controller provides attitude data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var hasAttitude: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the controller provides attitude data; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var attitude: GCQuaternion](gcmotion/attitude.md)
  The attitude of the controller.
- [var hasRotationRate: Bool](gcmotion/hasrotationrate.md)
  A Boolean value that indicates whether the controller provides rotation data.
- [var hasGravityAndUserAcceleration: Bool](gcmotion/hasgravityanduseracceleration.md)
  A Boolean value that indicates whether the controller provides gravity and user acceleration data.
- [var hasAttitudeAndRotationRate: Bool](gcmotion/hasattitudeandrotationrate.md)
  A Boolean value that indicates whether the controller provides attitude and rotation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/hasattitude)*