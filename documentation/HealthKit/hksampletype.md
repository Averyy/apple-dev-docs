# HKSampleType

**Framework**: HealthKit  
**Kind**: class

An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKSampleType
```

## Mentions

- [Saving data to HealthKit](saving-data-to-healthkit.md)

#### Overview

The [`HKSampleType`](hksampletype.md) class is an abstract subclass of the [`HKObjectType`](hkobjecttype.md) class, used to represent data samples. Never instantiate an [`HKSampleType`](hksampletype.md) object directly. Instead, work with one of its concrete subclasses: [`HKCategoryType`](hkcategorytype.md), [`HKCorrelationType`](hkcorrelationtype.md), [`HKQuantityType`](hkquantitytype.md), or [`HKWorkoutType`](hkworkouttype.md) classes.

## Topics

### Checking the Duration Restriction
- [var isMinimumDurationRestricted: Bool](hksampletype/isminimumdurationrestricted.md)
  A Boolean value that indicates whether samples of this type have a minimum time interval between the start and end dates.
- [var minimumAllowedDuration: TimeInterval](hksampletype/minimumallowedduration.md)
  The minimum duration if the sample type has a restricted duration.
- [var isMaximumDurationRestricted: Bool](hksampletype/ismaximumdurationrestricted.md)
  A Boolean value that indicates whether samples of this type have a maximum time interval between the start and end dates.
- [var maximumAllowedDuration: TimeInterval](hksampletype/maximumallowedduration.md)
  The maximum duration if the sample type has a restricted duration.
### Checking on Recalibrating Estimates
- [var allowsRecalibrationForEstimates: Bool](hksampletype/allowsrecalibrationforestimates.md)
  A Boolean value that indicates whether HealthKit supports recalibrating the prediction algorithm used to produce estimates for this sample type.

## Relationships

### Inherits From
- [HKObjectType](hkobjecttype.md)
### Inherited By
- [HKAudiogramSampleType](hkaudiogramsampletype.md)
- [HKCategoryType](hkcategorytype.md)
- [HKClinicalType](hkclinicaltype.md)
- [HKCorrelationType](hkcorrelationtype.md)
- [HKDocumentType](hkdocumenttype.md)
- [HKElectrocardiogramType](hkelectrocardiogramtype.md)
- [HKMedicationDoseEventType](hkmedicationdoseeventtype.md)
- [HKPrescriptionType](hkprescriptiontype.md)
- [HKQuantityType](hkquantitytype.md)
- [HKScoredAssessmentType](hkscoredassessmenttype.md)
- [HKSeriesType](hkseriestype.md)
- [HKStateOfMindType](hkstateofmindtype.md)
- [HKWorkoutType](hkworkouttype.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HKCharacteristicType](hkcharacteristictype.md)
  A type that represents data that doesn’t typically change over time.
- [class HKQuantityType](hkquantitytype.md)
  A type that identifies samples that store numerical values.
- [class HKCategoryType](hkcategorytype.md)
  A type that identifies samples that contain a value from a small set of possible values.
- [class HKCorrelationType](hkcorrelationtype.md)
  A type that identifies samples that group multiple subsamples.
- [class HKActivitySummaryType](hkactivitysummarytype.md)
  A type that identifies activity summary objects.
- [class HKAudiogramSampleType](hkaudiogramsampletype.md)
  A type that identifies samples that contain audiogram data.
- [class HKElectrocardiogramType](hkelectrocardiogramtype.md)
  A type that identifies samples containing electrocardiogram data.
- [class HKSeriesType](hkseriestype.md)
  A type that indicates the data stored in a series sample.
- [class HKClinicalType](hkclinicaltype.md)
  A type that identifies samples that contain clinical record data.
- [class HKWorkoutType](hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [class HKObjectType](hkobjecttype.md)
  An abstract superclass with subclasses that identify a specific type of data for the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksampletype)*