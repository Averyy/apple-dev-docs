# HKUserAnnotatedMedicationQuery

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class HKUserAnnotatedMedicationQuery
```

```objc
@interface HKUserAnnotatedMedicationQuery : HKQuery
```

## Topics

### Initializers
- [init(predicate: NSPredicate?, limit: Int, resultsHandler: (HKUserAnnotatedMedicationQuery, HKUserAnnotatedMedication?, Bool, (any Error)?) -> Void)](./hkuserannotatedmedicationquery/init%28predicate,limit,resultshandler%29.md)

## Relationships

### Inherits From
- [HKQuery](./hkquery.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
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
- [class HKUserAnnotatedMedicationType](./hkuserannotatedmedicationtype.md)
- [struct HKHealthConceptDomain](./hkhealthconceptdomain.md)
  A domain that represents a health concept.
- [struct HKMedicationGeneralForm](./hkmedicationgeneralform.md)
  The manufactured form of a medication.
- [struct HKUserAnnotatedMedicationQueryDescriptor](./hkuserannotatedmedicationquerydescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkuserannotatedmedicationquery)*