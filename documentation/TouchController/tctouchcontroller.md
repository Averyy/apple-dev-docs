# TCTouchController

**Framework**: Touch Controller  
**Kind**: class

An object that allows you to create and customize on-screen touch controls for a game that uses Metal.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCTouchController
```

#### Overview

The controller exposes controls through a [`GCController`](https://developer.apple.com/documentation/GameController/GCController) instance, and enables seamless integration with the [`Game Controller`](https://developer.apple.com/documentation/GameController) framework.

This class manages the lifecycle of touch controls, handles user interaction, renders the controls using Metal, and provides a `GCController` instance that reflects the state of the on-screen controls.

## Topics

### Creating a touch controller
- [init(descriptor: TCTouchControllerDescriptor)](tctouchcontroller/init(descriptor:).md)
  Creates a new instance with the provided descriptor.
- [class TCTouchControllerDescriptor](tctouchcontrollerdescriptor.md)
  A descriptor for configuring a touch controller.
### Inspecting the touch controller
- [var buttons: [TCButton]](tctouchcontroller/buttons.md)
  An array containing all the button controls managed by this controller.
- [var controls: [any TCControl]](tctouchcontroller/controls.md)
  An array containing all the touch controls managed by this controller.
- [var device: any MTLDevice](tctouchcontroller/device.md)
  The Metal device the touch control uses for rendering the touch controls.
- [var directionPads: [TCDirectionPad]](tctouchcontroller/directionpads.md)
  An array containing all the direction pad controls managed by this controller.
- [var drawableSize: CGSize](tctouchcontroller/drawablesize.md)
  The size of the drawable to which the touch controller’s contents be drawn, in native pixels.
- [var size: CGSize](tctouchcontroller/size.md)
  The size of the view the touch controller’s drawable is embedded in, in points.
- [var switches: [TCSwitch]](tctouchcontroller/switches.md)
  An array containing all the switch controls managed by this controller.
- [var isConnected: Bool](tctouchcontroller/isconnected.md)
  A Boolean value that indicates whether the touch controller is connected to the Game Controller framework.
- [class var isSupported: Bool](tctouchcontroller/issupported.md)
  Whether touch controllers are supported for the device.
- [var throttles: [TCThrottle]](tctouchcontroller/throttles.md)
  An array containing all the throttle controls managed by this controller.
- [var thumbsticks: [TCThumbstick]](tctouchcontroller/thumbsticks.md)
  An array containing all the thumbstick controls managed by this controller.
- [var touchpads: [TCTouchpad]](tctouchcontroller/touchpads.md)
  An array containing all the touchpad controls managed by this controller.
### Getting the touch controller
- [var controller: GCController](tctouchcontroller/controller.md)
  The game controller instance associated with this touch controller.
### Adding a button control
- [func addButton(descriptor: TCButtonDescriptor) -> TCButton](tctouchcontroller/addbutton(descriptor:).md)
  Creates a new button control with the provided descriptor, and adds it to the touch controller.
- [class TCButtonDescriptor](tcbuttondescriptor.md)
  A descriptor for configuring a button.
### Adding a directional pad control
- [func addDirectionPad(descriptor: TCDirectionPadDescriptor) -> TCDirectionPad](tctouchcontroller/adddirectionpad(descriptor:).md)
  Creates a new direction pad control with the provided descriptor, and adds it to the touch controller.
- [class TCDirectionPadDescriptor](tcdirectionpaddescriptor.md)
  A descriptor for configuring a directional pad.
### Adding a switch control
- [func addSwitch(descriptor: TCSwitchDescriptor) -> TCSwitch](tctouchcontroller/addswitch(descriptor:).md)
  Creates a new switch control with the provided descriptor, and adds it to the touch controller.
- [class TCSwitchDescriptor](tcswitchdescriptor.md)
  A descriptor for configuring a switch.
### Adding a throttle control
- [func addThrottle(descriptor: TCThrottleDescriptor) -> TCThrottle](tctouchcontroller/addthrottle(descriptor:).md)
  Creates a new throttle control with the provided descriptor, and adds it to the touch controller.
- [class TCThrottleDescriptor](tcthrottledescriptor.md)
  A descriptor for configuring a throttle.
### Adding a thumbstick control
- [func addThumbstick(descriptor: TCThumbstickDescriptor) -> TCThumbstick](tctouchcontroller/addthumbstick(descriptor:).md)
  Creates a new thumbstick control with the provided descriptor, and adds it to the touch controller.
- [class TCThumbstickDescriptor](tcthumbstickdescriptor.md)
  A descriptor for configuring a thumbstick.
### Adding a touchpad control
- [func addTouchpad(descriptor: TCTouchpadDescriptor) -> TCTouchpad](tctouchcontroller/addtouchpad(descriptor:).md)
  Creates a new touchpad control with the provided descriptor, and adds it to the touch controller.
- [class TCTouchpadDescriptor](tctouchpaddescriptor.md)
  A descriptor for configuring a touchpad.
### Connecting and disconnecting a controller
- [func connect()](tctouchcontroller/connect.md)
  Connects the touch controller to the app, allowing its controls to be drawn and an associated `GCController` to be created.
- [func disconnect()](tctouchcontroller/disconnect.md)
  Disconnects the touch controller from the app, preventing its controls from being drawn.
### Getting the controller at a point
- [func control(at: CGPoint) -> (any TCControl)?](tctouchcontroller/control(at:).md)
  The control at the specified point, if any.
### Handling layout updates
- [func automaticallyLayoutControls(for: [TCControlLabel])](tctouchcontroller/automaticallylayoutcontrols(for:).md)
  Automatically lays out the provided control labels, creating them if needed.
- [func render(using: any MTLRenderCommandEncoder)](tctouchcontroller/render(using:).md)
  Renders the touch controls using the provided Metal render command encoder.
### Handling a touch
- [func handleTouchBegan(at: CGPoint, index: Int) -> Bool](tctouchcontroller/handletouchbegan(at:index:).md)
  Handles a touch began event at the specified point.
- [func handleTouchEnded(at: CGPoint, index: Int) -> Bool](tctouchcontroller/handletouchended(at:index:).md)
  Handles a touch ended event at the specified point.
- [func handleTouchMoved(at: CGPoint, index: Int) -> Bool](tctouchcontroller/handletouchmoved(at:index:).md)
  Handles a touch moved event at the specified point.
### Removing controls
- [func removeControl(any TCControl)](tctouchcontroller/removecontrol(_:).md)
  Removes the control from the touch controller.
- [func removeAllControls()](tctouchcontroller/removeallcontrols.md)
  Removes all controls from the touch controller.
### Getting the touch controller category
- [let TCGameControllerProductCategoryTouchController: String](tcgamecontrollerproductcategorytouchcontroller.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller)*