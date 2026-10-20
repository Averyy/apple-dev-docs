# DeviceActivityCenter.MonitoringError.invalidDateComponents

**Framework**: Device Activity  
**Kind**: case  
**Role**: Case

The schedule’s date range is invalid.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case invalidDateComponents
```

#### Discussion

The schedule’s start or end date components don’t match any future dates. Consider specifying a different calendar or different date components.

## See Also

### Checking for Errors
- [DeviceActivityCenter.MonitoringError.excessiveActivities](./excessiveactivities.md)
  The calling process is monitoring too many activities.
- [DeviceActivityCenter.MonitoringError.intervalTooLong](./intervaltoolong.md)
  The activity’s schedule has an interval that is too long.
- [DeviceActivityCenter.MonitoringError.intervalTooShort](./intervaltooshort.md)
  The activity’s schedule has an interval that is too short.
- [DeviceActivityCenter.MonitoringError.unauthorized](./unauthorized.md)
  The calling process isn’t authorized to monitor device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror/invaliddatecomponents)*