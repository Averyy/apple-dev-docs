# ParentalControlsTimeLimits.Time-limits.Weekend-allowance

**Framework**: Device Management  
**Kind**: dictionary

The weekend allowance dictionary.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ParentalControlsTimeLimits.Time-limits.Weekend-allowance
```

## Properties

- `enabled` (boolean) *(required)*: If `true`, enable these settings.
- `end` (string): The curfew end time, in the format `%d:%d:%d`.
- `rangeType` (integer) *(required)*: The type of day range, which has the following possible values: - `0`: Weekday
- `1`: Weekend
- `secondsPerDay` (integer): The allowance for that day, in seconds.
- `start` (string): The curfew start time, in the format ‘%d:%d:%d’.

## See Also

- [object ParentalControlsTimeLimits.Time-limits.Weekday-allowance](parentalcontrolstimelimits/time-limits-data.dictionary/weekday-allowance-data.dictionary.md)
  The weekday allowance dictionary.
- [object ParentalControlsTimeLimits.Time-limits.Weekday-curfew](parentalcontrolstimelimits/time-limits-data.dictionary/weekday-curfew-data.dictionary.md)
  The weekday curfew dictionary.
- [object ParentalControlsTimeLimits.Time-limits.Weekend-curfew](parentalcontrolstimelimits/time-limits-data.dictionary/weekend-curfew-data.dictionary.md)
  The weekend curfew dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolstimelimits/time-limits-data.dictionary/weekend-allowance-data.dictionary)*