# CMGyroData

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

A single measurement of the device’s rotation rate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CMGyroData
```

```objc
@interface CMGyroData : CMLogItem
```

## Overview

An application receives or samples `CMGyroData` objects at regular intervals after calling the [`startGyroUpdates(to:withHandler:)`](./cmmotionmanager/startgyroupdates%28to,withhandler%29.md) method or the [`startGyroUpdates()`](./cmmotionmanager/startgyroupdates%28%29.md) method of the [`CMMotionManager`](./cmmotionmanager.md) class.

## Topics

### Getting the Rotation Rate
- [var rotationRate: CMRotationRate](./cmgyrodata/rotationrate.md)
  The rotation rate as measured by the device’s gyroscope.
- [struct CMRotationRate](./cmrotationrate.md)
  The type of structures representing a measurement of rotation rate.
- [class CMRotationRateData](./cmrotationratedata.md)
  A data object that contains a single rotation-rate measurement.
- [class CMRecordedRotationRateData](./cmrecordedrotationratedata.md)
  A data object that contains a single rotation-rate measurement at a specific time.

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

## See Also

### Gyroscopes
- [Getting raw gyroscope events](./getting-raw-gyroscope-events.md)
  Retrieve data from the onboard gyroscopes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmgyrodata)*