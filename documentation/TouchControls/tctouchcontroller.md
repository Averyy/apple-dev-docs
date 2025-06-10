# TCTouchController

**Framework**: Touch Controls  
**Kind**: class

An object that allows you to create and customize on-screen touch controls for a game that uses Metal.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class TCTouchController
```

#### Overview

The controller exposes controls through a [`GCController`](https://developer.apple.com/documentation/GameController/GCController) instance, and enables seamless integration with the [`Game Controller`](https://developer.apple.com/documentation/GameController) framework.

This class manages the lifecycle of touch controls, handles user interaction, renders the controls using Metal, and provides a `GCController` instance that reflects the state of the on-screen controls.

## Topics

### Initializers
- [init(descriptor: TCTouchControllerDescriptor)](tctouchcontroller/init(descriptor:).md)
  Creates a new instance with the provided descriptor.
### Instance Properties
- [var buttons: [TCButton]](tctouchcontroller/buttons.md)
  An array containing all the button controls managed by this controller.
- [var controls: [any TCControl]](tctouchcontroller/controls.md)
  An array containing all the touch controls managed by this controller.
- [var device: any MTLDevice](tctouchcontroller/device.md)
  The Metal device the touch control uses for rendering the touch controls.
- [var directionPads: [TCDirectionPad]](tctouchcontroller/directionpads.md)
  An array containing all the direction pad controls managed by this controller.
- [var isConnected: Bool](tctouchcontroller/isconnected.md)
  A Boolean value that indicates whether the touch controller is connected to the Game Controller framework.
- [var scaleFactor: CGFloat](tctouchcontroller/scalefactor.md)
  The scale factor of the screen.
- [var screenHeight: CGFloat](tctouchcontroller/screenheight.md)
  The height of the screen in points.
- [var screenWidth: CGFloat](tctouchcontroller/screenwidth.md)
  The width of the screen in points.
- [var throttles: [TCThrottle]](tctouchcontroller/throttles.md)
  An array containing all the throttle controls managed by this controller.
- [var thumbsticks: [TCThumbstick]](tctouchcontroller/thumbsticks.md)
  An array containing all the thumbstick controls managed by this controller.
- [var touchpads: [TCTouchpad]](tctouchcontroller/touchpads.md)
  An array containing all the touchpad controls managed by this controller.
### Instance Methods
- [func addButton(TCButton)](tctouchcontroller/addbutton(_:).md)
  Adds a button to the touch controller.
- [func addDirectionPad(TCDirectionPad)](tctouchcontroller/adddirectionpad(_:).md)
  Adds a direction pad to the touch controller.
- [func addThrottle(TCThrottle)](tctouchcontroller/addthrottle(_:).md)
  Adds a throttle to the touch controller.
- [func addThumbstick(TCThumbstick)](tctouchcontroller/addthumbstick(_:).md)
  Adds a thumbstick to the touch controller.
- [func addTouchpad(TCTouchpad)](tctouchcontroller/addtouchpad(_:).md)
  Adds a touchpad to the touch controller.
- [func button(with: TCButtonDescriptor) -> TCButton](tctouchcontroller/button(with:).md)
  Creates a new button control with the provided descriptor.
- [func connect()](tctouchcontroller/connect.md)
  Connects the touch controller to the app, allowing its controls to be drawn and an associated `GCController` to be created.
- [func control(at: CGPoint) -> (any TCControl)?](tctouchcontroller/control(at:).md)
  The control at the specified point, if any.
- [func controller() -> GCController](tctouchcontroller/controller.md)
  The game controller instance associated with this touch controller.
- [func directionPad(with: TCDirectionPadDescriptor) -> TCDirectionPad](tctouchcontroller/directionpad(with:).md)
  Creates a new direction pad control with the provided descriptor.
- [func disconnect()](tctouchcontroller/disconnect.md)
  Disconnects the touch controller from the app, preventing its controls from being drawn.
- [func drawableSizeWillChange(CGSize, scaleFactor: CGFloat)](tctouchcontroller/drawablesizewillchange(_:scalefactor:).md)
  Called when the drawable size changes.
- [func handleTouchBegan(at: CGPoint, index: NSNumber) -> Bool](tctouchcontroller/handletouchbegan(at:index:).md)
  Handles a touch began event at the specified point.
- [func handleTouchEnded(at: CGPoint, index: NSNumber) -> Bool](tctouchcontroller/handletouchended(at:index:).md)
  Handles a touch ended event at the specified point.
- [func handleTouchMoved(at: CGPoint, index: NSNumber) -> Bool](tctouchcontroller/handletouchmoved(at:index:).md)
  Handles a touch moved event at the specified point.
- [func removeAllButtons()](tctouchcontroller/removeallbuttons.md)
  Removes all buttons from the touch controller.
- [func removeAllControls()](tctouchcontroller/removeallcontrols.md)
  Removes all controls from the touch controller.
- [func removeAllDirectionPads()](tctouchcontroller/removealldirectionpads.md)
  Removes all direction pads from the touch controller.
- [func removeAllThrottles()](tctouchcontroller/removeallthrottles.md)
  Removes all throttles from the touch controller.
- [func removeAllThumbsticks()](tctouchcontroller/removeallthumbsticks.md)
  Removes all thumbsticks from the touch controller.
- [func removeAllTouchpads()](tctouchcontroller/removealltouchpads.md)
  Removes all touchpads from the touch controller.
- [func removeButton(TCButton)](tctouchcontroller/removebutton(_:).md)
  Removes a button from the touch controller.
- [func removeDirectionPad(TCDirectionPad)](tctouchcontroller/removedirectionpad(_:).md)
  Removes a direction pad from the touch controller.
- [func removeThrottle(TCThrottle)](tctouchcontroller/removethrottle(_:).md)
  Removes a throttle from the touch controller.
- [func removeThumbstick(TCThumbstick)](tctouchcontroller/removethumbstick(_:).md)
  Removes a thumbstick from the touch controller.
- [func removeTouchpad(TCTouchpad)](tctouchcontroller/removetouchpad(_:).md)
  Removes a touchpad from the touch controller.
- [func render(with: any MTLRenderCommandEncoder)](tctouchcontroller/render(with:).md)
  Renders the touch controls using the provided Metal render command encoder.
- [func setupDefaultLayout(for: [TCControlLabel])](tctouchcontroller/setupdefaultlayout(for:).md)
  Sets up a default layout for the provided control labels.
- [func throttle(with: TCThrottleDescriptor) -> TCThrottle](tctouchcontroller/throttle(with:).md)
  Creates a new throttle control with the provided descriptor.
- [func thumbstick(with: TCThumbstickDescriptor) -> TCThumbstick](tctouchcontroller/thumbstick(with:).md)
  Creates a new thumbstick control with the provided descriptor.
- [func touchpad(with: TCTouchpadDescriptor) -> TCTouchpad](tctouchcontroller/touchpad(with:).md)
  Creates a new touchpad control with the provided descriptor.

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

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontrols/tctouchcontroller)*