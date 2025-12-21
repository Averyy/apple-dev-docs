# predicateForMedicationDoseEvent(scheduledStart:end:)

**Framework**: HealthKit  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class func predicateForMedicationDoseEvent(scheduledStart startDate: Date?, end endDate: Date?) -> NSPredicate
```

#### Discussion

Creates a predicate for use with HKQuery subclasses.

Creates a query predicate that matches HKMedicationDoseEvent samples that have a scheduled date within a window of scheduled times. If nil is provided to either parameter, the respective side of the window is unbound.

## Parameters

- `startDate`: The beginning of the window for scheduled dates of any medication dose event to match.
- `endDate`: The beginning of the window for scheduled dates of any medication dose event to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateformedicationdoseevent(scheduledstart:end:))*