# HKClinicalType

**Framework**: HealthKit  
**Kind**: class

A type that identifies samples that contain clinical record data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class HKClinicalType
```

## Topics

### Creating Clinical Types
- [convenience init(HKClinicalTypeIdentifier)](hkclinicaltype/init(_:).md)
  Creates a clinical type using the provided identifier.

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

- [class HKClinicalRecord](hkclinicalrecord.md)
  A sample that stores a clinical record.
- [static let allergyRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/allergyrecord.md)
  A type identifier for records of allergic or intolerant reactions.
- [static let conditionRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/conditionrecord.md)
  A type identifier for records of a condition, problem, diagnosis, or other event.
- [static let immunizationRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/immunizationrecord.md)
  A type identifier for records of the current or historical administration of vaccines.
- [static let labResultRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/labresultrecord.md)
  A type identifier for records of lab results.
- [static let medicationRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/medicationrecord.md)
  A type identifier for records of medication.
- [static let procedureRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/procedurerecord.md)
  A type identifier for records of procedures.
- [static let vitalSignRecord: HKClinicalTypeIdentifier](hkclinicaltypeidentifier/vitalsignrecord.md)
  A type identifier for records of vital signs.
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
- [class HKElectrocardiogramType](hkelectrocardiogramtype.md)
  A type that identifies samples containing electrocardiogram data.
- [class HKSeriesType](hkseriestype.md)
  A type that indicates the data stored in a series sample.
- [class HKWorkoutType](hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [class HKObjectType](hkobjecttype.md)
  An abstract superclass with subclasses that identify a specific type of data for the HealthKit store.
- [class HKSampleType](hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicaltype)*