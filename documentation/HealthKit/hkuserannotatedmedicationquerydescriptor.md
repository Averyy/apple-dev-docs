# HKUserAnnotatedMedicationQueryDescriptor

**Framework**: HealthKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkuserannotatedmedicationquerydescriptor)*