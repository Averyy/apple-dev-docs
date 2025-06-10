# HKClinicalCoding

**Framework**: HealthKit  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class HKClinicalCoding
```

#### Overview

Typically represents a single abstract concept within a coding system. This model is closely related to the FHIR model for codings. (https://build.fhir.org/datatypes.html#Coding)

## Topics

### Initializers
- [init(system: String, version: String?, code: String)](hkclinicalcoding/init(system:version:code:).md)
### Instance Properties
- [var code: String](hkclinicalcoding/code.md)
- [var system: String](hkclinicalcoding/system.md)
- [var version: String?](hkclinicalcoding/version.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [class HKHealthConceptIdentifier](hkhealthconceptidentifier.md)
- [class HKMedicationConcept](hkmedicationconcept.md)
- [class HKMedicationDoseEvent](hkmedicationdoseevent.md)
- [class HKMedicationDoseEventType](hkmedicationdoseeventtype.md)
- [class HKUserAnnotatedMedication](hkuserannotatedmedication.md)
- [class HKUserAnnotatedMedicationQuery](hkuserannotatedmedicationquery.md)
- [class HKUserAnnotatedMedicationType](hkuserannotatedmedicationtype.md)
- [struct HKHealthConceptDomain](hkhealthconceptdomain.md)
  Represents the domain of a HKHealthConceptIdentifier
- [struct HKMedicationGeneralForm](hkmedicationgeneralform.md)
  Represents a medications general form.
- [struct HKUserAnnotatedMedicationQueryDescriptor](hkuserannotatedmedicationquerydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicalcoding)*