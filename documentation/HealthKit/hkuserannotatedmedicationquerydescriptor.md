# HKUserAnnotatedMedicationQueryDescriptor

**Framework**: HealthKit  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct HKUserAnnotatedMedicationQueryDescriptor
```

## Topics

### Initializers
- [init(predicate: NSPredicate?, limit: Int?)](hkuserannotatedmedicationquerydescriptor/init(predicate:limit:).md)
### Instance Properties
- [var limit: Int?](hkuserannotatedmedicationquerydescriptor/limit.md)
  The maximum number of resulting HKUserAnnotatedMedication objects.
- [var predicate: NSPredicate?](hkuserannotatedmedicationquerydescriptor/predicate.md)
  The predicate that matches the desired HKUserAnnotatedMedication objects.
### Default Implementations
- [HKAsyncQuery Implementations](hkuserannotatedmedicationquerydescriptor/hkasyncquery-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HKAsyncQuery](hkasyncquery.md)

## See Also

- [class HKClinicalCoding](hkclinicalcoding.md)
  A clinical coding that represents a medical concept using a standardized coding system.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkuserannotatedmedicationquerydescriptor)*