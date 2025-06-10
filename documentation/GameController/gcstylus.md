# GCStylus

**Framework**: Game Controller  
**Kind**: class

An object that represents a physical stylus connected to the device.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
class GCStylus
```

## Mentions

- [Discovering and tracking spatial game controllers and styli](discovering-and-tracking-spatial-game-controllers-and-styli.md)

#### Overview

Use the `styli` property to get the currently connect stylus accessories when your application starts.  Register for `GCStylusDidConnectNotification` and `GCStylusDidDisconnectNotification` to get notified when a stylus connects of disconnects while your application is running.

```None
// Register for notifications
NotificationCenter.default.addObserver(self, selector: #selector(stylus(didConnect:)), name: NSNotification.Name.GCStylusDidConnect, object: nil)
NotificationCenter.default.addObserver(self, selector: #selector(stylus(didDisconnect:)), name: NSNotification.Name.GCStylusDidConnect, object: nil)

// Query current stylus devices
for stylus in GCStylus.styluses {
    ...
}

// Later, handle connection
@objc func stylus(didConnect notification: Notification) {
    guard let stylus = notification.object as? GCStylus else { return }
    ...
}
```

Check the `productCategory` to determine the type of stylus.  A spatial stylus - capable of 6DoF tracking by Apple Vision Pro - has a `GCProductCategorySpatialStylus` category.

Use the `input` property to get the input profile of the stylus.  A spatial stylus includes a pressure sensitive tip and an input cluster composed of two buttons.

- The primary button (`GCInputStylusPrimaryButton`) is the front button (closest to the stylus tip) in the input cluster of the stylus.  This button is frequently used grab virtual objects.
- The secondary button (`GCInputStylusSecondaryButton`) is the middle button in the input cluster.  It can measures pressure/force levels. It’s intended to be used for controlling in-air drawing, selection, and generic interactions.
- The tip is also represented as a button (`GCInputStylusTip`).

```None
guard let input = stylus.input else { return }
input.inputStateQueueDepth = 20
input.inputStateAvailableHandler = { input in
    // This block will be enqueued for execution when the state of
    // any stylus input changes.

    // Iterate through all input state changes since last execution of
    // the block.
    while let nextState = input.nextInputState() {
        // Use the value of `pressedInput.isPressed` for binary
        // interactions, such as object selection.
        let primaryButtonPressed = nextState.buttons[.stylusPrimaryButton]?.pressedInput.isPressed
        let secondaryButtonPressed = nextState.buttons[.stylusSecondaryButton]?.pressedInput.isPressed
        // Use the normalized press value for analog actions such as
        // controlling virtual ink flow.
        let secondaryButtonPressure = nextState.buttons[.stylusSecondaryButton]?.pressedInput.value
        let tipPressure = nextState.buttons[.stylusTip]?.pressedInput.value

        ...
    }
}
```

Use the `haptics` property to get the haptics profile of the stylus.  A spatial stylus may optionally support haptic feedback to a single locality - `GCHapticsLocalityDefault`.

## Topics

### Accessing the styli
- [class var styli: [GCStylus]](gcstylus/styli.md)
  Get the collection of stylus accessories currently connected to the device.
### Getting input values and haptics
- [var input: (any GCDevicePhysicalInput)?](gcstylus/input.md)
  Gets the input profile for the stylus.
- [var haptics: GCDeviceHaptics?](gcstylus/haptics.md)
  Gets the haptics profile for the stylus, if supported.
### Retrieving the buttons
- [var GCInputStylusPrimaryButton: String](gcinputstylusprimarybutton-18g2p.md)
- [var GCInputStylusSecondaryButton: String](gcinputstylussecondarybutton-6r3q.md)
- [var GCInputStylusTip: String](gcinputstylustip-1rhuw.md)
### Type Properties
- [class var styluses: [GCStylus]](gcstylus/styluses.md)

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
- [class GCKeyboard](gckeyboard.md)
  An object that represents a physical keyboard connected to a device.
- [class GCMouse](gcmouse.md)
  An object that represents a physical mouse connected to a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcstylus)*