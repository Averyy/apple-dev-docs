# ENStatus.unknown

**Framework**: Exposure Notification  
**Kind**: case

Notification is unknown.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
case unknown
```

#### Discussion

This is the status before [`ENManager`](enmanager.md) has activated successfully.

## See Also

- [ENStatus.active](enstatus/active.md)
  Notification is active.
- [ENStatus.bluetoothOff](enstatus/bluetoothoff.md)
  Bluetooth is turned off.
- [ENStatus.disabled](enstatus/disabled.md)
  Notification is disabled.
- [ENStatus.restricted](enstatus/restricted.md)
  Notification is not active due to system restrictions, such as parental controls.
- [ENStatus.paused](enstatus/paused.md)
  The user paused Exposure Notification.
- [ENStatus.unauthorized](enstatus/unauthorized.md)
  The user hasn’t authorized Exposure Notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enstatus/unknown)*