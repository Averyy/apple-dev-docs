# NSGestureRecognizerDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods for fine-tuning a gesture recognizer’s behavior.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSGestureRecognizerDelegate : NSObjectProtocol
```

#### Overview

Use the methods in this protocol to establish dynamic dependencies between gesture recognizers and to prevent a single gesture recognizer from acting at all.

## Topics

### Regulating Gesture Recognition
- [func gestureRecognizer(NSGestureRecognizer, shouldAttemptToRecognizeWith: NSEvent) -> Bool](nsgesturerecognizerdelegate/gesturerecognizer(_:shouldattempttorecognizewith:).md)
  Asks the delegate if a gesture recognizer should attempt to recognize gestures for a particular event.
- [func gestureRecognizerShouldBegin(NSGestureRecognizer) -> Bool](nsgesturerecognizerdelegate/gesturerecognizershouldbegin(_:).md)
  Asks the delegate if a gesture recognizer should transition out of the Possible (`NSGestureRecognizerStatePossible`) state.
### Controlling Simultaneous Gesture Recognition
- [func gestureRecognizer(NSGestureRecognizer, shouldRecognizeSimultaneouslyWith: NSGestureRecognizer) -> Bool](nsgesturerecognizerdelegate/gesturerecognizer(_:shouldrecognizesimultaneouslywith:).md)
  Asks the delegate if two gesture recognizers should be allowed to recognize their gestures simultaneously.
### Setting Up Failure Requirements
- [func gestureRecognizer(NSGestureRecognizer, shouldRequireFailureOf: NSGestureRecognizer) -> Bool](nsgesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:).md)
  Asks the delegate if the current gesture recognizer must wait to recognize its gesture until the specified gesture recognizer fails.
- [func gestureRecognizer(NSGestureRecognizer, shouldBeRequiredToFailBy: NSGestureRecognizer) -> Bool](nsgesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:).md)
  Asks the delegate if the current gesture recognizer must fail before another gesture recognizer is allowed to recognize its gesture.
### Instance Methods
- [func gestureRecognizer(NSGestureRecognizer, shouldReceive: NSTouch) -> Bool](nsgesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:).md)
  Called, for a new touch, before the system calls the `touchesBegan:withEvent:` method on the gesture recognizer. Return `NO` to prevent the gesture recognizer from seeing this touch.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSGestureRecognizer](nsgesturerecognizer.md)
  An object that monitors events and calls its action method when a predefined sequence of events occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate)*