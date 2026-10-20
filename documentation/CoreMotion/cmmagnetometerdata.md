# CMMagnetometerData

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

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

```objc
@interface CMMagnetometerData : CMLogItem
```

#### Overview

Your application can obtain samples of magnetometer measurements, as represented by instances of this class, from the block handler of the [`startMagnetometerUpdates(to:withHandler:)`](./cmmotionmanager/startmagnetometerupdates%28to,withhandler%29.md) method or from the [`magnetometerData`](./cmmotionmanager/magnetometerdata.md) property of the `CMMotionManager` class.

> **Note**:  The [`magnetometerData`](./cmmotionmanager/magnetometerdata.md) property of `CMMotionManager` provides a non-`nil` value only if you have called the `startMagnetometerUpdates()` method or the [`startMagnetometerUpdates(to:withHandler:)`](./cmmotionmanager/startmagnetometerupdates%28to,withhandler%29.md) method to start magnetometer updates.

## Topics

### Getting the Field Strength
- [var magneticField: CMMagneticField](./cmmagnetometerdata/magneticfield.md)
  Returns the magnetic field measured by the magnetometer.
- [struct CMMagneticField](./cmmagneticfield.md)
  A structure containing 3-axis magnetometer data

## Relationships

### Inherits From
- [CMLogItem](./cmlogitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)*