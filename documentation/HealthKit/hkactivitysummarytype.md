# HKActivitySummaryType

**Framework**: HealthKit  
**Kind**: class

A type that identifies activity summary objects.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
class HKActivitySummaryType
```

#### Overview

Use the activity summary type to request permission to read [`HKActivitySummary`](hkactivitysummary.md) objects from the HealthKit store. To create an activity summary type, use the [`HKObjectType`](hkobjecttype.md) class’s [`activitySummaryType()`](hkobjecttype/activitysummarytype().md) convenience method.

> **Note**:  Although you can request permission to read [`HKActivitySummary`](hkactivitysummary.md) objects, you can’t request permission to share them. For more information, see [`requestAuthorization(toShare:read:completion:)`](hkhealthstore/requestauthorization(toshare:read:completion:).md).

 Although you can request permission to read [`HKActivitySummary`](hkactivitysummary.md) objects, you can’t request permission to share them. For more information, see [`requestAuthorization(toShare:read:completion:)`](hkhealthstore/requestauthorization(toshare:read:completion:).md).

The [`HKActivitySummaryType`](hkactivitysummarytype.md) class is a concrete subclass of the [`HKObjectType`](hkobjecttype.md) class. Like many HealthKit classes, activity summary types aren’t extensible and you shouldn’t subclass them.

##### Access and Modify Activity Summaries

Any workouts that you save to the HealthKit store may affect that day’s summary. For more information, see [`HKWorkout`](hkworkout.md).

To query for activity summary objects, use an [`HKActivitySummaryQuery`](hkactivitysummaryquery.md). You can also create your own [`HKActivitySummary`](hkactivitysummary.md) objects (for example, to display in an [`HKActivityRingView`](https://developer.apple.com/documentation/healthkitui/hkactivityringview)), but you can’t save them to the HealthKit store.

## Relationships

### Inherits From
- [HKObjectType](hkobjecttype.md)
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

## See Also

- [class HKActivitySummary](hkactivitysummary.md)
  An object that contains the move, exercise, and stand data for a given day.
- [class HKActivitySummaryQuery](hkactivitysummaryquery.md)
  A query for reading activity summary objects from the HealthKit store.
- [class HKActivityRingView](../healthkitui/hkactivityringview.md)
  A view that uses the Move, Exercise, and Stand activity rings to display data from a HealthKit activity summary object.
- [class HKCharacteristicType](hkcharacteristictype.md)
  A type that represents data that doesn’t typically change over time.
- [class HKQuantityType](hkquantitytype.md)
  A type that identifies samples that store numerical values.
- [class HKCategoryType](hkcategorytype.md)
  A type that identifies samples that contain a value from a small set of possible values.
- [class HKCorrelationType](hkcorrelationtype.md)
  A type that identifies samples that group multiple subsamples.
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
- [class HKSampleType](hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummarytype)*