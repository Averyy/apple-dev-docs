# ImagePlaygroundViewController.Delegate

**Framework**: Image Playground  
**Kind**: protocol

An interface you use to receive images and handle events related to an image-generation view controller.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@objc
(ImageGenerationViewControllerDelegate) protocol Delegate : NSObjectProtocol
```

#### Overview

Adopt the [`ImagePlaygroundViewController.Delegate`](imageplaygroundviewcontroller/delegate-swift.protocol.md) protocol in a custom type and assign that type as the delegate of an [`ImagePlaygroundViewController`](imageplaygroundviewcontroller.md) object. When you present the view controller, the system interface handles interactions with the person and reports the results back to your delegate object.

## Topics

### Receiving the image
- [func imagePlaygroundViewController(ImagePlaygroundViewController, didCreateImageAt: URL)](imageplaygroundviewcontroller/delegate-swift.protocol/imageplaygroundviewcontroller(_:didcreateimageat:).md)
  Returns the generated image to the delegate.
### Handling cancellation events
- [func imagePlaygroundViewControllerDidCancel(ImagePlaygroundViewController)](imageplaygroundviewcontroller/delegate-swift.protocol/imageplaygroundviewcontrollerdidcancel(_:).md)
  Notifies the delegate that the person canceled the generation of the image.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any ImagePlaygroundViewController.Delegate)?](imageplaygroundviewcontroller/delegate-swift.property.md)
  The delegate object that receives the generated image and handles events from the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/delegate-swift.protocol)*