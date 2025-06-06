# HKSample

**Framework**: HealthKit  
**Kind**: class

A HealthKit sample represents a piece of data associated with a start and end time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKSample
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)
- [Saving data to HealthKit](saving-data-to-healthkit.md)
- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)

#### Overview

The `HKSample` class is an abstract class. You should never instantiate a `HKSample` object directly. Instead, you always work with one of its concrete subclasses: [`HKCategorySample`](hkcategorysample.md), [`HKQuantitySample`](hkquantitysample.md), [`HKCorrelation`](hkcorrelation.md), or [`HKWorkout`](hkworkout.md) classes.

HealthKit samples are all immutable: You set the sample’s properties when you create it, and they cannot change.

If the sample represents data over a duration, the start time must be earlier than the end time. If the sample represents data at a particular instant, the start and end times can be the same.

## Topics

### Accessing the Sample’s Data
- [var startDate: Date](hksample/startdate.md)
  The sample’s start date.
- [var endDate: Date](hksample/enddate.md)
  The sample’s end date.
- [var hasUndeterminedDuration: Bool](hksample/hasundeterminedduration.md)
  Indicates whether the sample has an unknown duration.
- [var sampleType: HKSampleType](hksample/sampletype.md)
  The sample type.
### Specifying Sort Identifiers
- [let HKSampleSortIdentifierStartDate: String](hksamplesortidentifierstartdate.md)
  A constant for sorting samples based on their start date.
- [let HKSampleSortIdentifierEndDate: String](hksamplesortidentifierenddate.md)
  A constant for sorting samples based on their end date.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathStartDate: String](hkpredicatekeypathstartdate.md)
  The key path for accessing the sample’s start date.
- [let HKPredicateKeyPathEndDate: String](hkpredicatekeypathenddate.md)
  The key path for accessing the sample’s end date.

## Relationships

### Inherits From
- [HKObject](hkobject.md)
### Inherited By
- [HKAudiogramSample](hkaudiogramsample.md)
- [HKCategorySample](hkcategorysample.md)
- [HKClinicalRecord](hkclinicalrecord.md)
- [HKCorrelation](hkcorrelation.md)
- [HKDocumentSample](hkdocumentsample.md)
- [HKElectrocardiogram](hkelectrocardiogram.md)
- [HKQuantitySample](hkquantitysample.md)
- [HKScoredAssessment](hkscoredassessment.md)
- [HKSeriesSample](hkseriessample.md)
- [HKStateOfMind](hkstateofmind.md)
- [HKVerifiableClinicalRecord](hkverifiableclinicalrecord.md)
- [HKVisionPrescription](hkvisionprescription.md)
- [HKWorkout](hkworkout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKObject](hkobject.md)
  A piece of data that can be stored inside the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksample)*