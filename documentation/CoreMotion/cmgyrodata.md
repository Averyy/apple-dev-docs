# CMGyroData

**Framework**: Core Motion  
**Kind**: class

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

#### Overview

An application receives or samples `CMGyroData` objects at regular intervals after calling the [`startGyroUpdates(to:withHandler:)`](cmmotionmanager/startgyroupdates(to:withhandler:).md) method or the [`startGyroUpdates()`](cmmotionmanager/startgyroupdates().md) method of the [`CMMotionManager`](cmmotionmanager.md) class.

## Topics

### Getting the Rotation Rate
- [var rotationRate: CMRotationRate](cmgyrodata/rotationrate.md)
  The rotation rate as measured by the device’s gyroscope.
- [struct CMRotationRate](cmrotationrate.md)
  The type of structures representing a measurement of rotation rate.
- [class CMRotationRateData](cmrotationratedata.md)
  A data object that contains a single rotation-rate measurement.
- [class CMRecordedRotationRateData](cmrecordedrotationratedata.md)
  A data object that contains a single rotation-rate measurement at a specific time.

## Relationships

### Inherits From
- [CMLogItem](cmlogitem.md)
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

## See Also

- [Getting raw gyroscope events](getting-raw-gyroscope-events.md)
  Retrieve data from the onboard gyroscopes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmgyrodata)*