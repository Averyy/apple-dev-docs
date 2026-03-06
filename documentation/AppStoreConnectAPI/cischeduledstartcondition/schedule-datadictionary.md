# CiScheduledStartCondition.Schedule

**Framework**: App Store Connect API  
**Kind**: dictionary

The schedule of an Xcode Cloud workflow that starts a new build based on a schedule.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiScheduledStartCondition.Schedule
```

## Properties

- `days` ([string]): A list of days you configure for the start condition that starts a new build on a schedule.
- `frequency` (string): A string indicating the frequency of the start condition that starts a new build on a schedule.
- `hour` (integer): An integer that represents the hour you configure for the start condition that starts a new build on a schedule.
- `minute` (integer): An integer that represents the minute you configure for the start condition that starts a new build on a schedule.
- `timezone` (string): A string that represents the time zone you configure for the start condition that starts a new build on a schedule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cischeduledstartcondition/schedule-data.dictionary)*