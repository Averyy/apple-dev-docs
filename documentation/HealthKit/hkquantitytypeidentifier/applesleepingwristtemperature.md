# appleSleepingWristTemperature

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that records the wrist temperature during sleep.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let appleSleepingWristTemperature: HKQuantityTypeIdentifier
```

#### Discussion

Apple Watch Series 8 and Apple Watch Ultra can sample a person’s wrist temperature while they sleep. A supported watch measures temperature from both sensors every five seconds overnight during sleep. The watch then aggregates this data to a single [`appleSleepingWristTemperature`](hkquantitytypeidentifier/applesleepingwristtemperature.md) sample. It corrects this sample for environmental bias and calculates a single value that represents the wrist temperature over the entire night.

Body temperature naturally fluctuates from night to night, and external factors, like the sleep environment, can also affect the measurements. Other factors that can affect a person’s relative temperature include exercise, jet lag, menstrual cycles, or illness.

Cycle tracking uses a person’s sleeping wrist temperature data to provide a retrospective estimate of when they likely ovulated. It also combines this data with heart rate and logged cycle data to provide improved predictions about their cycle.

To enable sleeping wrist temperature measurements, ensure Sleep Focus is on and that someone is wearing Apple Watch while sleeping.

Apple Watch records the absolute wrist temperature value; however, Health displays this data as a relative value, based on a person’s baseline. Health needs to calculate this baseline, so it won’t display the wrist temperature until it has gathered about five nights of data. However, Apple Watch records [`appleSleepingWristTemperature`](hkquantitytypeidentifier/applesleepingwristtemperature.md) samples starting with the first night, and you can read them immediately from the HealthKit store.

Sleeping wrist temperature samples use temperature units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)).

> ❗ **Important**:  These samples are read-only. You can request permission to read the samples using this identifier, but you can’t request authorization to share them. This means you can’t save new sleeping wrist temperature samples to the HealthKit store.

## See Also

- [static let mindfulSession: HKCategoryTypeIdentifier](hkcategorytypeidentifier/mindfulsession.md)
  A category sample type for recording a mindful session.
- [static let sleepAnalysis: HKCategoryTypeIdentifier](hkcategorytypeidentifier/sleepanalysis.md)
  A category sample type for sleep analysis information.
- [enum HKAppleSleepingBreathingDisturbancesClassification](hkapplesleepingbreathingdisturbancesclassification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/applesleepingwristtemperature)*