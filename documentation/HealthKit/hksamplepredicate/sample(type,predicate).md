# sample(type:predicate:)

**Framework**: HealthKit  
**Kind**: method

Returns a sample predicate that matches samples.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
static func sample(type sampleType: HKSampleType, predicate: NSPredicate? = nil) -> HKSamplePredicate<HKSample>
```

#### Discussion

Use this method to create an [`HKSamplePredicate`](hksamplepredicate.md) instance that you can use to query for a heterogenous set of sample types.

```swift
let stepType = HKQuantityType(.stepCount)
// Normally, you'd create a quantity predicate for step counts.
let stepPredicate = HKSamplePredicate.sample(type: stepType)

let highHeartRateType = HKCategoryType(.highHeartRateEvent)
// Normally, you'd create a category predicate for high heart rate events.
let highHeartRatePredicate = HKSamplePredicate.sample(type: highHeartRateType)

// By using sample predicates, you can query for different sample types.
let descriptor = HKSampleQueryDescriptor(
    predicates: [stepPredicate, highHeartRatePredicate],
    sortDescriptors: [],
    limit: 10)

// However, the results are an array of HKSample objects.
// You'll need to downcast them to access the data.
let results = try await descriptor.result(for: store)
```

## Parameters

- `sampleType`: A type that matches samples.
- `predicate`: An optional predicate that further restricts the results that the query returns.

## See Also

- [static func audiogram(NSPredicate?) -> HKSamplePredicate<HKAudiogramSample>](hksamplepredicate/audiogram(_:).md)
  Returns a sample predicate that matches audiogram samples.
- [static func categorySample(type: HKCategoryType, predicate: NSPredicate?) -> HKSamplePredicate<HKCategorySample>](hksamplepredicate/categorysample(type:predicate:).md)
  Returns a sample predicate that matches category samples.
- [static func clinicalRecord(type: HKClinicalType, predicate: NSPredicate?) -> HKSamplePredicate<HKClinicalRecord>](hksamplepredicate/clinicalrecord(type:predicate:).md)
  Returns a sample predicate that matches clinical record samples.
- [static func correlation(type: HKCorrelationType, predicate: NSPredicate?) -> HKSamplePredicate<HKCorrelation>](hksamplepredicate/correlation(type:predicate:).md)
  Returns a sample predicate that matches samples that contain correlated data.
- [static func electrocardiogram(NSPredicate?) -> HKSamplePredicate<HKElectrocardiogram>](hksamplepredicate/electrocardiogram(_:).md)
  Returns a sample predicate that matches electrocardiogram samples.
- [static func heartbeatSeries(NSPredicate?) -> HKSamplePredicate<HKHeartbeatSeriesSample>](hksamplepredicate/heartbeatseries(_:).md)
  Returns a sample predicate that matches heartbeat series samples.
- [static func quantitySample(type: HKQuantityType, predicate: NSPredicate?) -> HKSamplePredicate<HKQuantitySample>](hksamplepredicate/quantitysample(type:predicate:).md)
  Returns a sample predicate that matches quantity samples.
- [static func visionPrescription(NSPredicate?) -> HKSamplePredicate<HKVisionPrescription>](hksamplepredicate/visionprescription(_:).md)
  Returns a predicate that matches prescription samples.
- [static func workout(NSPredicate?) -> HKSamplePredicate<HKWorkout>](hksamplepredicate/workout(_:).md)
  Returns a sample predicate that matches workout samples.
- [static func workoutRoute(NSPredicate?) -> HKSamplePredicate<HKWorkoutRoute>](hksamplepredicate/workoutroute(_:).md)
  Returns a sample predicate that matches samples containing workout route data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplepredicate/sample(type:predicate:))*