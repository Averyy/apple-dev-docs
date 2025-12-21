# GCKeyboard

**Framework**: Game Controller  
**Kind**: class

An object that represents a physical keyboard connected to a device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GCKeyboard
```

#### Overview

To get the keyboard object and its input values, register for the [`GCKeyboardDidConnect`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/GCKeyboardDidConnect) (Swift) or [`GCKeyboardDidConnectNotification`](gckeyboarddidconnectnotification.md) (Objective-C) notification for when a keyboard connects to the device, or use the [`coalesced`](gckeyboard/coalesced.md) class property. Then get the input values from the keyboard object’s [`keyboardInput`](gckeyboard/keyboardinput.md) controller profile.

## Topics

### Discovering keyboards
- [class var coalesced: GCKeyboard?](gckeyboard/coalesced.md)
  The keyboard currently connected to the device.
- [static let GCKeyboardDidConnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCKeyboardDidConnect.md)
  A notification that posts after a keyboard connects to the device.
- [static let GCKeyboardDidDisconnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCKeyboardDidDisconnect.md)
  A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.
### Getting input values
- [var keyboardInput: GCKeyboardInput?](gckeyboard/keyboardinput.md)
  The controller profile for the keyboard.
### Structures
- [GCKeyboard.DidConnectMessage](gckeyboard/didconnectmessage.md)
  A message that posts after a keyboard accessory connects to the device.
- [GCKeyboard.DidDisconnectMessage](gckeyboard/diddisconnectmessage.md)
  A message that posts after a keyboard accessory disconnects from the device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GCDevice](gcdevice.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [class GCMouse](gcmouse.md)
  An object that represents a physical mouse connected to a device.
- [class GCStylus](gcstylus.md)
  An object that represents a physical stylus connected to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboard)*