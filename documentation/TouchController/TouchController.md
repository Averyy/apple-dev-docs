# Touch Controller

**Framework**: Touch Controller  
**Kind**: module

Integrate onscreen touch controls into your Metal-based games.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

#### Overview

Use Touch Controller to add custom and interactive touch controls for your games. The framework offers a suite of controls that enable support for a variety of control schemes, like buttons, directional pads, thumbsticks, throttle controls, and touchpads. The Game Controller framework supports each control and surfaces them through a [`GCController`](https://developer.apple.com/documentation/GameController/GCController) instance.

Use the [`TCTouchController`](tctouchcontroller.md) class as the central point to manage and render your touch controls. To configure the appearance of your controls, use [`TCControlContents`](tccontrolcontents.md) and [`TCControlImage`](tccontrolimage.md). Use [`TCControlContents`](tccontrolcontents.md) to create a consistent look and feel with system-provided assets.

## Topics

### Essentials
- [class TCTouchController](tctouchcontroller.md)
  An object that allows you to create and customize on-screen touch controls for a game that uses Metal.
### Controls
- [protocol TCControl](tccontrol.md)
  A protocol that defines the base properties and methods for all touch controls.
- [class TCButton](tcbutton.md)
  A control that represents a single on-screen button.
- [class TCDirectionPad](tcdirectionpad.md)
  An object that represents a direction pad.
- [class TCSwitch](tcswitch.md)
  A control that represents a single on-screen switch.
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.
### Visuals
- [class TCControlContents](tccontrolcontents.md)
  Represents the visual contents of a touch control.
- [class TCControlImage](tccontrolimage.md)
  Represents an image to be rendered using Metal.
- [protocol TCControlLayout](tccontrollayout.md)
  A protocol defining the controlLayout properties for a control.
### System content
- [TCControlContents.ButtonShape](tccontrolcontents/buttonshape.md)
  Defines the visual shape of a button.
- [TCControlContents.DpadDirection](tccontrolcontents/dpaddirection.md)
  Defines the direction of a direction pad visual.
- [TCControlContents.DpadElementStyle](tccontrolcontents/dpadelementstyle.md)
  Defines the visual style of the individual up/down/left/right elements of a direction pad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TouchController)*