# CMRotationRateData

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

A data object that contains a single rotation-rate measurement.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class CMRotationRateData
```

```objc
@interface CMRotationRateData : CMLogItem
```

## Topics

### Accessing Rotation Data
- [var rotationRate: CMRotationRate](./cmrotationratedata/rotationrate.md)
  The rotation rate measured by the gyroscope.

## Relationships

### Inherits From
- [CMLogItem](./cmlogitem.md)
### Inherited By
- [CMRecordedRotationRateData](./cmrecordedrotationratedata.md)
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
- [class CMRecordedRotationRateData](./cmrecordedrotationratedata.md)
  A data object that contains a single rotation-rate measurement at a specific time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmrotationratedata)*