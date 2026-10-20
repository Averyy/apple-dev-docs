# ENStatus.unknown

**Framework**: Exposure Notification  
**Kind**: case  
**Role**: Case

Notification is unknown.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
case unknown
```

```c
ENStatusUnknown
```

#### Discussion

This is the status before [`ENManager`](../enmanager.md) has activated successfully.

## See Also

### States
- [ENStatus.active](./active.md)
  Notification is active.
- [ENStatus.bluetoothOff](./bluetoothoff.md)
  Bluetooth is turned off.
- [ENStatus.disabled](./disabled.md)
  Notification is disabled.
- [ENStatus.restricted](./restricted.md)
  Notification is not active due to system restrictions, such as parental controls.
- [ENStatus.paused](./paused.md)
  The user paused Exposure Notification.
- [ENStatus.unauthorized](./unauthorized.md)
  The user hasn’t authorized Exposure Notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enstatus/unknown)*