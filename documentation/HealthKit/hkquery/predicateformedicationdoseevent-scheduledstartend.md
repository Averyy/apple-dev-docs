# predicateForMedicationDoseEvent(scheduledStart:end:)

**Framework**: HealthKit  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class func predicateForMedicationDoseEvent(scheduledStart startDate: Date?, end endDate: Date?) -> NSPredicate
```

#### Discussion

Creates a query predicate that matches HKMedicationDoseEvent samples that have a scheduled date within a window of scheduled times. If nil is provided to either parameter, the respective side of the window is unbound.

## Parameters

- `startDate`: The beginning of the window for scheduled dates of any medication dose event to match.
- `endDate`: The beginning of the window for scheduled dates of any medication dose event to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateformedicationdoseevent(scheduledstart:end:))*