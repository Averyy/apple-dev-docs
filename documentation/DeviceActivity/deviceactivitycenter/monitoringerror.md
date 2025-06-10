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
- [var failureReason: String?](deviceactivitycenter/monitoringerror/failurereason.md)
  A localized message that describes the reason for the failure.
- [var helpAnchor: String?](deviceactivitycenter/monitoringerror/helpanchor.md)
  A localized message that provides a help text if the user requests help.
- [var localizedDescription: String](deviceactivitycenter/monitoringerror/localizeddescription.md)
  A string that contains the localized description of the error.
- [var recoverySuggestion: String?](deviceactivitycenter/monitoringerror/recoverysuggestion.md)
  A localized message that describes how to recover from the failure.
### Comparing Errors
- [static func != (Self, Self) -> Bool](deviceactivitycenter/monitoringerror/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
### Operators
- [static func == (DeviceActivityCenter.MonitoringError, DeviceActivityCenter.MonitoringError) -> Bool](deviceactivitycenter/monitoringerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](deviceactivitycenter/monitoringerror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](deviceactivitycenter/monitoringerror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](deviceactivitycenter/monitoringerror/equatable-implementations.md)
- [Error Implementations](deviceactivitycenter/monitoringerror/error-implementations.md)
- [LocalizedError Implementations](deviceactivitycenter/monitoringerror/localizederror-implementations.md)

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