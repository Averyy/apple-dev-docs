# restingHeartRate

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that measures the user’s resting heart rate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static let restingHeartRate: HKQuantityTypeIdentifier
```

#### Discussion

These samples use count/time units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)).

Resting heart rate is commonly correlated with overall cardiovascular health. It is an estimation of  the user’s lowest heart rate during periods of rest, and is intended to be used as a medically relevant metric. A resting heart rate sample is different than a sedentary heart rate sample (that is, a sample using the [`heartRate`](hkquantitytypeidentifier/heartrate.md) identifier with a [`HKHeartRateMotionContext.sedentary`](hkheartratemotioncontext/sedentary.md) motion context). For example, if the user finishes a high-intensity workout, and then sits down to rest, the next heart rate sample may be marked as a sedentary sample, but it is still much higher than the user’s actual resting heart rate. To produce more accurate results, the system estimates the resting heart rate by analyzing sedentary heart rate samples throughout the day.

Because the resting heart rate estimates become more accurate as the day progresses, the system may delete earlier samples and replace them with better estimates. Apple Watch replaces only the samples written by the watch for the current or previous day.

## See Also

- [static let heartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartrate.md)
  A quantity sample type that measures the user’s heart rate.
- [static let lowHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/lowheartrateevent.md)
  A category sample type for low heart rate events.
- [static let highHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/highheartrateevent.md)
  A category sample type for high heart rate events.
- [static let irregularHeartRhythmEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/irregularheartrhythmevent.md)
  A category sample type for irregular heart rhythm events.
- [static let heartRateVariabilitySDNN: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartratevariabilitysdnn.md)
  A quantity sample type that measures the standard deviation of heartbeat intervals.
- [static let heartRateRecoveryOneMinute: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartraterecoveryoneminute.md)
  A quantity sample that records the reduction in heart rate from the peak exercise rate to the rate one minute after exercising ended.
- [static let atrialFibrillationBurden: HKQuantityTypeIdentifier](hkquantitytypeidentifier/atrialfibrillationburden.md)
  A quantity type that measures an estimate of the percentage of time a person’s heart shows signs of atrial fibrillation (AFib) while wearing Apple Watch.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/restingheartrate)*