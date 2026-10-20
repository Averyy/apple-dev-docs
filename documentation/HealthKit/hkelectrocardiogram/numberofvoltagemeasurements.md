# numberOfVoltageMeasurements

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The number of voltage measurements associated with this sample.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var numberOfVoltageMeasurements: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger numberOfVoltageMeasurements;
```

## See Also

### Accessing Voltage Measurements
- [var samplingFrequency: HKQuantity?](./samplingfrequency.md)
  The frequency at which the Apple Watch sampled the voltage.
- [HKElectrocardiogram.VoltageMeasurement](./voltagemeasurement.md)
  The voltage for all leads at a single point in time.
- [HKElectrocardiogram.Lead](./lead.md)
  The lead used to record a voltage measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/numberofvoltagemeasurements)*