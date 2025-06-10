# HKCategoryType

**Framework**: HealthKit  
**Kind**: class

A type that identifies samples that contain a value from a small set of possible values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKCategoryType
```

#### Overview

The [`HKCategoryType`](hkcategorytype.md) class is a concrete subclass of the HKObjectType class. To create a category type instance, use the object type’s [`categoryType(forIdentifier:)`](hkobjecttype/categorytype(foridentifier:).md) convenience method.

Use category types to:

- Request permission to read or write matching quantity samples.
- Create and share matching quantity samples.
- Query for matching quantity samples.

## Topics

### Creating Category Types
- [convenience init(HKCategoryTypeIdentifier)](hkcategorytype/init(_:).md)
  Creates a category type using the provided identifier.

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

- [struct HKCategoryTypeIdentifier](hkcategorytypeidentifier.md)
  Identifiers for creating category types.
- [class HKCategorySample](hkcategorysample.md)
  A sample with values from a short list of possible values.
- [class HKCharacteristicType](hkcharacteristictype.md)
  A type that represents data that doesn’t typically change over time.
- [class HKQuantityType](hkquantitytype.md)
  A type that identifies samples that store numerical values.
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
- [class HKSampleType](hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytype)*