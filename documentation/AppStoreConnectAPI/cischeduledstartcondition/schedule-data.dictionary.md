# CiScheduledStartCondition.Schedule

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The schedule of an Xcode Cloud workflow that starts a new build based on a schedule.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiScheduledStartCondition.Schedule
```

## Properties

- `days` ([string]): A list of days you configure for the start condition that starts a new build on a schedule.

  **Allowed Values**: `SUNDAY`, `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`
- `frequency` (string): A string indicating the frequency of the start condition that starts a new build on a schedule.

  **Allowed Values**: `WEEKLY`, `DAILY`, `HOURLY`
- `hour` (integer): An integer that represents the hour you configure for the start condition that starts a new build on a schedule.
- `minute` (integer): An integer that represents the minute you configure for the start condition that starts a new build on a schedule.
- `timezone` (string): A string that represents the time zone you configure for the start condition that starts a new build on a schedule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cischeduledstartcondition/schedule-data.dictionary)*