# thumbsticks

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

An array containing all the thumbstick controls managed by this controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var thumbsticks: [TCThumbstick] { get }
```

```objc
@property (nonatomic, readonly) NSArray<TCThumbstick *> * thumbsticks;
```

## See Also

### Inspecting the touch controller
- [var buttons: [TCButton]](./buttons.md)
  An array containing all the button controls managed by this controller.
- [var controls: [any TCControl]](./controls.md)
  An array containing all the touch controls managed by this controller.
- [var device: any MTLDevice](./device.md)
  The Metal device the touch control uses for rendering the touch controls.
- [var directionPads: [TCDirectionPad]](./directionpads.md)
  An array containing all the direction pad controls managed by this controller.
- [var drawableSize: CGSize](./drawablesize.md)
  The size of the drawable to which the touch controller’s contents be drawn, in native pixels.
- [var size: CGSize](./size.md)
  The size of the view the touch controller’s drawable is embedded in, in points.
- [var switches: [TCSwitch]](./switches.md)
  An array containing all the switch controls managed by this controller.
- [var isConnected: Bool](./isconnected.md)
  A Boolean value that indicates whether the touch controller is connected to the Game Controller framework.
- [class var isSupported: Bool](./issupported.md)
  Whether touch controllers are supported for the device.
- [var throttles: [TCThrottle]](./throttles.md)
  An array containing all the throttle controls managed by this controller.
- [var touchpads: [TCTouchpad]](./touchpads.md)
  An array containing all the touchpad controls managed by this controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/thumbsticks)*