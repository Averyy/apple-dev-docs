# HKUserAnnotatedMedication

**Framework**: HealthKit  
**Kind**: class

A reference to the tracked medication and the details a person can customize.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class HKUserAnnotatedMedication
```

#### Overview

The details are relevant to the medication tracking experience.

## Topics

### Instance Properties
- [var hasSchedule: Bool](hkuserannotatedmedication/hasschedule.md)
  A Boolean value that indicates whether a medication has a schedule set up.
- [var isArchived: Bool](hkuserannotatedmedication/isarchived.md)
  A Boolean value that indicates whether a medication is archived.
- [var medication: HKMedicationConcept](hkuserannotatedmedication/medication.md)
  A reference to the specific medication a person is tracking.
- [var nickname: String?](hkuserannotatedmedication/nickname.md)
  The nickname that a person added to a medication during the entry experience.

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

- [class HKClinicalCoding](hkclinicalcoding.md)
  A clinical coding that represents a medical concept using a standardized coding system.
- [class HKHealthConceptIdentifier](hkhealthconceptidentifier.md)
  A unique identifier for a specific health concept within a domain.
- [class HKMedicationConcept](hkmedicationconcept.md)
  An object that describes a specific medication concept.
- [class HKMedicationDoseEvent](hkmedicationdoseevent.md)
- [class HKMedicationDoseEventType](hkmedicationdoseeventtype.md)
- [class HKUserAnnotatedMedicationQuery](hkuserannotatedmedicationquery.md)
- [class HKUserAnnotatedMedicationType](hkuserannotatedmedicationtype.md)
- [struct HKHealthConceptDomain](hkhealthconceptdomain.md)
  A domain that represents a health concept.
- [struct HKMedicationGeneralForm](hkmedicationgeneralform.md)
  The manufactured form of a medication.
- [struct HKUserAnnotatedMedicationQueryDescriptor](hkuserannotatedmedicationquerydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkuserannotatedmedication)*