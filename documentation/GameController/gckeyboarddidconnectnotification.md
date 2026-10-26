# GCKeyboardDidConnectNotification

**Framework**: Game Controller  
**Kind**: var  
**Role**: Global Variable

A notification that posts after a keyboard connects to the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
extern NSString * const GCKeyboardDidConnectNotification;
```

#### Discussion

The notification object is a [`GCKeyboard`](./gckeyboard.md) object that represents the keyboard. If the user connects multiple keyboards, the framework posts this notification only after the first keyboard connects to the device.

The system posts this notification on the main thread.

## See Also

### Discovering keyboards
- [class var coalesced: GCKeyboard?](./gckeyboard/coalesced.md)
  The keyboard currently connected to the device.
- [GCKeyboardDidDisconnectNotification](./gckeyboarddiddisconnectnotification.md)
  A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboarddidconnectnotification)*