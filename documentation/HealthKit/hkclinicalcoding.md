# HKClinicalCoding

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKClinicalCoding : NSObject
```

## Overview

A clinical coding pairs a [`system`](./hkclinicalcoding/system.md), an optional [`version`](./hkclinicalcoding/version.md), and a [`code`](./hkclinicalcoding/code.md) which identify a medical concept.

This model is closely related to the [FHIR Coding model](https://build.fhir.org/datatypes.html#Coding).

## Topics

### Initializers
- [init?(coder: NSCoder)](./hkclinicalcoding/init%28coder%29.md)
- [init(system: String, version: String?, code: String)](./hkclinicalcoding/init%28system,version,code%29.md)
  Creates a clinical coding with the specified system, version, and code.
### Instance Properties
- [var code: String](./hkclinicalcoding/code.md)
  The clinical code that represents a medical concept inside the coding system.
- [var system: String](./hkclinicalcoding/system.md)
  The string that identifies the coding system that defines this clinical code.
- [var version: String?](./hkclinicalcoding/version.md)
  The version of the coding system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Medication queries
- [class HKHealthConceptIdentifier](./hkhealthconceptidentifier.md)
  A unique identifier for a specific health concept within a domain.
- [class HKMedicationConcept](./hkmedicationconcept.md)
  An object that describes a specific medication concept.
- [class HKMedicationDoseEvent](./hkmedicationdoseevent.md)
- [class HKMedicationDoseEventType](./hkmedicationdoseeventtype.md)
- [class HKUserAnnotatedMedication](./hkuserannotatedmedication.md)
  A reference to the tracked medication and the details a person can customize.
- [class HKUserAnnotatedMedicationQuery](./hkuserannotatedmedicationquery.md)
- [class HKUserAnnotatedMedicationType](./hkuserannotatedmedicationtype.md)
- [struct HKHealthConceptDomain](./hkhealthconceptdomain.md)
  A domain that represents a health concept.
- [struct HKMedicationGeneralForm](./hkmedicationgeneralform.md)
  The manufactured form of a medication.
- [struct HKUserAnnotatedMedicationQueryDescriptor](./hkuserannotatedmedicationquerydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkclinicalcoding)*