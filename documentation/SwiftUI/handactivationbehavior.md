# HandActivationBehavior

**Framework**: SwiftUI  
**Kind**: struct

An activation behavior specific to hand-driven input.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct HandActivationBehavior
```

#### Overview

Hand activation behavior determines what hand input modes activate a gesture.

## Topics

### Getting the behaviors
- [static let automatic: HandActivationBehavior](handactivationbehavior/automatic.md)
  The default activation behavior, including direct touch, direct pinch, and indirect pinch.
- [static let pinch: HandActivationBehavior](handactivationbehavior/pinch.md)
  Activation that requires a pinched hand.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](view/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](view/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](view/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [func defersSystemGestures(on: Edge.Set) -> some View](view/deferssystemgestures(on:).md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [protocol Gesture](gesture.md)
  An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [struct AnyGesture](anygesture.md)
  A type-erased gesture.
- [struct HandGestureShortcut](handgestureshortcut.md)
  Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/handactivationbehavior)*