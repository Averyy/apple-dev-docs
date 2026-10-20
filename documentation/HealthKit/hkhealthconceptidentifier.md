# HKHealthConceptIdentifier

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A unique identifier for a specific health concept within a domain.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class HKHealthConceptIdentifier
```

```objc
@interface HKHealthConceptIdentifier : NSObject
```

#### Overview

Each identifier points to one concept inside a domain. For example, within the medication domain, one identifier might represent ibuprofen while another represents insulin.

## Topics

### Initializers
- [init?(coder: NSCoder)](./hkhealthconceptidentifier/init%28coder%29.md)
### Instance Properties
- [var domain: HKHealthConceptDomain](./hkhealthconceptidentifier/domain.md)
  The domain this identifier belongs to.

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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthconceptidentifier)*