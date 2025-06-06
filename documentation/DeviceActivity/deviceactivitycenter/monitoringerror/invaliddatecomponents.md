# DeviceActivityCenter.MonitoringError.invalidDateComponents

**Framework**: DeviceActivity  
**Kind**: case

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

- [DeviceActivityCenter.MonitoringError.excessiveActivities](deviceactivitycenter/monitoringerror/excessiveactivities.md)
  The calling process is monitoring too many activities.
- [DeviceActivityCenter.MonitoringError.intervalTooLong](deviceactivitycenter/monitoringerror/intervaltoolong.md)
  The activity’s schedule has an interval that is too long.
- [DeviceActivityCenter.MonitoringError.intervalTooShort](deviceactivitycenter/monitoringerror/intervaltooshort.md)
  The activity’s schedule has an interval that is too short.
- [DeviceActivityCenter.MonitoringError.unauthorized](deviceactivitycenter/monitoringerror/unauthorized.md)
  The calling process isn’t authorized to monitor device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror/invaliddatecomponents)*