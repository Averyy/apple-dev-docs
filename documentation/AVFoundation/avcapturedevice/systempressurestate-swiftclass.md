# AVCaptureDevice.SystemPressureState

**Framework**: AVFoundation  
**Kind**: class

An object that provides information about OS and hardware status affecting capture system performance and availability.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class SystemPressureState
```

#### Overview

The performance and availability of the camera capture system on an iOS device is subject to several external factors, such as power usage and device temperature. If during a capture session the total system pressure reaches excessive levels, the capture system automatically shuts down, causing a session interruption (see [`wasInterruptedNotification`](avcapturesession/wasinterruptednotification.md)). Under less heavy pressure, the system may automatically reduce capture quality.

Key-value observe the capture device’s [`systemPressureState`](avcapturedevice/systempressurestate-swift.property.md) property to monitor its state, and take action to reduce the performance impact of your capture session when system pressure increases—for example, by reducing the capture frame rate.

## Topics

### Overall Level
- [var level: AVCaptureDevice.SystemPressureState.Level](avcapturedevice/systempressurestate-swift.class/level-swift.property.md)
  The overall level of performance constraints on the capture system.
- [AVCaptureDevice.SystemPressureState.Level](avcapturedevice/systempressurestate-swift.class/level-swift.struct.md)
  A structure that defines system pressure state levels.
### Contributing Factors
- [var factors: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.property.md)
  The set of underlying causes for the system pressure level.
- [AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct.md)
  A structure that defines the factors affecting capture system performance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var systemPressureState: AVCaptureDevice.SystemPressureState](avcapturedevice/systempressurestate-swift.property.md)
  A value that indicates the capture device’s current system pressure state.
- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class)*