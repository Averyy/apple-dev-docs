# HandGestureShortcut

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- watchOS 11.0+

## Declaration

```swift
struct HandGestureShortcut
```

## Topics

### Type Properties
- [static let primaryAction: HandGestureShortcut](./handgestureshortcut/primaryaction.md)
  The hand gesture shortcut for the primary action.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining custom gestures
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](./view/highprioritygesture%28_,including%29.md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](./view/highprioritygesture%28_,isenabled%29.md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](./view/highprioritygesture%28_,name,isenabled%29.md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](./view/handgestureshortcut%28_,isenabled%29.md)
  Assigns a hand gesture shortcut to the modified control.
- [func defersSystemGestures(on: Edge.Set) -> some View](./view/deferssystemgestures%28on%29.md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [protocol Gesture](./gesture.md)
  An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [struct AnyGesture](./anygesture.md)
  A type-erased gesture.
- [struct HandActivationBehavior](./handactivationbehavior.md)
  An activation behavior specific to hand-driven input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/handgestureshortcut)*