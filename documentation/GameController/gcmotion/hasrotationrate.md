# hasRotationRate

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the controller provides rotation data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var hasRotationRate: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasRotationRate;
```

#### Discussion

[`true`](../../Swift/true.md) if the controller provides rotation data; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var rotationRate: GCRotationRate](./rotationrate.md)
  The rotation rate of the controller.
### Verifying Capabilities
- [var hasAttitude: Bool](./hasattitude.md)
  A Boolean value that indicates whether the controller provides attitude data.
- [var hasGravityAndUserAcceleration: Bool](./hasgravityanduseracceleration.md)
  A Boolean value that indicates whether the controller provides gravity and user acceleration data.
- [var hasAttitudeAndRotationRate: Bool](./hasattitudeandrotationrate.md)
  A Boolean value that indicates whether the controller provides attitude and rotation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/hasrotationrate)*