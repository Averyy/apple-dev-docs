# HKElectrocardiogram.VoltageMeasurement

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKElectrocardiogramVoltageMeasurement : NSObject
```

## Topics

### Accessing Data
- [func quantity(for: HKElectrocardiogram.Lead) -> HKQuantity?](./voltagemeasurement/quantity%28for%29.md)
  Returns the voltage for the specified lead.
- [var timeSinceSampleStart: TimeInterval](./voltagemeasurement/timesincesamplestart.md)
  The time of the measurement relative to the sample’s start time.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Electrocardiograms
- [class HKElectrocardiogram](../hkelectrocardiogram.md)
  A sample for electrocardiogram data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/voltagemeasurement)*