# oxygenSaturation

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A quantity sample type that measures the user’s oxygen saturation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let oxygenSaturation: HKQuantityTypeIdentifier
```

```c
extern HKQuantityTypeIdentifier const HKQuantityTypeIdentifierOxygenSaturation;
```

## Discussion

Oxygen saturation samples measure the percentage of oxygen in the bloodstream. These samples use percent units (described in [`HKUnit`](../hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](../hkquantityaggregationstyle.md)).

## See Also

### Vital signs
- [static let heartRate: HKQuantityTypeIdentifier](./heartrate.md)
  A quantity sample type that measures the user’s heart rate.
- [static let lowHeartRateEvent: HKCategoryTypeIdentifier](../hkcategorytypeidentifier/lowheartrateevent.md)
  A category sample type for low heart rate events.
- [static let highHeartRateEvent: HKCategoryTypeIdentifier](../hkcategorytypeidentifier/highheartrateevent.md)
  A category sample type for high heart rate events.
- [static let irregularHeartRhythmEvent: HKCategoryTypeIdentifier](../hkcategorytypeidentifier/irregularheartrhythmevent.md)
  A category sample type for irregular heart rhythm events.
- [static let restingHeartRate: HKQuantityTypeIdentifier](./restingheartrate.md)
  A quantity sample type that measures the user’s resting heart rate.
- [static let heartRateVariabilitySDNN: HKQuantityTypeIdentifier](./heartratevariabilitysdnn.md)
  A quantity sample type that measures the standard deviation of heartbeat intervals.
- [static let heartRateRecoveryOneMinute: HKQuantityTypeIdentifier](./heartraterecoveryoneminute.md)
  A quantity sample that records the reduction in heart rate from the peak exercise rate to the rate one minute after exercising ended.
- [static let atrialFibrillationBurden: HKQuantityTypeIdentifier](./atrialfibrillationburden.md)
  A quantity type that measures an estimate of the percentage of time a person’s heart shows signs of atrial fibrillation (AFib) while wearing Apple Watch.
- [static let walkingHeartRateAverage: HKQuantityTypeIdentifier](./walkingheartrateaverage.md)
  A quantity sample type that measures the user’s heart rate while walking.
- [let HKDataTypeIdentifierHeartbeatSeries: String](../hkdatatypeidentifierheartbeatseries.md)
  A series sample containing heartbeat data.
- [class HKElectrocardiogramType](../hkelectrocardiogramtype.md)
  A type that identifies samples containing electrocardiogram data.
- [static let bodyTemperature: HKQuantityTypeIdentifier](./bodytemperature.md)
  A quantity sample type that measures the user’s body temperature.
- [static let bloodPressure: HKCorrelationTypeIdentifier](../hkcorrelationtypeidentifier/bloodpressure.md)
  A correlation sample that combines a systolic sample and a diastolic sample into a single blood pressure reading.
- [static let bloodPressureSystolic: HKQuantityTypeIdentifier](./bloodpressuresystolic.md)
  A quantity sample type that measures the user’s systolic blood pressure.
- [static let bloodPressureDiastolic: HKQuantityTypeIdentifier](./bloodpressurediastolic.md)
  A quantity sample type that measures the user’s diastolic blood pressure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/oxygensaturation)*