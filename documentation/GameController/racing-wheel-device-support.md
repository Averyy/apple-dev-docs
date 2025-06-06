# Racing wheel device support

**Framework**: Game Controller

Add support for racing wheel devices in macOS.

#### Overview

For macOS apps that support racing wheel devices, follow these steps for your app:

- If you distribute your app through the Mac App Store, add the [`com.apple.security.device.usb`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.device.usb) entitlement to your Xcode project.
- To get a racing wheel controller object, register for the [`GCRacingWheelDidConnect`](https://developer.apple.com/documentation/foundation/nsnotification/name/3930188-gcracingwheeldidconnect) (Swift) or  [`GCRacingWheelDidConnectNotification`](gcracingwheeldidconnectnotification.md) (Objective-C) and [`GCRacingWheelDidDisconnect`](https://developer.apple.com/documentation/foundation/nsnotification/name/3930189-gcracingwheeldiddisconnect) (Swift) or [`GCRacingWheelDidDisconnectNotification`](gcracingwheeldiddisconnectnotification.md) (Objective-C) notifications. Alternatively, check the `GCRacingWheel` [`connectedRacingWheels`](gcracingwheel/connectedracingwheels.md) class property for the currently connected controllers.
- To start receiving input from a racing wheel controller, invoke the `GCRacingWheel` [`acquireDevice()`](gcracingwheel/acquiredevice().md) method. Then use the [`relinquishDevice()`](gcracingwheel/relinquishdevice().md) method when you finish processing input.
- To process the input, set callbacks for the specific racing wheel elements that you want to receive input from. For example, set the [`valueDidChangeHandler`](gcphysicalinputprofile/valuedidchangehandler.md) property of the steering wheel and accelerator pedal elements. Get these elements using the [`wheel`](gcracingwheelinputstate/wheel.md) and [`acceleratorPedal`](gcracingwheelinputstate/acceleratorpedal.md) properties of the racing wheel’s [`wheelInput`](gcracingwheel/wheelinput.md) property, as in: `racingWheel.wheelInput.wheel`.
- If you just want the latest value of the steering wheel, use the `GCSteeringWheelElement` [`absoluteInput`](gcaxiselement/absoluteinput.md) property.
- For games that poll for input, set the input buffer size using the [`inputStateQueueDepth`](gcdevicephysicalinput/inputstatequeuedepth.md) property. In each iteration of your game loop, repeatedly invoke the [`nextInputState()`](gcracingwheelinput/nextinputstate().md) method until the queue is empty and it returns `nil`.

## Topics

### Racing wheel controller
- [class GCRacingWheel](gcracingwheel.md)
  An object that represents a physical racing wheel controller connected to a device.
### Racing wheel input
- [class GCRacingWheelInput](gcracingwheelinput.md)
  A controller profile that supports a racing wheel.
- [class GCRacingWheelInputState](gcracingwheelinputstate.md)
  The input for the wheel of a racing wheel controller.
### Left and right paddles
- [var GCInputLeftPaddle: String](gcinputleftpaddle-77y86.md)
  The name for the left paddle input.
- [var GCInputRightPaddle: String](gcinputrightpaddle-5klic.md)
  The name for the right paddle input.
### Gear shifter elements
- [protocol GCAxisInput](gcaxisinput.md)
  The common properties of inputs that provide absolute values along an axis with a fixed origin.
- [class GCGearShifterElement](gcgearshifterelement.md)
  An element that represents either a pattern or a sequential gear shift.
- [protocol GCRelativeInput](gcrelativeinput.md)
  The common properties of inputs that provide positions along an axis that are relative to the previous position.
### Steering and switch elements
- [class GCSteeringWheelElement](gcsteeringwheelelement.md)
  The element that represents the wheel of a racing wheel controller.
- [protocol GCSwitchPositionInput](gcswitchpositioninput.md)
  The common properties of inputs that switch between two or more positions.
### Directional pad elements
- [protocol GCLinearInput](gclinearinput.md)
  The common properties of inputs that provide values in unit coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/racing-wheel-device-support)*