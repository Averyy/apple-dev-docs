# atrialFibrillationBurden

**Framework**: HealthKit  
**Kind**: property

A quantity type that measures an estimate of the percentage of time a person’s heart shows signs of atrial fibrillation (AFib) while wearing Apple Watch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let atrialFibrillationBurden: HKQuantityTypeIdentifier
```

#### Discussion

On watchOS 9 and iOS 16 and later, once a person enables AFib History, Apple Watch begins collecting heart-rhythm data more frequently. iPhone then calculates the AFib burden once a week, as long as Apple Watch has gathered enough heart-rhythm data during that week.

If iPhone is unlocked and isn’t under heavy load, it starts analyzing heart rhythm samples around 8:00 am Monday morning. As soon as it finishes this analysis, iPhone sends the user a notification telling them the results.

These samples use percentage units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)). The sample’s value represents an estimate of the percentage of time a person’s heart shows signs of AFib while wearing Apple Watch.

> ❗ **Important**:  These samples are read-only. You can request permission to read the samples using this identifier, but you can’t request authorization to share them. This means you can’t save new AFib burden samples to the HealthKit store.

## See Also

- [static let heartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartrate.md)
  A quantity sample type that measures the user’s heart rate.
- [static let lowHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/lowheartrateevent.md)
  A category sample type for low heart rate events.
- [static let highHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/highheartrateevent.md)
  A category sample type for high heart rate events.
- [static let irregularHeartRhythmEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/irregularheartrhythmevent.md)
  A category sample type for irregular heart rhythm events.
- [static let restingHeartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/restingheartrate.md)
  A quantity sample type that measures the user’s resting heart rate.
- [static let heartRateVariabilitySDNN: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartratevariabilitysdnn.md)
  A quantity sample type that measures the standard deviation of heartbeat intervals.
- [static let heartRateRecoveryOneMinute: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartraterecoveryoneminute.md)
  A quantity sample that records the reduction in heart rate from the peak exercise rate to the rate one minute after exercising ended.
- [static let walkingHeartRateAverage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingheartrateaverage.md)
  A quantity sample type that measures the user’s heart rate while walking.
- [let HKDataTypeIdentifierHeartbeatSeries: String](hkdatatypeidentifierheartbeatseries.md)
  A series sample containing heartbeat data.
- [class HKElectrocardiogramType](hkelectrocardiogramtype.md)
  A type that identifies samples containing electrocardiogram data.
- [static let oxygenSaturation: HKQuantityTypeIdentifier](hkquantitytypeidentifier/oxygensaturation.md)
  A quantity sample type that measures the user’s oxygen saturation.
- [static let bodyTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bodytemperature.md)
  A quantity sample type that measures the user’s body temperature.
- [static let bloodPressure: HKCorrelationTypeIdentifier](hkcorrelationtypeidentifier/bloodpressure.md)
  A correlation sample that combines a systolic sample and a diastolic sample into a single blood pressure reading.
- [static let bloodPressureSystolic: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodpressuresystolic.md)
  A quantity sample type that measures the user’s systolic blood pressure.
- [static let bloodPressureDiastolic: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodpressurediastolic.md)
  A quantity sample type that measures the user’s diastolic blood pressure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/atrialfibrillationburden)*