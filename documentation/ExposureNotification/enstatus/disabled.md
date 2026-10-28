# ENStatus.disabled

**Framework**: Exposure Notification  
**Kind**: case  
**Role**: Case

Notification is disabled.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
case disabled
```

```c
ENStatusDisabled
```

## Discussion

Use [`setExposureNotificationEnabled(_:completionHandler:)`](../enmanager/setexposurenotificationenabled%28_,completionhandler%29.md) to enable exposure notification.

## See Also

### States
- [ENStatus.active](./active.md)
  Notification is active.
- [ENStatus.bluetoothOff](./bluetoothoff.md)
  Bluetooth is turned off.
- [ENStatus.restricted](./restricted.md)
  Notification is not active due to system restrictions, such as parental controls.
- [ENStatus.unknown](./unknown.md)
  Notification is unknown.
- [ENStatus.paused](./paused.md)
  The user paused Exposure Notification.
- [ENStatus.unauthorized](./unauthorized.md)
  The user hasn’t authorized Exposure Notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enstatus/disabled)*