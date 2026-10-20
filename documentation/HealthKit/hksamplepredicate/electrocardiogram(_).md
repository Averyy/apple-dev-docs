# electrocardiogram(_:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a sample predicate that matches electrocardiogram samples.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
static func electrocardiogram(_ predicate: NSPredicate? = nil) -> HKSamplePredicate<HKElectrocardiogram>
```

#### Discussion

Use this method to create an [`HKSamplePredicate`](../hksamplepredicate.md) instance that you can use to query for [`HKElectrocardiogram`](../hkelectrocardiogram.md) objects.

## Parameters

- `predicate`: An optional predicate that further restricts the results that the query returns.

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
- [static func heartbeatSeries(NSPredicate?) -> HKSamplePredicate<HKHeartbeatSeriesSample>](./heartbeatseries%28_%29.md)
  Returns a sample predicate that matches heartbeat series samples.
- [static func quantitySample(type: HKQuantityType, predicate: NSPredicate?) -> HKSamplePredicate<HKQuantitySample>](./quantitysample%28type,predicate%29.md)
  Returns a sample predicate that matches quantity samples.
- [static func sample(type: HKSampleType, predicate: NSPredicate?) -> HKSamplePredicate<HKSample>](./sample%28type,predicate%29.md)
  Returns a sample predicate that matches samples.
- [static func visionPrescription(NSPredicate?) -> HKSamplePredicate<HKVisionPrescription>](./visionprescription%28_%29.md)
  Returns a predicate that matches prescription samples.
- [static func workout(NSPredicate?) -> HKSamplePredicate<HKWorkout>](./workout%28_%29.md)
  Returns a sample predicate that matches workout samples.
- [static func workoutRoute(NSPredicate?) -> HKSamplePredicate<HKWorkoutRoute>](./workoutroute%28_%29.md)
  Returns a sample predicate that matches samples containing workout route data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplepredicate/electrocardiogram(_:))*