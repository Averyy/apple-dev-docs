# defersSystemGestures(on:)

**Framework**: SwiftUI  
**Kind**: method

Sets the screen edge from which you want your gesture to take precedence over the system gesture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
nonisolated
func defersSystemGestures(on edges: Edge.Set) -> some View
```

#### Discussion

The following code defers the vertical screen edges system gestures of a given canvas.

```swift
struct DeferredView: View {
    var body: some View {
        Canvas()
            .defersSystemGestures(on: .vertical)
    }
}
```

## Parameters

- `edges`: A value that indicates the screen edge from which   you want your gesture to take precedence over the system gesture.

## See Also

- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](view/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](view/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View](view/handgestureshortcut(_:isenabled:).md)
  Assigns a hand gesture shortcut to the modified control.
- [protocol Gesture](gesture.md)
  An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [struct AnyGesture](anygesture.md)
  A type-erased gesture.
- [struct HandActivationBehavior](handactivationbehavior.md)
  An activation behavior specific to hand-driven input.
- [struct HandGestureShortcut](handgestureshortcut.md)
  Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/deferssystemgestures(on:))*