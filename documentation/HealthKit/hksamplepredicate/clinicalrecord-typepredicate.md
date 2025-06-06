# clinicalRecord(type:predicate:)

**Framework**: HealthKit  
**Kind**: method

Returns a sample predicate that matches clinical record samples.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
static func clinicalRecord(type clinicalType: HKClinicalType, predicate: NSPredicate? = nil) -> HKSamplePredicate<HKClinicalRecord>
```

#### Discussion

Use this method to create an [`HKSamplePredicate`](hksamplepredicate.md) instance that you can use to query for [`HKClinicalRecord`](hkclinicalrecord.md) objects.

## Parameters

- `clinicalType`: A type that matches samples that contain clinical record data.
- `predicate`: An optional predicate that further restricts the results that the query returns.

## See Also

- [static func audiogram(NSPredicate?) -> HKSamplePredicate<HKAudiogramSample>](hksamplepredicate/audiogram(_:).md)
  Returns a sample predicate that matches audiogram samples.
- [static func categorySample(type: HKCategoryType, predicate: NSPredicate?) -> HKSamplePredicate<HKCategorySample>](hksamplepredicate/categorysample(type:predicate:).md)
  Returns a sample predicate that matches category samples.
- [static func correlation(type: HKCorrelationType, predicate: NSPredicate?) -> HKSamplePredicate<HKCorrelation>](hksamplepredicate/correlation(type:predicate:).md)
  Returns a sample predicate that matches samples that contain correlated data.
- [static func electrocardiogram(NSPredicate?) -> HKSamplePredicate<HKElectrocardiogram>](hksamplepredicate/electrocardiogram(_:).md)
  Returns a sample predicate that matches electrocardiogram samples.
- [static func heartbeatSeries(NSPredicate?) -> HKSamplePredicate<HKHeartbeatSeriesSample>](hksamplepredicate/heartbeatseries(_:).md)
  Returns a sample predicate that matches heartbeat series samples.
- [static func quantitySample(type: HKQuantityType, predicate: NSPredicate?) -> HKSamplePredicate<HKQuantitySample>](hksamplepredicate/quantitysample(type:predicate:).md)
  Returns a sample predicate that matches quantity samples.
- [static func sample(type: HKSampleType, predicate: NSPredicate?) -> HKSamplePredicate<HKSample>](hksamplepredicate/sample(type:predicate:).md)
  Returns a sample predicate that matches samples.
- [static func visionPrescription(NSPredicate?) -> HKSamplePredicate<HKVisionPrescription>](hksamplepredicate/visionprescription(_:).md)
  Returns a predicate that matches prescription samples.
- [static func workout(NSPredicate?) -> HKSamplePredicate<HKWorkout>](hksamplepredicate/workout(_:).md)
  Returns a sample predicate that matches workout samples.
- [static func workoutRoute(NSPredicate?) -> HKSamplePredicate<HKWorkoutRoute>](hksamplepredicate/workoutroute(_:).md)
  Returns a sample predicate that matches samples containing workout route data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplepredicate/clinicalrecord(type:predicate:))*