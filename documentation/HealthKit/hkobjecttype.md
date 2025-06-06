# HKObjectType

**Framework**: HealthKit  
**Kind**: class

An abstract superclass with subclasses that identify a specific type of data for the HealthKit store.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKObjectType
```

## Mentions

- [Saving data to HealthKit](saving-data-to-healthkit.md)
- [About the HealthKit framework](about-the-healthkit-framework.md)

#### Overview

The `HKObjectType` class is an abstract class. Don’t instantiate an `HKObjectType` object directly. Instead, instantiate one of the following concrete subclasses:

- [`HKActivitySummaryType`](hkactivitysummarytype.md)
- [`HKCategoryType`](hkcategorytype.md)
- [`HKCorrelationType`](hkcorrelationtype.md)
- [`HKCharacteristicType`](hkcharacteristictype.md)
- [`HKDocumentType`](hkdocumenttype.md)
- [`HKQuantityType`](hkquantitytype.md)
- [`HKSeriesType`](hkseriestype.md)
- [`HKWorkoutType`](hkworkouttype.md)

The `HKObjectType` class provides a convenience method to create each of these subclasses.

##### Work with Object Types

Like many HealthKit classes, HealthKit object types aren’t extensible. Don’t subclass these classes.

Additionally, wherever possible, this class uses a single instance to represent all copies of the same type. For example, if you make two calls to the [`quantityType(forIdentifier:)`](hkobjecttype/quantitytype(foridentifier:).md) method with the same identifier, the system returns the same instance. Reusing object types helps reduce HealthKit’s overall memory usage.

## Topics

### Creating quantity types
- [class func quantityType(forIdentifier: HKQuantityTypeIdentifier) -> HKQuantityType?](hkobjecttype/quantitytype(foridentifier:).md)
  Returns the shared quantity type for the provided identifier.
- [struct HKQuantityTypeIdentifier](hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.
### Creating category types
- [class func categoryType(forIdentifier: HKCategoryTypeIdentifier) -> HKCategoryType?](hkobjecttype/categorytype(foridentifier:).md)
  Returns the shared category type for the provided identifier.
- [struct HKCategoryTypeIdentifier](hkcategorytypeidentifier.md)
  Identifiers for creating category types.
### Creating characteristic types
- [class func characteristicType(forIdentifier: HKCharacteristicTypeIdentifier) -> HKCharacteristicType?](hkobjecttype/characteristictype(foridentifier:).md)
  Returns the shared characteristic type for the provided identifier.
- [struct HKCharacteristicTypeIdentifier](hkcharacteristictypeidentifier.md)
  The identifiers that create characteristic type objects.
### Creating correlation types
- [class func correlationType(forIdentifier: HKCorrelationTypeIdentifier) -> HKCorrelationType?](hkobjecttype/correlationtype(foridentifier:).md)
  Returns the shared correlation type for the provided identifier.
- [struct HKCorrelationTypeIdentifier](hkcorrelationtypeidentifier.md)
  The identifiers that create correlation type objects.
### Creating workout types
- [class func workoutType() -> HKWorkoutType](hkobjecttype/workouttype.md)
  Returns the shared [`HKWorkoutType`](hkworkouttype.md) object.
### Creating activity summary types
- [class func activitySummaryType() -> HKActivitySummaryType](hkobjecttype/activitysummarytype.md)
  Returns the shared activity summary type.
### Creating electrocardiogram types
- [class func electrocardiogramType() -> HKElectrocardiogramType](hkobjecttype/electrocardiogramtype.md)
  Returns the shared electrocardiogram type.
### Creating audiogram sample types
- [class func audiogramSampleType() -> HKAudiogramSampleType](hkobjecttype/audiogramsampletype.md)
  Returns an audiogram sample type.
### Creating vision prescription types
- [class func visionPrescriptionType() -> HKPrescriptionType](hkobjecttype/visionprescriptiontype.md)
  Returns a shared vision prescription type object.
### Creating clinical record types
- [class func clinicalType(forIdentifier: HKClinicalTypeIdentifier) -> HKClinicalType?](hkobjecttype/clinicaltype(foridentifier:).md)
  Returns the shared clinical type for the provided identifier.
### Creating series types
- [class func seriesType(forIdentifier: String) -> HKSeriesType?](hkobjecttype/seriestype(foridentifier:).md)
  Returns the shared series type for the provided identifier.
### Creating document types
- [class func documentType(forIdentifier: HKDocumentTypeIdentifier) -> HKDocumentType?](hkobjecttype/documenttype(foridentifier:).md)
  Returns the shared document type for the provided identifier.
- [struct HKDocumentTypeIdentifier](hkdocumenttypeidentifier.md)
  The identifiers for documents.
### Getting property data
- [var identifier: String](hkobjecttype/identifier.md)
  A unique string identifying the HealthKit object type.
- [func requiresPerObjectAuthorization() -> Bool](hkobjecttype/requiresperobjectauthorization.md)
  Returns a Boolean that indicates whether the data type requires per-object authorization.
### Type Methods
- [class func stateOfMindType() -> HKStateOfMindType](hkobjecttype/stateofmindtype.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [HKActivitySummaryType](hkactivitysummarytype.md)
- [HKCharacteristicType](hkcharacteristictype.md)
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
- [class HKClinicalType](hkclinicaltype.md)
  A type that identifies samples that contain clinical record data.
- [class HKWorkoutType](hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [class HKSampleType](hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype)*