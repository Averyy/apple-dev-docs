# AVCaptureDevice.SystemPressureState

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptureSystemPressureState : NSObject
```

#### Overview

The performance and availability of the camera capture system on an iOS device is subject to several external factors, such as power usage and device temperature. If during a capture session the total system pressure reaches excessive levels, the capture system automatically shuts down, causing a session interruption (see [`wasInterruptedNotification`](../avcapturesession/wasinterruptednotification.md)). Under less heavy pressure, the system may automatically reduce capture quality.

Key-value observe the capture device’s [`systemPressureState`](./systempressurestate-swift.property.md) property to monitor its state, and take action to reduce the performance impact of your capture session when system pressure increases—for example, by reducing the capture frame rate.

## Topics

### Overall level
- [var level: AVCaptureDevice.SystemPressureState.Level](./systempressurestate-swift.class/level-swift.property.md)
  The overall level of performance constraints on the capture system.
- [AVCaptureDevice.SystemPressureState.Level](./systempressurestate-swift.class/level-swift.struct.md)
  A structure that defines system pressure state levels.
### Contributing factors
- [var factors: AVCaptureDevice.SystemPressureState.Factors](./systempressurestate-swift.class/factors-swift.property.md)
  The set of underlying causes for the system pressure level.
- [AVCaptureDevice.SystemPressureState.Factors](./systempressurestate-swift.class/factors-swift.struct.md)
  A structure that defines the factors affecting capture system performance.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Monitoring system pressure
- [var systemPressureState: AVCaptureDevice.SystemPressureState](./systempressurestate-swift.property.md)
  A value that indicates the capture device’s current system pressure state.
- [let AVCaptureSessionInterruptionSystemPressureStateKey: String](../avcapturesessioninterruptionsystempressurestatekey.md)
  A key to retrieve a state value that indicates the system pressure level and contributing factors that caused the interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class)*