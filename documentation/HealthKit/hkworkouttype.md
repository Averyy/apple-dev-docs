# HKWorkoutType

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A type that identifies samples that store information about a workout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKWorkoutType
```

```objc
@interface HKWorkoutType : HKSampleType
```

## Overview

The [`HKWorkoutType`](./hkworkouttype.md) class is a concrete subclass of the [`HKObjectType`](./hkobjecttype.md) class. To create a workout type instances, use the [`workoutType()`](./hkobjecttype/workouttype%28%29.md)  convenience method.

All workouts use the same workout type instance.

## Relationships

### Inherits From
- [HKSampleType](./hksampletype.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Object type subclasses
- [class HKCharacteristicType](./hkcharacteristictype.md)
  A type that represents data that doesn’t typically change over time.
- [class HKQuantityType](./hkquantitytype.md)
  A type that identifies samples that store numerical values.
- [class HKCategoryType](./hkcategorytype.md)
  A type that identifies samples that contain a value from a small set of possible values.
- [class HKCorrelationType](./hkcorrelationtype.md)
  A type that identifies samples that group multiple subsamples.
- [class HKActivitySummaryType](./hkactivitysummarytype.md)
  A type that identifies activity summary objects.
- [class HKAudiogramSampleType](./hkaudiogramsampletype.md)
  A type that identifies samples that contain audiogram data.
- [class HKElectrocardiogramType](./hkelectrocardiogramtype.md)
  A type that identifies samples containing electrocardiogram data.
- [class HKSeriesType](./hkseriestype.md)
  A type that indicates the data stored in a series sample.
- [class HKClinicalType](./hkclinicaltype.md)
  A type that identifies samples that contain clinical record data.
- [class HKObjectType](./hkobjecttype.md)
  An abstract superclass with subclasses that identify a specific type of data for the HealthKit store.
- [class HKSampleType](./hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkouttype)*