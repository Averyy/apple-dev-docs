# GCController

**Framework**: Game Controller  
**Kind**: class

A representation of a real game controller, a virtual controller, or a snapshot of a controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCController
```

## Mentions

- [Adding touch controls to games that support game controllers in iOS](adding-touch-controls-to-games-that-support-game-controllers-in-ios.md)
- [Handling input events](handling-input-events.md)
- [Discovering and tracking spatial game controllers and styli](discovering-and-tracking-spatial-game-controllers-and-styli.md)

#### Overview

This class represents a real or virtual controller that a user interacts with during a game. A  is a physical controller that connects directly or wirelessly to the device. A real controller can be formfitting or can attach closely to a device so players can use controls on both simultaneously. A  is a software emulation of a real controller.

You discover controllers, and then you process the input from those controllers during gameplay. Use the [`controllers()`](gccontroller/controllers().md) method to get the currently connected controllers. If necessary, use the [`startWirelessControllerDiscovery(completionHandler:)`](gccontroller/startwirelesscontrollerdiscovery(completionhandler:).md) method to connect with wireless controllers.

This framework supports multiple connected game controllers. To identify which player is using a controller in a multiplayer game, check the [`playerIndex`](gccontroller/playerindex.md) property and set it, if necessary. For single-player games, use the [`current`](gccontroller/current.md) property to get the controller that the player is actively using.

A controller’s profile encapsulates the details about a controller’s buttons, pads, axis, and other input elements. Get the controller’s profile using one of the profile properties, such as [`extendedGamepad`](gccontroller/extendedgamepad.md), and then process the input from its elements.

You can either get the values of input elements on each iteration of your game loop, or set handlers to receive callbacks when those values change. For example, use the [`leftThumbstick`](gcextendedgamepad/leftthumbstick.md) property of the [`GCExtendedGamepad`](gcextendedgamepad.md) profile to get the thumbstick state. Use the [`valueChangedHandler`](gcextendedgamepad/valuechangedhandler.md) property to set a handler that you implement to process any input values that change in the profile.

Alternatively, you can create a snapshot of a real or virtual controller using the [`capture()`](gccontroller/capture().md) method. A  is a copy of a controller at a moment in time with its current element values. Creating a snapshot may impact performance, and over time a snapshot doesn’t stay current. Unlike other types of controllers, you can set the values of elements in a snapshot.

## Topics

### Discovering controllers
- [class func controllers() -> [GCController]](gccontroller/controllers.md)
  Returns the connected controllers for the device.
- [class func startWirelessControllerDiscovery(completionHandler: (() -> Void)?)](gccontroller/startwirelesscontrollerdiscovery(completionhandler:).md)
  Starts searching for nearby wireless controllers.
- [class func stopWirelessControllerDiscovery()](gccontroller/stopwirelesscontrollerdiscovery.md)
  Stops searching for nearby wireless controllers.
- [static let GCControllerDidConnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerDidConnect.md)
  A notification that posts after a controller connects to the device.
- [static let GCControllerDidDisconnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerDidDisconnect.md)
  A notification that posts after a controller disconnects from the device.
### Handling multiple controllers
- [class var current: GCController?](gccontroller/current.md)
  The most recently used game controller.
- [static let GCControllerDidBecomeCurrent: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerDidBecomeCurrent.md)
  A notification that posts when a controller becomes the current controller.
- [static let GCControllerDidStopBeingCurrent: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCControllerDidStopBeingCurrent.md)
  A notification that posts when a controller stops being the current controller.
### Inspecting a controller
- [var isAttachedToDevice: Bool](gccontroller/isattachedtodevice.md)
  A Boolean value that indicates whether the controller closely integrates with the device.
- [class func supportsHIDDevice(IOHIDDevice) -> Bool](gccontroller/supportshiddevice(_:).md)
  Returns a Boolean value that indicates whether the framework supports the specified human interface device.
- [class var shouldMonitorBackgroundEvents: Bool](gccontroller/shouldmonitorbackgroundevents.md)
  A Boolean value that indicates whether the app needs to respond to controller events when it isn’t the frontmost app.
### Accessing controller input
- [var input: GCControllerLiveInput](gccontroller/input.md)
  The input profile for the controller.
- [class GCControllerLiveInput](gccontrollerliveinput.md)
  The input profile for a controller.
- [class GCControllerInputState](gccontrollerinputstate.md)
  A class that represents an input state for gamepads and arcade sticks.
### Accessing controller profiles
- [var extendedGamepad: GCExtendedGamepad?](gccontroller/extendedgamepad.md)
  The extended gamepad profile.
- [class GCPhysicalInputProfile](gcphysicalinputprofile.md)
  The base class for controller profiles that support physical buttons, thumbsticks, and directional pads.
- [class GCKeyboardInput](gckeyboardinput.md)
  A controller profile that uses the keyboard as the input device.
- [class GCMouseInput](gcmouseinput.md)
  A controller profile that tracks input from a mouse.
- [class GCExtendedGamepad](gcextendedgamepad.md)
  A controller profile that supports the extended set of gamepad controls.
- [class GCDualShockGamepad](gcdualshockgamepad.md)
  A controller profile that supports the DualShock 4 controller.
- [class GCXboxGamepad](gcxboxgamepad.md)
  A controller profile that supports the Xbox controller.
- [class GCDualSenseGamepad](gcdualsensegamepad.md)
  A controller profile that supported the DualSense controller.
- [var microGamepad: GCMicroGamepad?](gccontroller/microgamepad.md)
  The micro gamepad profile.
- [class GCMicroGamepad](gcmicrogamepad.md)
  A controller profile that supports the Siri Remote.
- [class GCDirectionalGamepad](gcdirectionalgamepad.md)
  A profile that supports only the directional pad, without motion or rotation.
- [var motion: GCMotion?](gccontroller/motion.md)
  The motion input profile.
- [var physicalInputProfile: GCPhysicalInputProfile](gccontroller/physicalinputprofile.md)
  The physical input profile for the controller.
- [var gamepad: GCGamepad?](gccontroller/gamepad.md)
  The gamepad profile.
### Accessing controller elements
- [class GCControllerElement](gccontrollerelement.md)
  An input for a physical control, such as a button or thumbstick.
- [class GCControllerAxisInput](gccontrolleraxisinput.md)
  A control element that tracks movement along an axis.
- [class GCControllerButtonInput](gccontrollerbuttoninput.md)
  A control element that represents a button touch or press.
- [class GCControllerTouchpad](gccontrollertouchpad.md)
  A control element that represents a touch event on a touchpad.
- [class GCControllerDirectionPad](gccontrollerdirectionpad.md)
  A control element associated with a directional pad or a thumbstick.
- [class GCDeviceCursor](gcdevicecursor.md)
  A control element for the cursor used as a directional pad.
- [class GCDualSenseAdaptiveTrigger](gcdualsenseadaptivetrigger.md)
  A class that encapsulates the features of a DualSense adaptive trigger.
### Identifying controllers and displaying a player index
- [var playerIndex: GCControllerPlayerIndex](gccontroller/playerindex.md)
  The player index for the controller.
- [enum GCControllerPlayerIndex](gccontrollerplayerindex.md)
  The possible values for controller player indices.
### Accessing battery, haptics, and light objects
- [var battery: GCDeviceBattery?](gccontroller/battery.md)
  The controller’s battery information.
- [var haptics: GCDeviceHaptics?](gccontroller/haptics.md)
  The controller’s haptics information.
- [var light: GCDeviceLight?](gccontroller/light.md)
  The controller’s light settings.
### Creating snapshots
- [class func withExtendedGamepad() -> GCController](gccontroller/withextendedgamepad.md)
  Returns a snapshot of a newly created controller with an extended gamepad profile.
- [class func withMicroGamepad() -> GCController](gccontroller/withmicrogamepad.md)
  Returns a snapshot of a newly created controller with a micro gamepad profile.
- [func capture() -> GCController](gccontroller/capture.md)
  Returns a snapshot of the controller with its current element values.
- [var isSnapshot: Bool](gccontroller/issnapshot.md)
  A Boolean value that indicates whether the controller is a snapshot of a controller.
### Responding to a paused controller or controller event
- [var controllerPausedHandler: ((GCController) -> Void)?](gccontroller/controllerpausedhandler.md)
  The block that the framework calls when the user presses the pause button on the controller.
- [protocol GCGameControllerSceneDelegate](gcgamecontrollerscenedelegate.md)
- [class GCEventInteraction](gceventinteraction.md)
  An interaction that indicates the view’s intent to receive game controller events through the Game Controller framework.
### Identifying the activation context
- [class GCGameControllerActivationContext](gcgamecontrolleractivationcontext.md)
### Structures
- [GCController.DidBecomeCurrentMessage](gccontroller/didbecomecurrentmessage.md)
  A message that posts after a game controller becomes the most recently used controller.
- [GCController.DidConnectMessage](gccontroller/didconnectmessage.md)
  A message that posts after a game controller accessory connects to the device.
- [GCController.DidDisconnectMessage](gccontroller/diddisconnectmessage.md)
  A message that posts after a game controller accessory disconnects from the device.
- [GCController.DidStopBeingCurrentMessage](gccontroller/didstopbeingcurrentmessage.md)
  A message that posts after a game controller stops being the most recently used controller.

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
- [class GCRacingWheel](gcracingwheel.md)
  An object that represents a physical racing wheel controller connected to a device.
- [class GCKeyboard](gckeyboard.md)
  An object that represents a physical keyboard connected to a device.
- [class GCMouse](gcmouse.md)
  An object that represents a physical mouse connected to a device.
- [class GCStylus](gcstylus.md)
  An object that represents a physical stylus connected to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller)*