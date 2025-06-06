# Letting players use their second-generation Siri Remote as a game controller

**Framework**: Game Controller

Support the second-generation Siri Remote as a game controller in your Apple TV game.

#### Overview

To add support for the second-generation Siri Remote in your Apple TV game, you make a few changes to your Xcode project and code.

##### Configure Your Project

First configure your Xcode project to handle directional gamepads and multiple micro gamepads.

On the Signing & Capabilities tab in the project editor, add the Game Controllers capability to your project and check Directional Gamepad under Game Controllers. For more information, see [`Configuring game controllers`](https://developer.apple.com/documentation/Xcode/configuring-game-controllers).

On the Info tab, add the [`GCSupportsMultipleMicroGamepads`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportsMultipleMicroGamepads) key and set the value to `YES`. For more information, see [`Managing Your App’s Information Property List`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list).

##### Handle Multiple Micro Gamepads

In your code, handle multiple micro gamepad connections. When a game controller connects, check if the controller is a directional gamepad using the [`isKind(of:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isKind(of:)) method:

```swift
if controller.microGamepad isKind(of: GCDirectionalGamepad.class) {
   ...
}
```

Check if the device category is second-generation Siri Remote using the [`productCategory`](gcdevice/productcategory.md) property:

```swift
if device.productCategory == GCProductCategorySiriRemote2ndGen {
   ...
}
```

If these conditions are true, you can use the connected second-generation Siri Remote as a game controller.

##### Access the Remote Buttons and Directional Pad

To access the center button of the second-generation Siri Remote, use the [`buttons`](gcdevicephysicalinputstate/buttons-3257g.md) property:

```swift
controller.physicalInputProfile.buttons[GCInputDirectionalCenterButton]
```

Then to access the directional pad, use the [`dpads`](gcdevicephysicalinputstate/dpads-5yr9x.md) property:

```swift
controller.physicalInputProfile.dpads[GCInputDirectionalCardinalDpad]
```

If your game requires an analog touch surface, check whether the directional pad is digital using the [`isAnalog`](gccontrollerelement/isanalog.md) property:

```swift
if physicalInputProfile.dpads[GCInputDirectionalDpad].isAnalog == false
```

For example, the Universal Electronic remote that works with Apple TV is a directional gamepad but with physical non-analog buttons.

## See Also

- [Supporting Game Controllers](supporting-game-controllers.md)
  Support a physical controller or add a virtual controller to enhance how people interact with your game through haptics, lighting, and motion sensing.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/letting-players-use-their-second-generation-siri-remote-as-a-game-controller)*