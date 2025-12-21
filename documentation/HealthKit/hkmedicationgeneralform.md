# HKMedicationGeneralForm

**Framework**: HealthKit  
**Kind**: struct

The manufactured form of a medication.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct HKMedicationGeneralForm
```

## Topics

### Initializers
- [init(rawValue: String)](hkmedicationgeneralform/init(rawvalue:).md)
### Type Properties
- [static let capsule: HKMedicationGeneralForm](hkmedicationgeneralform/capsule.md)
  The medication comes in capsule form, such as a hard-shell capsule or softgel.
- [static let cream: HKMedicationGeneralForm](hkmedicationgeneralform/cream.md)
  The medication is applied as a cream.
- [static let device: HKMedicationGeneralForm](hkmedicationgeneralform/device.md)
  The medication is administered through a device, such as an infusion pump for controlled fluid delivery.
- [static let drops: HKMedicationGeneralForm](hkmedicationgeneralform/drops.md)
  The medication is taken as drops, for example eye drops or ear drops.
- [static let foam: HKMedicationGeneralForm](hkmedicationgeneralform/foam.md)
  The medication is applied as a foam.
- [static let gel: HKMedicationGeneralForm](hkmedicationgeneralform/gel.md)
  The medication is applied as a gel.
- [static let inhaler: HKMedicationGeneralForm](hkmedicationgeneralform/inhaler.md)
  The medication is delivered through an inhaler.
- [static let injection: HKMedicationGeneralForm](hkmedicationgeneralform/injection.md)
  The medication is given as an injection.
- [static let liquid: HKMedicationGeneralForm](hkmedicationgeneralform/liquid.md)
  The medication is taken as a liquid, such as a syrup.
- [static let lotion: HKMedicationGeneralForm](hkmedicationgeneralform/lotion.md)
  The medication is applied as a lotion.
- [static let ointment: HKMedicationGeneralForm](hkmedicationgeneralform/ointment.md)
  The medication is applied as an ointment.
- [static let patch: HKMedicationGeneralForm](hkmedicationgeneralform/patch.md)
  The medication is applied as a patch worn on the skin.
- [static let powder: HKMedicationGeneralForm](hkmedicationgeneralform/powder.md)
  The medication is taken as a powder.
- [static let spray: HKMedicationGeneralForm](hkmedicationgeneralform/spray.md)
  The medication is delivered as a spray, for example a nasal spray or throat spray.
- [static let suppository: HKMedicationGeneralForm](hkmedicationgeneralform/suppository.md)
  The medication is delivered as a suppository.
- [static let tablet: HKMedicationGeneralForm](hkmedicationgeneralform/tablet.md)
  The medication comes in tablet form, such as a pill or caplet.
- [static let topical: HKMedicationGeneralForm](hkmedicationgeneralform/topical.md)
  The medication is applied topically in a form that wasn’t specified.
- [static let unknown: HKMedicationGeneralForm](hkmedicationgeneralform/unknown.md)
  The system doesn’t know the general form of the medication.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
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
- [class HKUserAnnotatedMedication](hkuserannotatedmedication.md)
  A reference to the tracked medication and the details a person can customize.
- [class HKUserAnnotatedMedicationQuery](hkuserannotatedmedicationquery.md)
- [class HKUserAnnotatedMedicationType](hkuserannotatedmedicationtype.md)
- [struct HKHealthConceptDomain](hkhealthconceptdomain.md)
  A domain that represents a health concept.
- [struct HKUserAnnotatedMedicationQueryDescriptor](hkuserannotatedmedicationquerydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationgeneralform)*