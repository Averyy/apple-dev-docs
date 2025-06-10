# CMMagnetometerData

**Framework**: Core Motion  
**Kind**: class

Measurements of the Earth’s magnetic field relative to the device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
class CMMagnetometerData
```

#### Overview

Your application can obtain samples of magnetometer measurements, as represented by instances of this class, from the block handler of the [`startMagnetometerUpdates(to:withHandler:)`](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md) method or from the [`magnetometerData`](cmmotionmanager/magnetometerdata.md) property of the `CMMotionManager` class.

> **Note**:  The [`magnetometerData`](cmmotionmanager/magnetometerdata.md) property of `CMMotionManager` provides a non-`nil` value only if you have called the `startMagnetometerUpdates()` method or the [`startMagnetometerUpdates(to:withHandler:)`](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md) method to start magnetometer updates.

## Topics

### Getting the Field Strength
- [var magneticField: CMMagneticField](cmmagnetometerdata/magneticfield.md)
  Returns the magnetic field measured by the magnetometer.
- [struct CMMagneticField](cmmagneticfield.md)
  A structure containing 3-axis magnetometer data

## Relationships

### Inherits From
- [CMLogItem](cmlogitem.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)*