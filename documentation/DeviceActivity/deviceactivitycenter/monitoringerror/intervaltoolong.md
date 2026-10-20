# DeviceActivityCenter.MonitoringError.intervalTooLong

**Framework**: Device Activity  
**Kind**: case  
**Role**: Case

The activity’s schedule has an interval that is too long.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case intervalTooLong
```

#### Discussion

The maximum interval length for monitoring device activity events is one week.

## See Also

### Checking for Errors
- [DeviceActivityCenter.MonitoringError.excessiveActivities](./excessiveactivities.md)
  The calling process is monitoring too many activities.
- [DeviceActivityCenter.MonitoringError.intervalTooShort](./intervaltooshort.md)
  The activity’s schedule has an interval that is too short.
- [DeviceActivityCenter.MonitoringError.invalidDateComponents](./invaliddatecomponents.md)
  The schedule’s date range is invalid.
- [DeviceActivityCenter.MonitoringError.unauthorized](./unauthorized.md)
  The calling process isn’t authorized to monitor device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror/intervaltoolong)*