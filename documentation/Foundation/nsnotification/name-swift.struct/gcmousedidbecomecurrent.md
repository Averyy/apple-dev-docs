# GCMouseDidBecomeCurrent

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A notification that posts when a mouse becomes the most recent mouse that the user connects.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let GCMouseDidBecomeCurrent: NSNotification.Name
```

## Discussion

The notification object is a [`GCMouse`](../../../GameController/gcmouse.md) object that represents the current mouse. For example, set the mouse input change handlers when you receive this notification.

The system posts this notification on the main actor.

## See Also

### Game Controller
- [static let GCControllerDidConnect: NSNotification.Name](./gccontrollerdidconnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](./gccontrollerdiddisconnect.md)
  A notification that posts after a controller disconnects from the device.
- [static let GCControllerDidBecomeCurrent: NSNotification.Name](./gccontrollerdidbecomecurrent.md)
  A notification that posts when a controller becomes the current controller.
- [static let GCControllerDidStopBeingCurrent: NSNotification.Name](./gccontrollerdidstopbeingcurrent.md)
  A notification that posts when a controller stops being the current controller.
- [static let GCControllerUserCustomizationsDidChange: NSNotification.Name](./gccontrollerusercustomizationsdidchange.md)
  A notification that posts when the user customizes the button mappings or other settings of a controller.
- [static let GCKeyboardDidConnect: NSNotification.Name](./gckeyboarddidconnect.md)
  A notification that posts after a keyboard connects to the device.
- [static let GCKeyboardDidDisconnect: NSNotification.Name](./gckeyboarddiddisconnect.md)
  A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.
- [static let GCMouseDidConnect: NSNotification.Name](./gcmousedidconnect.md)
  A notification that posts after a mouse connects to the device.
- [static let GCMouseDidDisconnect: NSNotification.Name](./gcmousediddisconnect.md)
  A notification that posts after a mouse disconnects from the device.
- [static let GCMouseDidStopBeingCurrent: NSNotification.Name](./gcmousedidstopbeingcurrent.md)
  A notification that posts when a mouse stops being the most recent mouse that the user connects.
- [static let GCRacingWheelDidConnect: NSNotification.Name](./gcracingwheeldidconnect.md)
  A notification that posts after a racing wheel controller connects to the device.
- [static let GCRacingWheelDidDisconnect: NSNotification.Name](./gcracingwheeldiddisconnect.md)
  A notification that posts after a racing wheel controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/gcmousedidbecomecurrent)*