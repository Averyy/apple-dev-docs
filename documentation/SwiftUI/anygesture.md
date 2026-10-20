# AnyGesture

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A type-erased gesture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
nonisolated struct AnyGesture<Value>
```

## Topics

### Implementing a custom gesture
- [init<T>(T)](./anygesture/init%28_%29.md)
  Creates an instance from another gesture.

## Relationships

### Conforms To
- [Gesture](./gesture.md)

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
- [struct HandActivationBehavior](./handactivationbehavior.md)
  An activation behavior specific to hand-driven input.
- [struct HandGestureShortcut](./handgestureshortcut.md)
  Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anygesture)*