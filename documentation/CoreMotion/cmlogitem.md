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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmlogitem)*