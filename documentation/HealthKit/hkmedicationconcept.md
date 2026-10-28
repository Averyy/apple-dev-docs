# HKMedicationConcept

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

An object that describes a specific medication concept.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class HKMedicationConcept
```

```objc
@interface HKMedicationConcept : NSObject
```

## Overview

A medication concept represents the idea of a medication, like ibuprofen or insulin. It can have clinical significance, or can be created by the person using your app.

## Topics

### Initializers
- [init?(coder: NSCoder)](./hkmedicationconcept/init%28coder%29.md)
### Instance Properties
- [var displayText: String](./hkmedicationconcept/displaytext.md)
  The display name for this medication.
- [var generalForm: HKMedicationGeneralForm](./hkmedicationconcept/generalform.md)
  The general form the medication is manufactured in.
- [var identifier: HKHealthConceptIdentifier](./hkmedicationconcept/identifier.md)
  The unique identifier for the specific medication concept.
- [var relatedCodings: Set<HKClinicalCoding>](./hkmedicationconcept/relatedcodings.md)
  The set of related clinical codings for the medication.

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
- [class HKClinicalCoding](./hkclinicalcoding.md)
  A clinical coding that represents a medical concept using a standardized coding system.
- [class HKHealthConceptIdentifier](./hkhealthconceptidentifier.md)
  A unique identifier for a specific health concept within a domain.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationconcept)*