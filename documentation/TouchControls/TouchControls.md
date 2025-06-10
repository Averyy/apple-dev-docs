# Touch Controls

**Framework**: Touch Controls  
**Kind**: module

Integrate on-screen touch controls into your Metal-based games.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

#### Overview

Use Touch Controls to add custom and interactive touch controls for your games. The framework offers a suite of controls that enable support for a variety of control schemes, for example, buttons, direction pads, thumbsticks, throttles, and touchpads. The Game Controller framework supports each control and surfaces them through a [`GCController`](https://developer.apple.com/documentation/GameController/GCController) instance.

Use the [`TCTouchController`](tctouchcontroller.md) class as the central point to manage and render your touch controls. To configure the appearance of your controls, use [`TCControlVisuals`](tccontrolvisuals.md) and [`TCSpriteRenderer`](tcspriterenderer.md). Use [`TCControlSystemVisualsProvider`](tccontrolsystemvisualsprovider.md) to create a consistent look and feel with system-provided assets.

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
- [class TCThumbstick](tcthumbstick.md)
  Represents a single on-screen thumbstick.
- [class TCThrottle](tcthrottle.md)
  Represents a single on-screen throttle - a one axis input.
- [class TCTouchpad](tctouchpad.md)
  Represents a single on-screen touchpad that reports absolute coordinates or delta movements.
### Visuals
- [class TCControlVisuals](tccontrolvisuals.md)
  Represents the visual elements of a touch control.
- [class TCSpriteRenderer](tcspriterenderer.md)
  A renderer for drawing sprites using Metal.
### System visuals
- [class TCControlSystemVisualsProvider](tccontrolsystemvisualsprovider.md)
  Provides system-defined visuals for touch controls.
- [enum TCButtonVisualShape](tcbuttonvisualshape.md)
  Defines the visual shape of a button.
- [enum TCDirectionPadVisualStyle](tcdirectionpadvisualstyle.md)
  Defines the visual style of a direction pad.
- [enum TCDirectionPadVisualDirection](tcdirectionpadvisualdirection.md)
  Defines the direction of a direction pad visual.
### Collision
- [protocol TCCollider](tccollider.md)
  A protocol defining the collider properties for a control.
- [enum TCColliderType](tccollidertype.md)
  Defines the type of collider.
- [class TCRectCollider](tcrectcollider.md)
  A rectangular collider.
- [class TCCircleCollider](tccirclecollider.md)
  A circular collider.
- [class TCRegionCollider](tcregioncollider.md)
  A collider that covers a specific region of the touch controller.
- [enum TCRegionColliderRegion](tcregioncolliderregion.md)
  Defines the region of the touch controller that the `TCRegionCollider` represents.
### Classes
- [class TCButtonDescriptor](tcbuttondescriptor.md)
  A descriptor for configuring a button.
- [class TCControlLabel](tccontrollabel.md)
  A label you associate with a touch control and provides a semantic description.
- [class TCDirectionPadDescriptor](tcdirectionpaddescriptor.md)
  A descriptor for configuring a directional pad.
- [class TCThrottleDescriptor](tcthrottledescriptor.md)
  A descriptor for configuring a throttle.
- [class TCThumbstickDescriptor](tcthumbstickdescriptor.md)
  A descriptor for configuring a thumbstick.
- [class TCTouchControllerDescriptor](tctouchcontrollerdescriptor.md)
  A descriptor for configuring a touch controller.
- [class TCTouchpadDescriptor](tctouchpaddescriptor.md)
  A descriptor for configuring a touchpad.
### Protocols
- [protocol TCTransform](tctransform.md)
  A protocol defining the transform properties for a control.
### Enumerations
- [enum TCControlLabelType](tccontrollabeltype.md)
  Defines the type of control label.
- [enum TCThrottleOrientation](tcthrottleorientation.md)
  Defines the orientation of the throttle.
- [enum TCTransformAnchor](tctransformanchor.md)
  Defines the anchor point for a transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TouchControls)*