# HKCategoryType

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKCategoryType : HKSampleType
```

## Mentions

- [Recording and querying menopausal state](./recording-and-querying-menopausal-state.md)

## Overview

The [`HKCategoryType`](./hkcategorytype.md) class is a concrete subclass of the HKObjectType class. To create a category type instance, use the [`init(_:)`](./hkcategorytype/init%28_%29.md) convenience method.  For example, the following code creates a category sample type for handwashing events.

```swift
let handwashingCategoryType = HKCategoryType(.handwashingEvent)
```

Use category types to:

- Request permission to read or write matching category samples.
- Create and share matching category samples.
- Query for matching category samples.

For a complete list of category types, refer to [`HKCategoryTypeIdentifier`](./hkcategorytypeidentifier.md).

## Topics

### Creating Category Types
- [convenience init(HKCategoryTypeIdentifier)](./hkcategorytype/init%28_%29.md)
  Creates a category type using the provided identifier.

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
- [struct HKCategoryTypeIdentifier](./hkcategorytypeidentifier.md)
  Identifiers for creating category types.
- [class HKCategorySample](./hkcategorysample.md)
  A sample with values from a short list of possible values.
### Object type subclasses
- [class HKCharacteristicType](./hkcharacteristictype.md)
  A type that represents data that doesn’t typically change over time.
- [class HKQuantityType](./hkquantitytype.md)
  A type that identifies samples that store numerical values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytype)*