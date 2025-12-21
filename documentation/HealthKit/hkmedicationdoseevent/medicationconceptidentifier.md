# medicationConceptIdentifier

**Framework**: HealthKit  
**Kind**: property

The identifier of the medication concept the system associates with this dose event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@NSCopying
var medicationConceptIdentifier: HKHealthConceptIdentifier { get }
```

#### Discussion

The system uses this identifier to link the dose event back to its [`HKMedicationConcept`](hkmedicationconcept.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/medicationconceptidentifier)*