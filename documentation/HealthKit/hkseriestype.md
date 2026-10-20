# HKSeriesType

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A type that indicates the data stored in a series sample.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HKSeriesType
```

```objc
@interface HKSeriesType : HKSampleType
```

## Topics

### Accessing Series Types
- [class func workoutRoute() -> Self](./hkseriestype/workoutroute%28%29.md)
  Returns a series type object for workout routes.
- [class func heartbeat() -> Self](./hkseriestype/heartbeat%28%29.md)
  Returns a series type object for heartbeat data.

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
- [class HKWorkoutRoute](./hkworkoutroute.md)
  A sample that contains a workout’s route data.
- [class HKWorkoutRouteBuilder](./hkworkoutroutebuilder.md)
  A builder object that incrementally constructs a workout route.
- [class HKWorkoutRouteQuery](./hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
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
- [class HKClinicalType](./hkclinicaltype.md)
  A type that identifies samples that contain clinical record data.
- [class HKWorkoutType](./hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [class HKObjectType](./hkobjecttype.md)
  An abstract superclass with subclasses that identify a specific type of data for the HealthKit store.
- [class HKSampleType](./hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkseriestype)*