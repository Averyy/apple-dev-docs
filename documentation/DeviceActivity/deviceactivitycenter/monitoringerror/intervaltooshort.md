# DeviceActivityCenter.MonitoringError.intervalTooShort

**Framework**: DeviceActivity  
**Kind**: case

The activity’s schedule has an interval that is too short.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case intervalTooShort
```

#### Discussion

The minimum interval length for monitoring device activity is fifteen minutes.

## See Also

- [DeviceActivityCenter.MonitoringError.excessiveActivities](deviceactivitycenter/monitoringerror/excessiveactivities.md)
  The calling process is monitoring too many activities.
- [DeviceActivityCenter.MonitoringError.intervalTooLong](deviceactivitycenter/monitoringerror/intervaltoolong.md)
  The activity’s schedule has an interval that is too long.
- [DeviceActivityCenter.MonitoringError.invalidDateComponents](deviceactivitycenter/monitoringerror/invaliddatecomponents.md)
  The schedule’s date range is invalid.
- [DeviceActivityCenter.MonitoringError.unauthorized](deviceactivitycenter/monitoringerror/unauthorized.md)
  The calling process isn’t authorized to monitor device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror/intervaltooshort)*