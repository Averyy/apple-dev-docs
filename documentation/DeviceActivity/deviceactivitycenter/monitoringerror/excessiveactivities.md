# DeviceActivityCenter.MonitoringError.excessiveActivities

**Framework**: DeviceActivity  
**Kind**: case

The calling process is monitoring too many activities.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case excessiveActivities
```

#### Discussion

The maximum number of activities that can be monitored at one time by an app and its extensions is twenty.

## See Also

- [DeviceActivityCenter.MonitoringError.intervalTooLong](deviceactivitycenter/monitoringerror/intervaltoolong.md)
  The activity’s schedule has an interval that is too long.
- [DeviceActivityCenter.MonitoringError.intervalTooShort](deviceactivitycenter/monitoringerror/intervaltooshort.md)
  The activity’s schedule has an interval that is too short.
- [DeviceActivityCenter.MonitoringError.invalidDateComponents](deviceactivitycenter/monitoringerror/invaliddatecomponents.md)
  The schedule’s date range is invalid.
- [DeviceActivityCenter.MonitoringError.unauthorized](deviceactivitycenter/monitoringerror/unauthorized.md)
  The calling process isn’t authorized to monitor device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror/excessiveactivities)*