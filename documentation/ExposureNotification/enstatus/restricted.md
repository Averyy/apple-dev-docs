# ENStatus.restricted

**Framework**: Exposure Notification  
**Kind**: case

Notification is not active due to system restrictions, such as parental controls.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
case restricted
```

#### Discussion

When in this state, the app cannot enable exposure notification.

## See Also

- [ENStatus.active](enstatus/active.md)
  Notification is active.
- [ENStatus.bluetoothOff](enstatus/bluetoothoff.md)
  Bluetooth is turned off.
- [ENStatus.disabled](enstatus/disabled.md)
  Notification is disabled.
- [ENStatus.unknown](enstatus/unknown.md)
  Notification is unknown.
- [ENStatus.paused](enstatus/paused.md)
  The user paused Exposure Notification.
- [ENStatus.unauthorized](enstatus/unauthorized.md)
  The user hasn’t authorized Exposure Notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enstatus/restricted)*