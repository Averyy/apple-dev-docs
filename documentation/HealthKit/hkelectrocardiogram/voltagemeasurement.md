# HKElectrocardiogram.VoltageMeasurement

**Framework**: HealthKit  
**Kind**: class

The voltage for all leads at a single point in time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class VoltageMeasurement
```

## Topics

### Accessing Data
- [func quantity(for: HKElectrocardiogram.Lead) -> HKQuantity?](hkelectrocardiogram/voltagemeasurement/quantity(for:).md)
  Returns the voltage for the specified lead.
- [var timeSinceSampleStart: TimeInterval](hkelectrocardiogram/voltagemeasurement/timesincesamplestart.md)
  The time of the measurement relative to the sample’s start time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HKElectrocardiogram](hkelectrocardiogram.md)
  A sample for electrocardiogram data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/voltagemeasurement)*