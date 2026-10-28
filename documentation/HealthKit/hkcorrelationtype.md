# HKCorrelationType

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A type that identifies samples that group multiple subsamples.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKCorrelationType
```

```objc
@interface HKCorrelationType : HKSampleType
```

## Overview

The [`HKCorrelationType`](./hkcorrelationtype.md) class is a concrete subclass of the [`HKObjectType`](./hkobjecttype.md) class. To create a correlation type instance, use the object type’s [`correlationType(forIdentifier:)`](./hkobjecttype/correlationtype%28foridentifier%29.md) conveniance method.

Use correlation types to:

- Request permission to read or write matching quantity samples.
- Create and share matching quantity samples.
- Query for matching quantity samples.

HealthKit provides two correlation types: blood pressure and food.

### Using Correlation Types

As with many HealthKit classes, don’t subclass correlation types.

This class reuses the same instance whenever possible. Letting multiple queries share the same workout type helps reduce the overall memory usage.

## Topics

### Creating Correlation Types
- [convenience init(HKCorrelationTypeIdentifier)](./hkcorrelationtype/init%28_%29.md)
  Creates a correlation type using the provided identifier.

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

### Related Documentation
- [struct HKCorrelationTypeIdentifier](./hkcorrelationtypeidentifier.md)
  The identifiers that create correlation type objects.
- [class HKCorrelation](./hkcorrelation.md)
  A sample that groups multiple related samples into a single entry.
### Object type subclasses
- [class HKCharacteristicType](./hkcharacteristictype.md)
  A type that represents data that doesn’t typically change over time.
- [class HKQuantityType](./hkquantitytype.md)
  A type that identifies samples that store numerical values.
- [class HKCategoryType](./hkcategorytype.md)
  A type that identifies samples that contain a value from a small set of possible values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelationtype)*