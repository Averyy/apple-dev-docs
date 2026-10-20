# DeviceActivityCenter.MonitoringError

**Framework**: Device Activity  
**Kind**: enum  
**Role**: Enumeration

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
- [DeviceActivityCenter.MonitoringError.excessiveActivities](./monitoringerror/excessiveactivities.md)
  The calling process is monitoring too many activities.
- [DeviceActivityCenter.MonitoringError.intervalTooLong](./monitoringerror/intervaltoolong.md)
  The activity’s schedule has an interval that is too long.
- [DeviceActivityCenter.MonitoringError.intervalTooShort](./monitoringerror/intervaltooshort.md)
  The activity’s schedule has an interval that is too short.
- [DeviceActivityCenter.MonitoringError.invalidDateComponents](./monitoringerror/invaliddatecomponents.md)
  The schedule’s date range is invalid.
- [DeviceActivityCenter.MonitoringError.unauthorized](./monitoringerror/unauthorized.md)
  The calling process isn’t authorized to monitor device activity.
### Getting the Localized Message
- [var errorDescription: String?](./monitoringerror/errordescription.md)
  A localized message that describes what error occurred.
- [var recoverySuggestion: String?](./monitoringerror/recoverysuggestion.md)
  A localized message that describes how to recover from the failure.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror)*