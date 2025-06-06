# handGestureShortcut(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Assigns a hand gesture shortcut to the modified control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func handGestureShortcut(_ shortcut: HandGestureShortcut, isEnabled: Bool = true) -> some View
```

#### Discussion

Performing the control’s shortcut while the control is anywhere in the frontmost scene is equivalent to direct interaction with the control to perform its primary action.

The following example lets users of a watchOS music app toggle playback by double-tapping their thumb and index finger together:

```swift
struct PlaybackControls: View {
    let model: TrackModel

    var body: some View {
        HStack {
            Button("Skip Back") {
                model.skipBack()
            }

            Button("Play/Pause") {
                model.playPause()
            }
            .handGestureShortcut(.primaryAction)

            Button("Skip Forward") {
                model.skipForward()
            }
        }
    }
}
```

The target of a hand gesture shortcut is resolved in a leading-to-trailing traversal of the active scene.

## Parameters

- `shortcut`: The shortcut to associate with this control.
- `isEnabled`: A Boolean value that indicates whether the shortcut is   is enabled for this control.

## See Also

- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](view/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, isEnabled: Bool) -> some View](view/highprioritygesture(_:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/highprioritygesture(_:name:isenabled:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/handgestureshortcut(_:isenabled:))*