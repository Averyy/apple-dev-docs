# ENStatus

**Framework**: Exposure Notification  
**Kind**: enum

A set of cases that represents the overall status of exposure notification on the system.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
enum ENStatus
```

#### Overview

> ❗ **Important**:  This enumeration is available in iOS 12.5, and in iOS 13.5 and later.

## Topics

### States
- [ENStatus.active](enstatus/active.md)
  Notification is active.
- [ENStatus.bluetoothOff](enstatus/bluetoothoff.md)
  Bluetooth is turned off.
- [ENStatus.disabled](enstatus/disabled.md)
  Notification is disabled.
- [ENStatus.restricted](enstatus/restricted.md)
  Notification is not active due to system restrictions, such as parental controls.
- [ENStatus.unknown](enstatus/unknown.md)
  Notification is unknown.
- [ENStatus.paused](enstatus/paused.md)
  The user paused Exposure Notification.
- [ENStatus.unauthorized](enstatus/unauthorized.md)
  The user hasn’t authorized Exposure Notification.
### Initializers
- [init?(rawValue: Int)](enstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum ENAuthorizationStatus](enauthorizationstatus.md)
  A set of cases that indicates the authorization status for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enstatus)*