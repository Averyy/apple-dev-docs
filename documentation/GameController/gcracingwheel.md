# GCRacingWheel

**Framework**: Game Controller  
**Kind**: class

An object that represents a physical racing wheel controller connected to a device.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class GCRacingWheel
```

## Mentions

- [Handling input events](handling-input-events.md)

## Topics

### Discovering racing wheels
- [class var connectedRacingWheels: Set<GCRacingWheel>](gcracingwheel/connectedracingwheels.md)
  The racing wheels connected to the device.
- [static let GCRacingWheelDidConnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCRacingWheelDidConnect.md)
  A notification that posts after a racing wheel controller connects to the device.
- [static let GCRacingWheelDidDisconnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCRacingWheelDidDisconnect.md)
  A notification that posts after a racing wheel controller disconnects from the device.
### Getting events
- [func acquireDevice() throws](gcracingwheel/acquiredevice.md)
  Starts receiving events from the racing wheel.
- [func relinquishDevice()](gcracingwheel/relinquishdevice.md)
  Stops receiving events from the racing wheel.
- [var isAcquired: Bool](gcracingwheel/isacquired.md)
  A Boolean value that indicates whether the racing wheel sends events to the app.
### Accessing the controller profile
- [var wheelInput: GCRacingWheelInput](gcracingwheel/wheelinput.md)
  The physical input profile for the racing wheel.
### Creating snapshots
- [func capture() -> GCRacingWheel](gcracingwheel/capture.md)
  Returns a snapshot of the racing wheel with its current element values.
- [var isSnapshot: Bool](gcracingwheel/issnapshot.md)
  A Boolean value that indicates whether the object is a snapshot of a racing wheel.

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
- [class GCKeyboard](gckeyboard.md)
  An object that represents a physical keyboard connected to a device.
- [class GCMouse](gcmouse.md)
  An object that represents a physical mouse connected to a device.
- [class GCStylus](gcstylus.md)
  An object that represents a physical stylus connected to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheel)*