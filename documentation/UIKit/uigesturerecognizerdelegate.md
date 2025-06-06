# UIGestureRecognizerDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIGestureRecognizerDelegate : NSObjectProtocol
```

## Mentions

- [Preferring one gesture over another](preferring-one-gesture-over-another.md)

#### Overview

The delegates receive messages from a gesture recognizer, and their responses to these messages enable them to affect the operation of the gesture recognizer or to specify a relationship between it and another gesture recognizer, such as allowing simultaneous recognition or setting up a dynamic failure requirement.

An example of a situation where dynamic failure requirements are useful is in an app that attaches a screen-edge pan gesture recognizer to a view. In this case, you might want all other relevant gesture recognizers associated with that view’s subtree to require the screen-edge gesture recognizer to fail so you can prevent any graphical glitches that might occur when the other recognizers get canceled after starting the recognition process. To do this, you could use code similar to the following:

## Topics

### Regulating gesture recognition
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](uigesturerecognizerdelegate/gesturerecognizershouldbegin(_:).md)
  Asks the delegate if a gesture recognizer should begin interpreting touches.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UITouch) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-16fuh.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIPress) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-73vzu.md)
  Asks the delegate if a gesture recognizer should receive an object representing a press.
- [func gestureRecognizer(UIGestureRecognizer, shouldReceive: UIEvent) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-evxd.md)
  Asks the delegate if a gesture recognizer should receive an object representing a touch or press event.
### Controlling simultaneous gesture recognition
- [func gestureRecognizer(UIGestureRecognizer, shouldRecognizeSimultaneouslyWith: UIGestureRecognizer) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrecognizesimultaneouslywith:).md)
  Asks the delegate if two gesture recognizers should be allowed to recognize gestures simultaneously.
### Setting up failure requirements
- [func gestureRecognizer(UIGestureRecognizer, shouldRequireFailureOf: UIGestureRecognizer) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:).md)
  Asks the delegate if a gesture recognizer should require another gesture recognizer to fail.
- [func gestureRecognizer(UIGestureRecognizer, shouldBeRequiredToFailBy: UIGestureRecognizer) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:).md)
  Asks the delegate if a gesture recognizer should be required to fail by another gesture recognizer.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UITableViewCell](uitableviewcell.md)

## See Also

- [Implementing a custom gesture recognizer](implementing-a-custom-gesture-recognizer.md)
  Discover when and how to build your own gesture recognizers.
- [class UIGestureRecognizer](uigesturerecognizer.md)
  The base class for concrete gesture recognizers.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md)
  Enrich your app’s user experience by supporting standard and custom gesture interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate)*