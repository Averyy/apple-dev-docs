# CMRecordedRotationRateData

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

A data object that contains a single rotation-rate measurement at a specific time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class CMRecordedRotationRateData
```

```objc
@interface CMRecordedRotationRateData : CMRotationRateData
```

## Topics

### Accessing Rotation Data
- [var startDate: Date](./cmrecordedrotationratedata/startdate.md)
  The time when the gyroscope measured the rotation data.

## Relationships

### Inherits From
- [CMRotationRateData](./cmrotationratedata.md)
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

### Getting the Rotation Rate
- [var rotationRate: CMRotationRate](./cmgyrodata/rotationrate.md)
  The rotation rate as measured by the device’s gyroscope.
- [struct CMRotationRate](./cmrotationrate.md)
  The type of structures representing a measurement of rotation rate.
- [class CMRotationRateData](./cmrotationratedata.md)
  A data object that contains a single rotation-rate measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmrecordedrotationratedata)*