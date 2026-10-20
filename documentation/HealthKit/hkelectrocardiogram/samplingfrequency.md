# samplingFrequency

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) HKQuantity * samplingFrequency;
```

#### Discussion

The system records the frequency in [`hertz()`](../hkunit/hertz%28%29.md) units.

## See Also

### Accessing Voltage Measurements
- [var numberOfVoltageMeasurements: Int](./numberofvoltagemeasurements.md)
  The number of voltage measurements associated with this sample.
- [HKElectrocardiogram.VoltageMeasurement](./voltagemeasurement.md)
  The voltage for all leads at a single point in time.
- [HKElectrocardiogram.Lead](./lead.md)
  The lead used to record a voltage measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/samplingfrequency)*