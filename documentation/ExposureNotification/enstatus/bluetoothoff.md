# ENStatus.bluetoothOff

**Framework**: Exposure Notification  
**Kind**: case  
**Role**: Case

Bluetooth is turned off.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
case bluetoothOff
```

```c
ENStatusBluetoothOff
```

#### Discussion

Bluetooth is required for Exposure Notification. If Bluetooth is disabled, notify the user that Exposure Notification can’t work without Bluetooth enabled.

> **Note**:  This may not match the state of Bluetooth as reported by CoreBluetooth.

Exposure Notification is a system service and can use Bluetooth in situations when apps cannot. For the purposes of notification of exposure, it’s better to use this API instead of CoreBluetooth.

## See Also

### States
- [ENStatus.active](./active.md)
  Notification is active.
- [ENStatus.disabled](./disabled.md)
  Notification is disabled.
- [ENStatus.restricted](./restricted.md)
  Notification is not active due to system restrictions, such as parental controls.
- [ENStatus.unknown](./unknown.md)
  Notification is unknown.
- [ENStatus.paused](./paused.md)
  The user paused Exposure Notification.
- [ENStatus.unauthorized](./unauthorized.md)
  The user hasn’t authorized Exposure Notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enstatus/bluetoothoff)*