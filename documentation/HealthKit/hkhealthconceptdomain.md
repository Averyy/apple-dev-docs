# HKHealthConceptDomain

**Framework**: HealthKit  
**Kind**: struct  
**Role**: Structure

A domain that represents a health concept.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct HKHealthConceptDomain
```

```c
typedef NSString * HKHealthConceptDomain;
```

#### Overview

A health concept describes what type of medical information a concept belongs to. For example, the medication domain groups all medication concepts together.

## Topics

### Initializers
- [init(rawValue: String)](./hkhealthconceptdomain/init%28rawvalue%29.md)
### Type Properties
- [static let medication: HKHealthConceptDomain](./hkhealthconceptdomain/medication.md)
  The domain that represents medication concepts.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Medication queries
- [class HKClinicalCoding](./hkclinicalcoding.md)
  A clinical coding that represents a medical concept using a standardized coding system.
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
- [struct HKMedicationGeneralForm](./hkmedicationgeneralform.md)
  The manufactured form of a medication.
- [struct HKUserAnnotatedMedicationQueryDescriptor](./hkuserannotatedmedicationquerydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthconceptdomain)*