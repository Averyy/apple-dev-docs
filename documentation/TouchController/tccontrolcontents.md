# TCControlContents

**Framework**: Touch Controller  
**Kind**: class  
**Role**: Class

Represents the visual contents of a touch control.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class TCControlContents
```

```objc
@interface TCControlContents : NSObject
```

## Topics

### Creating control contents
- [convenience init(images: [TCControlImage])](./tccontrolcontents/init%28images%29.md)
  Creates a new instance with the specified images.
### Getting the images
- [var images: [TCControlImage]](./tccontrolcontents/images.md)
  The array of objects used to render the control.
### Accessing button contents
- [class func buttonContents(forSystemImageNamed: String, size: CGSize, shape: TCControlContents.ButtonShape, controller: TCTouchController) -> TCControlContents](./tccontrolcontents/buttoncontents%28forsystemimagenamed,size,shape,controller%29.md)
  The button contents for the specified system image name, size, and shape.
- [TCControlContents.ButtonShape](./tccontrolcontents/buttonshape.md)
  Defines the visual shape of a button.
### Accessing directional pad contents
- [class func directionPadContents(label: TCControlLabel, size: CGSize, style: TCControlContents.DpadElementStyle, direction: TCControlContents.DpadDirection, controller: TCTouchController) -> TCControlContents](./tccontrolcontents/directionpadcontents%28label,size,style,direction,controller%29.md)
  The direction pad contents for the specified label, size, style, and direction.
- [TCControlContents.DpadDirection](./tccontrolcontents/dpaddirection.md)
  Defines the direction of a direction pad visual.
- [TCControlContents.DpadElementStyle](./tccontrolcontents/dpadelementstyle.md)
  Defines the visual style of the individual up/down/left/right elements of a direction pad.
### Accessing switch contents
- [class func switchedOnContents(forSystemImageNamed: String, size: CGSize, shape: TCControlContents.ButtonShape, controller: TCTouchController) -> TCControlContents](./tccontrolcontents/switchedoncontents%28forsystemimagenamed,size,shape,controller%29.md)
  The switch contents for the specified system image name, size, and shape.
### Accessing throttle contents
- [class func throttleBackgroundContents(size: CGSize, controller: TCTouchController) -> TCControlContents](./tccontrolcontents/throttlebackgroundcontents%28size,controller%29.md)
  The throttle background contents for the specified size.
- [class func throttleIndicatorContents(size: CGSize, controller: TCTouchController) -> TCControlContents](./tccontrolcontents/throttleindicatorcontents%28size,controller%29.md)
  The throttle indicator contents for the specified size.
### Accessing thumbstick contents
- [class func thumbstickStickBackgroundContents(size: CGSize, controller: TCTouchController) -> TCControlContents](./tccontrolcontents/thumbstickstickbackgroundcontents%28size,controller%29.md)
  The thumbstick background contents for the specified size.
- [class func thumbstickStickContents(size: CGSize, controller: TCTouchController) -> TCControlContents](./tccontrolcontents/thumbstickstickcontents%28size,controller%29.md)
  The thumbstick stick contents for the specified size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Visuals
- [class TCControlImage](./tccontrolimage.md)
  Represents an image to be rendered using Metal.
- [protocol TCControlLayout](./tccontrollayout.md)
  A protocol defining the controlLayout properties for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents)*