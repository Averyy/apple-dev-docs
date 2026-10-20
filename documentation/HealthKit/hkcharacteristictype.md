# HKCharacteristicType

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKCharacteristicType : HKObjectType
```

#### Overview

The [`HKCharacteristicType`](./hkcharacteristictype.md) class is a concrete subclass of the [`HKObjectType`](./hkobjecttype.md) class. To create a characteristic type instance, use the object type’s [`characteristicType(forIdentifier:)`](./hkobjecttype/characteristictype%28foridentifier%29.md) convenience method.

Unlike the other object types, characteristic types cannot be used to create and save new HealthKit objects. Instead, users must enter and edit their characteristic data using the Health app. Similarly, you cannot create queries for characteristic types. Instead, use the HealthKit store to access the data (see Reading characteristic data).

HealthKit provides five characteristic types: biological sex, blood type, birthdate, Fitzpatrick skin type, and wheelchair use. These types are used only when asking for permission to read data from the HealthKit store.

## Topics

### Creating Characteristic Types
- [convenience init(HKCharacteristicTypeIdentifier)](./hkcharacteristictype/init%28_%29.md)
  Creates a characteristic type using the provided identifier.

## Relationships

### Inherits From
- [HKObjectType](./hkobjecttype.md)
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

### Related Documentation
- [struct HKCharacteristicTypeIdentifier](./hkcharacteristictypeidentifier.md)
  The identifiers that create characteristic type objects.
### Object type subclasses
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
- [class HKWorkoutType](./hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [class HKObjectType](./hkobjecttype.md)
  An abstract superclass with subclasses that identify a specific type of data for the HealthKit store.
- [class HKSampleType](./hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcharacteristictype)*