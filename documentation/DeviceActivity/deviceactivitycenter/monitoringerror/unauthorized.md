# DeviceActivityCenter.MonitoringError.unauthorized

**Framework**: DeviceActivity  
**Kind**: case

The calling process isn’t authorized to monitor device activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case unauthorized
```

#### Discussion

See the `FamilyControls` framework for more details about authorization to access the user’s device activity.

## See Also

- [DeviceActivityCenter.MonitoringError.excessiveActivities](deviceactivitycenter/monitoringerror/excessiveactivities.md)
  The calling process is monitoring too many activities.
- [DeviceActivityCenter.MonitoringError.intervalTooLong](deviceactivitycenter/monitoringerror/intervaltoolong.md)
  The activity’s schedule has an interval that is too long.
- [DeviceActivityCenter.MonitoringError.intervalTooShort](deviceactivitycenter/monitoringerror/intervaltooshort.md)
  The activity’s schedule has an interval that is too short.
- [DeviceActivityCenter.MonitoringError.invalidDateComponents](deviceactivitycenter/monitoringerror/invaliddatecomponents.md)
  The schedule’s date range is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror/unauthorized)*