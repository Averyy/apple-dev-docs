# DeviceActivityCenter.MonitoringError

**Framework**: DeviceActivity  
**Kind**: enum

Errors that may occur when starting to monitor an activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum MonitoringError
```

## Topics

### Checking for Errors
- [DeviceActivityCenter.MonitoringError.excessiveActivities](deviceactivitycenter/monitoringerror/excessiveactivities.md)
  The calling process is monitoring too many activities.
- [DeviceActivityCenter.MonitoringError.intervalTooLong](deviceactivitycenter/monitoringerror/intervaltoolong.md)
  The activity’s schedule has an interval that is too long.
- [DeviceActivityCenter.MonitoringError.intervalTooShort](deviceactivitycenter/monitoringerror/intervaltooshort.md)
  The activity’s schedule has an interval that is too short.
- [DeviceActivityCenter.MonitoringError.invalidDateComponents](deviceactivitycenter/monitoringerror/invaliddatecomponents.md)
  The schedule’s date range is invalid.
- [DeviceActivityCenter.MonitoringError.unauthorized](deviceactivitycenter/monitoringerror/unauthorized.md)
  The calling process isn’t authorized to monitor device activity.
### Getting the Localized Message
- [var errorDescription: String?](deviceactivitycenter/monitoringerror/errordescription.md)
  A localized message that describes what error occurred.
- [var recoverySuggestion: String?](deviceactivitycenter/monitoringerror/recoverysuggestion.md)
  A localized message that describes how to recover from the failure.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror)*