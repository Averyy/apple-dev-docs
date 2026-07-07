# TCControlContents

**Framework**: Touch Controller  
**Kind**: class

Represents the visual contents of a touch control.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCControlContents
```

## Topics

### Creating control contents
- [convenience init(images: [TCControlImage])](tccontrolcontents/init(images:).md)
  Creates a new instance with the specified images.
### Getting the images
- [var images: [TCControlImage]](tccontrolcontents/images.md)
  The array of objects used to render the control.
### Accessing button contents
- [class func buttonContents(forSystemImageNamed: String, size: CGSize, shape: TCControlContents.ButtonShape, controller: TCTouchController) -> TCControlContents](tccontrolcontents/buttoncontents(forsystemimagenamed:size:shape:controller:).md)
  The button contents for the specified system image name, size, and shape.
- [TCControlContents.ButtonShape](tccontrolcontents/buttonshape.md)
  Defines the visual shape of a button.
### Accessing directional pad contents
- [class func directionPadContents(label: TCControlLabel, size: CGSize, style: TCControlContents.DpadElementStyle, direction: TCControlContents.DpadDirection, controller: TCTouchController) -> TCControlContents](tccontrolcontents/directionpadcontents(label:size:style:direction:controller:).md)
  The direction pad contents for the specified label, size, style, and direction.
- [TCControlContents.DpadDirection](tccontrolcontents/dpaddirection.md)
  Defines the direction of a direction pad visual.
- [TCControlContents.DpadElementStyle](tccontrolcontents/dpadelementstyle.md)
  Defines the visual style of the individual up/down/left/right elements of a direction pad.
### Accessing switch contents
- [class func switchedOnContents(forSystemImageNamed: String, size: CGSize, shape: TCControlContents.ButtonShape, controller: TCTouchController) -> TCControlContents](tccontrolcontents/switchedoncontents(forsystemimagenamed:size:shape:controller:).md)
  The switch contents for the specified system image name, size, and shape.
### Accessing throttle contents
- [class func throttleBackgroundContents(size: CGSize, controller: TCTouchController) -> TCControlContents](tccontrolcontents/throttlebackgroundcontents(size:controller:).md)
  The throttle background contents for the specified size.
- [class func throttleIndicatorContents(size: CGSize, controller: TCTouchController) -> TCControlContents](tccontrolcontents/throttleindicatorcontents(size:controller:).md)
  The throttle indicator contents for the specified size.
### Accessing thumbstick contents
- [class func thumbstickStickBackgroundContents(size: CGSize, controller: TCTouchController) -> TCControlContents](tccontrolcontents/thumbstickstickbackgroundcontents(size:controller:).md)
  The thumbstick background contents for the specified size.
- [class func thumbstickStickContents(size: CGSize, controller: TCTouchController) -> TCControlContents](tccontrolcontents/thumbstickstickcontents(size:controller:).md)
  The thumbstick stick contents for the specified size.

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

## See Also

- [class TCControlImage](tccontrolimage.md)
  Represents an image to be rendered using Metal.
- [protocol TCControlLayout](tccontrollayout.md)
  A protocol defining the controlLayout properties for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents)*