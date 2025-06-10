# predicateForUserAnnotatedMedications(hasSchedule:)

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
class func predicateForUserAnnotatedMedications(hasSchedule: Bool) -> NSPredicate
```

#### Discussion

Creates a query predicate that matches HKUserAnnotatedMedication objects that match the schedule status specified.

## Parameters

- `hasSchedule`: The schedule status of the medication. Ex: True will match medications that have a reminders schedule set up in the Health App.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforuserannotatedmedications(hasschedule:))*