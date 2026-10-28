# DeviceActivityCenter.MonitoringError.excessiveActivities

**Framework**: Device Activity  
**Kind**: case  
**Role**: Case

The calling process is monitoring too many activities.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case excessiveActivities
```

## Discussion

The maximum number of activities that can be monitored at one time by an app and its extensions is twenty.

## See Also

### Checking for Errors
- [DeviceActivityCenter.MonitoringError.intervalTooLong](./intervaltoolong.md)
  The activity’s schedule has an interval that is too long.
- [DeviceActivityCenter.MonitoringError.intervalTooShort](./intervaltooshort.md)
  The activity’s schedule has an interval that is too short.
- [DeviceActivityCenter.MonitoringError.invalidDateComponents](./invaliddatecomponents.md)
  The schedule’s date range is invalid.
- [DeviceActivityCenter.MonitoringError.unauthorized](./unauthorized.md)
  The calling process isn’t authorized to monitor device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror/excessiveactivities)*