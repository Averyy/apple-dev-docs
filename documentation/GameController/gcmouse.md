# GCMouse

**Framework**: Game Controller  
**Kind**: class

An object that represents a physical mouse connected to a device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCMouse
```

#### Overview

To get a mouse object and its input values, register for the [`GCMouseDidConnect`](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/gcmousedidconnect) (Swift) or [`GCMouseDidConnectNotification`](gcmousedidconnectnotification.md) (Objective-C) notification for when a mouse connects to the device. Then register for the [`GCMouseDidBecomeCurrent`](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/gcmousedidbecomecurrent)  (Swift) or [`GCMouseDidBecomeCurrentNotification`](gcmousedidbecomecurrentnotification.md) (Objective-C) notification for when it becomes the [`current`](gcmouse/current.md) mouse. Alternatively, use the [`current`](gcmouse/current.md) class property or the [`mice()`](gcmouse/mice().md) class method to get a mouse object. Then get the current input values from the mouse object’s [`mouseInput`](gcmouse/mouseinput.md) controller profile.

## Topics

### Discovering mouse devices
- [class func mice() -> [GCMouse]](gcmouse/mice.md)
  Returns any mice that the user connects to the device.
- [static let GCMouseDidConnect: NSNotification.Name](../foundation/nsnotification/name-swift.struct/gcmousedidconnect.md)
  A notification that posts after a mouse connects to the device.
- [static let GCMouseDidDisconnect: NSNotification.Name](../foundation/nsnotification/name-swift.struct/gcmousediddisconnect.md)
  A notification that posts after a mouse disconnects from the device.
### Handling multiple mouse devices
- [class var current: GCMouse?](gcmouse/current.md)
  The most recent mouse that the user connects.
- [static let GCMouseDidBecomeCurrent: NSNotification.Name](../foundation/nsnotification/name-swift.struct/gcmousedidbecomecurrent.md)
  A notification that posts when a mouse becomes the most recent mouse that the user connects.
- [static let GCMouseDidStopBeingCurrent: NSNotification.Name](../foundation/nsnotification/name-swift.struct/gcmousedidstopbeingcurrent.md)
  A notification that posts when a mouse stops being the most recent mouse that the user connects.
### Getting input values
- [var mouseInput: GCMouseInput?](gcmouse/mouseinput.md)
  The controller profile for the mouse device.
### Structures
- [GCMouse.DidBecomeCurrentMessage](gcmouse/didbecomecurrentmessage.md)
  A message that posts after a mouse becomes the most recently used mouse.
- [GCMouse.DidConnectMessage](gcmouse/didconnectmessage.md)
  A message that posts after a mouse accessory connects to the device.
- [GCMouse.DidDisconnectMessage](gcmouse/diddisconnectmessage.md)
  A message that posts after a mouse accessory disconnects from the device.
- [GCMouse.DidStopBeingCurrentMessage](gcmouse/didstopbeingcurrentmessage.md)
  A message that posts after a mouse stops being the most recently used mouse.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [GCDevice](gcdevice.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Supporting Game Controllers](supporting-game-controllers.md)
  Support a physical controller or add a virtual controller to enhance how people interact with your game through haptics, lighting, and motion sensing.
- [Letting players use their second-generation Siri Remote as a game controller](letting-players-use-their-second-generation-siri-remote-as-a-game-controller.md)
  Support the second-generation Siri Remote as a game controller in your Apple TV game.
- [Discovering and tracking spatial game controllers and styli](discovering-and-tracking-spatial-game-controllers-and-styli.md)
  Receive controller and stylus input to interact with content in your augmented reality app.
- [protocol GCDevice](gcdevice.md)
  A protocol that defines a common interface for game input devices.
- [class GCController](gccontroller.md)
  A representation of a real game controller, a virtual controller, or a snapshot of a controller.
- [class GCRacingWheel](gcracingwheel.md)
  An object that represents a physical racing wheel controller connected to a device.
- [class GCKeyboard](gckeyboard.md)
  An object that represents a physical keyboard connected to a device.
- [class GCStylus](gcstylus.md)
  An object that represents a physical stylus connected to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouse)*