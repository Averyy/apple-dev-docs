# visionPrescription(_:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that matches prescription samples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
static func visionPrescription(_ predicate: NSPredicate? = nil) -> HKSamplePredicate<HKVisionPrescription>
```

Available when `Sample` inherits `HKSample`.

#### Discussion

Use this method to create a predicate that matches vision prescriptions.

```swift
// Create a predicate that matches samples stored today.
let end = Date()
let start = Calendar.current.startOfDay(for: Date())
let datePredicate = HKQuery.predicateForSamples(withStart: start, end: end)

// Create a predicate that matches vision prescriptions samples stored today.
let predicate = HKSamplePredicate.visionPrescription(datePredicate)
```

## Parameters

- `predicate`: A predicate that further filters the matching prescriptions.

## See Also

### Creating Sample Predicates
- [static func audiogram(NSPredicate?) -> HKSamplePredicate<HKAudiogramSample>](./audiogram%28_%29.md)
  Returns a sample predicate that matches audiogram samples.
- [static func categorySample(type: HKCategoryType, predicate: NSPredicate?) -> HKSamplePredicate<HKCategorySample>](./categorysample%28type,predicate%29.md)
  Returns a sample predicate that matches category samples.
- [static func clinicalRecord(type: HKClinicalType, predicate: NSPredicate?) -> HKSamplePredicate<HKClinicalRecord>](./clinicalrecord%28type,predicate%29.md)
  Returns a sample predicate that matches clinical record samples.
- [static func correlation(type: HKCorrelationType, predicate: NSPredicate?) -> HKSamplePredicate<HKCorrelation>](./correlation%28type,predicate%29.md)
  Returns a sample predicate that matches samples that contain correlated data.
- [static func electrocardiogram(NSPredicate?) -> HKSamplePredicate<HKElectrocardiogram>](./electrocardiogram%28_%29.md)
  Returns a sample predicate that matches electrocardiogram samples.
- [static func heartbeatSeries(NSPredicate?) -> HKSamplePredicate<HKHeartbeatSeriesSample>](./heartbeatseries%28_%29.md)
  Returns a sample predicate that matches heartbeat series samples.
- [static func quantitySample(type: HKQuantityType, predicate: NSPredicate?) -> HKSamplePredicate<HKQuantitySample>](./quantitysample%28type,predicate%29.md)
  Returns a sample predicate that matches quantity samples.
- [static func sample(type: HKSampleType, predicate: NSPredicate?) -> HKSamplePredicate<HKSample>](./sample%28type,predicate%29.md)
  Returns a sample predicate that matches samples.
- [static func workout(NSPredicate?) -> HKSamplePredicate<HKWorkout>](./workout%28_%29.md)
  Returns a sample predicate that matches workout samples.
- [static func workoutRoute(NSPredicate?) -> HKSamplePredicate<HKWorkoutRoute>](./workoutroute%28_%29.md)
  Returns a sample predicate that matches samples containing workout route data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplepredicate/visionprescription(_:))*