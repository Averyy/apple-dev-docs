# highPriorityGesture(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Attaches a gesture to the view with a higher precedence than gestures defined by the view.

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
nonisolated
func highPriorityGesture<T>(_ gesture: T, isEnabled: Bool) -> some View where T : Gesture
```

#### Discussion

Use this method when you need to define a high priority gesture to take precedence over the view’s existing gestures. The example below defines a custom gesture that prints a message to the console and attaches it to the view’s [`VStack`](vstack.md). Inside the [`VStack`](vstack.md) a red heart [`Image`](image.md) defines its own [`TapGesture`](tapgesture.md) handler that also prints a message to the console, and a blue rectangle with no custom gesture handlers. Tapping or clicking any of the views results in a console message from the high priority gesture attached to the enclosing [`VStack`](vstack.md).

You can also use the `isEnabled` parameter to conditionally disable the gesture.

```swift
struct HighPriorityGestureExample: View {
    @State private var message = "Message"
    var isGestureEnabled: Bool
    let newGesture = TapGesture().onEnded {
        print("Tap on VStack.")
    }

    var body: some View {
        VStack(spacing:25) {
            Image(systemName: "heart.fill")
                .resizable()
                .frame(width: 75, height: 75)
                .padding()
                .foregroundColor(.red)
                .onTapGesture {
                    print("Tap on image.")
                }
            Rectangle()
                .fill(Color.blue)
        }
        .highPriorityGesture(
            newGesture, isEnabled: isGestureEnabled)
        .frame(width: 200, height: 200)
        .border(Color.purple)
    }
}
```

## Parameters

- `gesture`: A gesture to attach to the view.
- `isEnabled`: Whether the added gesture is enabled.

## See Also

- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](view/highprioritygesture(_:including:).md)
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
- [struct HandActivationBehavior](handactivationbehavior.md)
  An activation behavior specific to hand-driven input.
- [struct HandGestureShortcut](handgestureshortcut.md)
  Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/highprioritygesture(_:isenabled:))*