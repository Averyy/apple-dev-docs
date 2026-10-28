# ENStatus.restricted

**Framework**: Exposure Notification  
**Kind**: case  
**Role**: Case

Notification is not active due to system restrictions, such as parental controls.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
case restricted
```

```c
ENStatusRestricted
```

## Discussion

When in this state, the app cannot enable exposure notification.

## See Also

### States
- [ENStatus.active](./active.md)
  Notification is active.
- [ENStatus.bluetoothOff](./bluetoothoff.md)
  Bluetooth is turned off.
- [ENStatus.disabled](./disabled.md)
  Notification is disabled.
- [ENStatus.unknown](./unknown.md)
  Notification is unknown.
- [ENStatus.paused](./paused.md)
  The user paused Exposure Notification.
- [ENStatus.unauthorized](./unauthorized.md)
  The user hasn’t authorized Exposure Notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enstatus/restricted)*