# GCKeyboardDidConnect

**Framework**: Foundation  
**Kind**: property

A notification that posts after a keyboard connects to the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let GCKeyboardDidConnect: NSNotification.Name
```

#### Discussion

The notification object is a [`GCKeyboard`](https://developer.apple.com/documentation/GameController/GCKeyboard) object that represents the keyboard. If the user connects multiple keyboards, the framework posts this notification only after the first keyboard connects to the device.

## See Also

- [static let GCControllerDidConnect: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerdidconnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerdiddisconnect.md)
  A notification that posts after a controller disconnects from the device.
- [static let GCControllerDidBecomeCurrent: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerdidbecomecurrent.md)
  A notification that posts when a controller becomes the current controller.
- [static let GCControllerDidStopBeingCurrent: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerdidstopbeingcurrent.md)
  A notification that posts when a controller stops being the current controller.
- [static let GCControllerUserCustomizationsDidChange: NSNotification.Name](nsnotification/name-swift.struct/gccontrollerusercustomizationsdidchange.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.
- [static let GCKeyboardDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gckeyboarddiddisconnect.md)
  A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.
- [static let GCMouseDidBecomeCurrent: NSNotification.Name](nsnotification/name-swift.struct/gcmousedidbecomecurrent.md)
  A notification that posts when a mouse becomes the most recent mouse that the user connects.
- [static let GCMouseDidConnect: NSNotification.Name](nsnotification/name-swift.struct/gcmousedidconnect.md)
  A notification that posts after a mouse connects to the device.
- [static let GCMouseDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gcmousediddisconnect.md)
  A notification that posts after a mouse disconnects from the device.
- [static let GCMouseDidStopBeingCurrent: NSNotification.Name](nsnotification/name-swift.struct/gcmousedidstopbeingcurrent.md)
  A notification that posts when a mouse stops being the most recent mouse that the user connects.
- [static let GCRacingWheelDidConnect: NSNotification.Name](nsnotification/name-swift.struct/gcracingwheeldidconnect.md)
  A notification that posts after a racing wheel controller connects to the device.
- [static let GCRacingWheelDidDisconnect: NSNotification.Name](nsnotification/name-swift.struct/gcracingwheeldiddisconnect.md)
  A notification that posts after a racing wheel controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/gckeyboarddidconnect)*