# irregularHeartRhythmEvent

**Framework**: HealthKit  
**Kind**: property

A category sample type for irregular heart rhythm events.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
static let irregularHeartRhythmEvent: HKCategoryTypeIdentifier
```

#### Discussion

The system creates [`irregularHeartRhythmEvent`](hkcategorytypeidentifier/irregularheartrhythmevent.md) samples whenever Apple Watch produces an irregular rhythm notification. For more information, see [`Heart rate notifications on your Apple Watch`](https://developer.apple.comhttps://support.apple.com/en-us/HT208931).

The irregular rhythm samples are read-only. You can request permission to read the samples using this identifier, but you can’t request authorization to share them. This means you can’t save new irregular rhythm events to the HealthKit store. To add test data in iOS Simulator, open the Health app and select Browse > Heart > Irregular Rhythm Notifications > Add Data.

These samples have a value of [`HKCategoryValue.notApplicable`](hkcategoryvalue/notapplicable.md).

## See Also

- [static let heartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartrate.md)
  A quantity sample type that measures the user’s heart rate.
- [static let lowHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/lowheartrateevent.md)
  A category sample type for low heart rate events.
- [static let highHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/highheartrateevent.md)
  A category sample type for high heart rate events.
- [static let restingHeartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/restingheartrate.md)
  A quantity sample type that measures the user’s resting heart rate.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/irregularheartrhythmevent)*