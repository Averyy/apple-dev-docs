# samplingFrequency

**Framework**: HealthKit  
**Kind**: property

The frequency at which the Apple Watch sampled the voltage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@NSCopying
var samplingFrequency: HKQuantity? { get }
```

#### Discussion

The system records the frequency in [`hertz()`](hkunit/hertz().md) units.

## See Also

- [var numberOfVoltageMeasurements: Int](hkelectrocardiogram/numberofvoltagemeasurements.md)
  The number of voltage measurements associated with this sample.
- [HKElectrocardiogram.VoltageMeasurement](hkelectrocardiogram/voltagemeasurement.md)
  The voltage for all leads at a single point in time.
- [HKElectrocardiogram.Lead](hkelectrocardiogram/lead.md)
  The lead used to record a voltage measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/samplingfrequency)*