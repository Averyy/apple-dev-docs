# CMLogItem

**Framework**: Core Motion  
**Kind**: class

The base class for all motion-related data objects.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CMLogItem
```

#### Overview

The `CMLogItem` class defines a read-only [`timestamp`](cmlogitem/timestamp.md) property that records the time a motion-event measurement was taken.

## Topics

### Getting the Time of the Event
- [var timestamp: TimeInterval](cmlogitem/timestamp.md)
  The time when the logged item is valid.
### Initializers
- [init?(coder: NSCoder)](cmlogitem/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [CMAbsoluteAltitudeData](cmabsolutealtitudedata.md)
- [CMAccelerometerData](cmaccelerometerdata.md)
- [CMAltitudeData](cmaltitudedata.md)
- [CMAmbientPressureData](cmambientpressuredata.md)
- [CMDeviceMotion](cmdevicemotion.md)
- [CMGyroData](cmgyrodata.md)
- [CMHighFrequencyHeartRateData](cmhighfrequencyheartratedata.md)
- [CMMagnetometerData](cmmagnetometerdata.md)
- [CMMotionActivity](cmmotionactivity.md)
- [CMRotationRateData](cmrotationratedata.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmlogitem)*