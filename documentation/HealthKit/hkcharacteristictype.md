# HKCharacteristicType

**Framework**: HealthKit  
**Kind**: class

A type that represents data that doesn’t typically change over time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKCharacteristicType
```

#### Overview

The [`HKCharacteristicType`](hkcharacteristictype.md) class is a concrete subclass of the [`HKObjectType`](hkobjecttype.md) class. To create a characteristic type instance, use the object type’s [`characteristicType(forIdentifier:)`](hkobjecttype/characteristictype(foridentifier:).md) convenience method.

Unlike the other object types, characteristic types cannot be used to create and save new HealthKit objects. Instead, users must enter and edit their characteristic data using the Health app. Similarly, you cannot create queries for characteristic types. Instead, use the HealthKit store to access the data (see Reading characteristic data).

HealthKit provides five characteristic types: biological sex, blood type, birthdate, Fitzpatrick skin type, and wheelchair use. These types are used only when asking for permission to read data from the HealthKit store.

## Topics

### Creating Characteristic Types
- [convenience init(HKCharacteristicTypeIdentifier)](hkcharacteristictype/init(_:).md)
  Creates a characteristic type using the provided identifier.

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

- [struct HKCharacteristicTypeIdentifier](hkcharacteristictypeidentifier.md)
  The identifiers that create characteristic type objects.
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
- [class HKSampleType](hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcharacteristictype)*