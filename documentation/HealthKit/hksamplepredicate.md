# HKSamplePredicate

**Framework**: HealthKit  
**Kind**: struct

A predicate for queries that return a collection of matching sample objects.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct HKSamplePredicate<Sample> where Sample : HKSample
```

#### Overview

The [`HKSamplePredicate`](hksamplepredicate.md) structure bundles an [`HKSampleType`](hksampletype.md) and an optional [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate). The structure is generic. You can create it for any [`HKSampleType`](hksampletype.md) subclass, and it automatically sets the `Sample` type to the matching [`HKSampleType`](hksampletype.md) subtype. As a result, any query that you build using this structure returns properly typed results.

To create an [`HKSamplePredicate`](hksamplepredicate.md) instance, call one of its constructor methods.

```swift
let stepType = HKQuantityType(.stepCount)
let predicate = HKSamplePredicate.quantitySample(type: stepType)

let descriptor = HKSampleQueryDescriptor(
    predicates:[predicate],
    sortDescriptors: [],
    limit: 10)

// The results are an array of HKQuantitySample objects.
let results = try await descriptor.result(for: store)
```

## Topics

### Creating Sample Predicates
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
- [static func sample(type: HKSampleType, predicate: NSPredicate?) -> HKSamplePredicate<HKSample>](hksamplepredicate/sample(type:predicate:).md)
  Returns a sample predicate that matches samples.
- [static func visionPrescription(NSPredicate?) -> HKSamplePredicate<HKVisionPrescription>](hksamplepredicate/visionprescription(_:).md)
  Returns a predicate that matches prescription samples.
- [static func workout(NSPredicate?) -> HKSamplePredicate<HKWorkout>](hksamplepredicate/workout(_:).md)
  Returns a sample predicate that matches workout samples.
- [static func workoutRoute(NSPredicate?) -> HKSamplePredicate<HKWorkoutRoute>](hksamplepredicate/workoutroute(_:).md)
  Returns a sample predicate that matches samples containing workout route data.
### Accessing Sample Predicate Data
- [let nsPredicate: NSPredicate?](hksamplepredicate/nspredicate.md)
  An optional predicate that further restricts the results that the query returns.
- [let sampleType: HKSampleType](hksamplepredicate/sampletype.md)
  The type of samples that the query returns.
### Type Methods
- [static func gad7Assessment(NSPredicate?) -> HKSamplePredicate<HKGAD7Assessment>](hksamplepredicate/gad7assessment(_:).md)
- [static func phq9Assessment(NSPredicate?) -> HKSamplePredicate<HKPHQ9Assessment>](hksamplepredicate/phq9assessment(_:).md)
- [static func stateOfMind(NSPredicate?) -> HKSamplePredicate<HKStateOfMind>](hksamplepredicate/stateofmind(_:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)
  Use Swift concurrency to manage one-shot and long-running queries.
- [protocol HKAsyncQuery](hkasyncquery.md)
  A protocol that defines an asynchronous method for running queries.
- [protocol HKAsyncSequenceQuery](hkasyncsequencequery.md)
  A protocol that defines a method for running queries that returns results using an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplepredicate)*