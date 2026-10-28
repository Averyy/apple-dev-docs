# ImagePlaygroundViewController.Delegate

**Framework**: Image Playground  
**Kind**: protocol  
**Role**: Protocol

An interface you use to receive images and handle events related to an image-generation view controller.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.4+

## Declaration

```swift
@objc(ImageGenerationViewControllerDelegate)
protocol Delegate : NSObjectProtocol
```

## Overview

Adopt the [`ImagePlaygroundViewController.Delegate`](./delegate-swift.protocol.md) protocol in a custom type and assign that type as the delegate of an [`ImagePlaygroundViewController`](../imageplaygroundviewcontroller.md) object. When you present the view controller, the system interface handles interactions with the person and reports the results back to your delegate object.

## Topics

### Receiving the image
- [func imagePlaygroundViewController(ImagePlaygroundViewController, didCreateImageAt: URL)](./delegate-swift.protocol/imageplaygroundviewcontroller%28_,didcreateimageat%29.md)
  Returns the generated image to the delegate.
### Handling cancellation events
- [func imagePlaygroundViewControllerDidCancel(ImagePlaygroundViewController)](./delegate-swift.protocol/imageplaygroundviewcontrollerdidcancel%28_%29.md)
  Notifies the delegate that the person canceled the generation of the image.
### Instance Methods
- [func imagePlaygroundViewController(ImagePlaygroundViewController, didCreate: NSAdaptiveImageGlyph)](./delegate-swift.protocol/imageplaygroundviewcontroller%28_,didcreate%29.md)
  Returns the generated genmoji to the delegate.

## Relationships

### Inherits From
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Processing a generated image
- [var delegate: (any ImagePlaygroundViewController.Delegate)?](./delegate-swift.property.md)
  The delegate object that receives the generated image and handles events from the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/delegate-swift.protocol)*