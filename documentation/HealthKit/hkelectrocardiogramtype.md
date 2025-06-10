# HKElectrocardiogramType

**Framework**: HealthKit  
**Kind**: class

A type that identifies samples containing electrocardiogram data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class HKElectrocardiogramType
```

#### Overview

The [`HKElectrocardiogramType`](hkelectrocardiogramtype.md) class is a concrete subclass of the [`HKObjectType`](hkobjecttype.md) class. To create an electrocardiogram type instance, use the object type’s [`electrocardiogramType()`](hkobjecttype/electrocardiogramtype().md) convenience method.

Use the electrocardiogram type to:

- Request permission to read electrocardiogram samples
- Query for electrocardiogram samples

Electrocardiogram samples are read-only. You can request permission to read the samples using this identifier, but you can’t request authorization to share them. This means you can’t save new electrocardiogram samples to the HealthKit store. To add test data in iOS Simulator, open the Health app and select Browse > Heart > Electrocardiograms (ECG) > Add Data.

## Relationships

### Inherits From
- [HKSampleType](hksampletype.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramtype)*