# HKElectrocardiogram.Lead

**Framework**: HealthKit  
**Kind**: enum

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

## Topics

### Leads
- [HKElectrocardiogram.Lead.appleWatchSimilarToLeadI](hkelectrocardiogram/lead/applewatchsimilartoleadi.md)
  Apple Watch Series 4 or later.
### Initializers
- [init?(rawValue: Int)](hkelectrocardiogram/lead/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var numberOfVoltageMeasurements: Int](hkelectrocardiogram/numberofvoltagemeasurements.md)
  The number of voltage measurements associated with this sample.
- [var samplingFrequency: HKQuantity?](hkelectrocardiogram/samplingfrequency.md)
  The frequency at which the Apple Watch sampled the voltage.
- [HKElectrocardiogram.VoltageMeasurement](hkelectrocardiogram/voltagemeasurement.md)
  The voltage for all leads at a single point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/lead)*