# HKQuantityType

**Framework**: HealthKit  
**Kind**: class

A type that identifies samples that store numerical values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKQuantityType
```

## Mentions

- [Saving data to HealthKit](saving-data-to-healthkit.md)

#### Overview

The [`HKQuantityType`](hkquantitytype.md) class is a concrete subclass of the [`HKObjectType`](hkobjecttype.md) class. To create a quantity type instance, use the object type’s [`quantityType(forIdentifier:)`](hkobjecttype/quantitytype(foridentifier:).md) convenience method.

Use quantity types to:

- Request permission to read or write matching quantity samples.
- Create and share matching quantity samples.
- Query for matching quantity samples.

## Topics

### Creating Quantity Types
- [convenience init(HKQuantityTypeIdentifier)](hkquantitytype/init(_:).md)
  Creates a quantity type using the provided identifier.
### Accessing Quantity Type Data
- [var aggregationStyle: HKQuantityAggregationStyle](hkquantitytype/aggregationstyle.md)
  The aggregation style for the given quantity type.
- [enum HKQuantityAggregationStyle](hkquantityaggregationstyle.md)
  Constant values that describe how quantities can be aggregated over time.
- [func `is`(compatibleWith: HKUnit) -> Bool](hkquantitytype/is(compatiblewith:).md)
  Returns a Boolean value that indicates whether the quantity type is compatible with the given unit.

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

## See Also

- [struct HKQuantityTypeIdentifier](hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKCharacteristicType](hkcharacteristictype.md)
  A type that represents data that doesn’t typically change over time.
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
- [class HKSampleType](hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytype)*