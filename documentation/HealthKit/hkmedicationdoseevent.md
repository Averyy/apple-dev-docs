# HKMedicationDoseEvent

**Framework**: HealthKit  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class HKMedicationDoseEvent
```

## Topics

### Instance Properties
- [var doseQuantity: Double?](hkmedicationdoseevent/dosequantity-4cb5m.md)
  The quantity of the medication taken.
- [var logStatus: HKMedicationDoseEvent.LogStatus](hkmedicationdoseevent/logstatus-swift.property.md)
  The log status the system assigns to this dose event.
- [var medicationConceptIdentifier: HKHealthConceptIdentifier](hkmedicationdoseevent/medicationconceptidentifier.md)
  The identifier of the medication concept the system associates with this dose event.
- [var medicationDoseEventType: HKMedicationDoseEventType](hkmedicationdoseevent/medicationdoseeventtype.md)
  The data type that identified the samples that store medication dose event data.
- [var scheduleType: HKMedicationDoseEvent.ScheduleType](hkmedicationdoseevent/scheduletype-swift.property.md)
  The scheduling context for this logged dose event.
- [var scheduledDate: Date?](hkmedicationdoseevent/scheduleddate.md)
  The date and time the person takes the medication, if scheduled.
- [var scheduledDoseQuantity: Double?](hkmedicationdoseevent/scheduleddosequantity-477ge.md)
  The quantity of the medication scheduled to be taken.
- [var unit: HKUnit](hkmedicationdoseevent/unit.md)
  The unit that the system associates with the medication when the person logs the dose.
### Enumerations
- [HKMedicationDoseEvent.LogStatus](hkmedicationdoseevent/logstatus-swift.enum.md)
  The statuses the system assigns to a logged medication dose event.
- [HKMedicationDoseEvent.ScheduleType](hkmedicationdoseevent/scheduletype-swift.enum.md)
  The kind of schedule the system associates with a logged medication dose event.

## Relationships

### Inherits From
- [HKSample](hksample.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent)*