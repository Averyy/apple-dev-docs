# sensorsActive

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the sensors that compute the motion data are active.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var sensorsActive: Bool { get set }
```

```objc
@property (nonatomic) BOOL sensorsActive;
```

#### Discussion

[`true`](../../Swift/true.md) if the sensors are active; otherwise, [`false`](../../Swift/false.md).

## See Also

### Accessing Sensor Data
- [var sensorsRequireManualActivation: Bool](./sensorsrequiremanualactivation.md)
  A Boolean value that indicates whether the sensors that compute the motion data require manual activation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/sensorsactive)*