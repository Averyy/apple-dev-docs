# HKClinicalCoding

**Framework**: HealthKit  
**Kind**: class

A clinical coding that represents a medical concept using a standardized coding system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class HKClinicalCoding
```

#### Overview

A clinical coding pairs a [`system`](hkclinicalcoding/system.md), an optional [`version`](hkclinicalcoding/version.md), and a [`code`](hkclinicalcoding/code.md) which identify a medical concept.

This model is closely related to the [`FHIR Coding model`](https://developer.apple.comhttps://build.fhir.org/datatypes.html#Coding).

## Topics

### Initializers
- [init(system: String, version: String?, code: String)](hkclinicalcoding/init(system:version:code:).md)
  Creates a clinical coding with the specified system, version, and code.
### Instance Properties
- [var code: String](hkclinicalcoding/code.md)
  The clinical code that represents a medical concept inside the coding system.
- [var system: String](hkclinicalcoding/system.md)
  The string that identifies the coding system that defines this clinical code.
- [var version: String?](hkclinicalcoding/version.md)
  The version of the coding system.

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
  A unique identifier for a specific health concept within a domain.
- [class HKMedicationConcept](hkmedicationconcept.md)
  An object that describes a specific medication concept.
- [class HKMedicationDoseEvent](hkmedicationdoseevent.md)
- [class HKMedicationDoseEventType](hkmedicationdoseeventtype.md)
- [class HKUserAnnotatedMedication](hkuserannotatedmedication.md)
  A reference to the tracked medication and the details a person can customize.
- [class HKUserAnnotatedMedicationQuery](hkuserannotatedmedicationquery.md)
- [class HKUserAnnotatedMedicationType](hkuserannotatedmedicationtype.md)
- [struct HKHealthConceptDomain](hkhealthconceptdomain.md)
  A domain that represents a health concept.
- [struct HKMedicationGeneralForm](hkmedicationgeneralform.md)
  The manufactured form of a medication.
- [struct HKUserAnnotatedMedicationQueryDescriptor](hkuserannotatedmedicationquerydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicalcoding)*