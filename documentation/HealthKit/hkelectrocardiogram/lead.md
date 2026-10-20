# HKElectrocardiogram.Lead

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

The lead used to record a voltage measurement.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum Lead
```

```c
enum HKElectrocardiogramLead : NSInteger;
```

## Topics

### Leads
- [HKElectrocardiogram.Lead.appleWatchSimilarToLeadI](./lead/applewatchsimilartoleadi.md)
  Apple Watch Series 4 or later.
### Initializers
- [init?(rawValue: Int)](./lead/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Voltage Measurements
- [var numberOfVoltageMeasurements: Int](./numberofvoltagemeasurements.md)
  The number of voltage measurements associated with this sample.
- [var samplingFrequency: HKQuantity?](./samplingfrequency.md)
  The frequency at which the Apple Watch sampled the voltage.
- [HKElectrocardiogram.VoltageMeasurement](./voltagemeasurement.md)
  The voltage for all leads at a single point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/lead)*