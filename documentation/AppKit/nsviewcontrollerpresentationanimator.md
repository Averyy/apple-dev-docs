# NSViewControllerPresentationAnimator

**Framework**: AppKit  
**Kind**: protocol

A set of methods that let you define animations to play when transitioning between two view controllers.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSViewControllerPresentationAnimator : NSObjectProtocol
```

#### Overview

Implement this protocol only if you want to provide custom animations. You might find what you need in the [`NSViewController.TransitionOptions`](nsviewcontroller/transitionoptions.md) enumeration, which provides many predefined animations.

A class that adopts this protocol is responsible for both presenting and dismissing a view controller.

## Topics

### Animating Presentation and Dismissal of View Controllers
- [func animatePresentation(of: NSViewController, from: NSViewController)](nsviewcontrollerpresentationanimator/animatepresentation(of:from:).md)
  Called when the specified view controller is about to be presented.
- [func animateDismissal(of: NSViewController, from: NSViewController)](nsviewcontrollerpresentationanimator/animatedismissal(of:from:).md)
  Called when a previously-presented view controller is about to be dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontrollerpresentationanimator)*