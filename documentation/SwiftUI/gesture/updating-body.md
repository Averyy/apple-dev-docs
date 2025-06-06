# updating(_:body:)

**Framework**: SwiftUI  
**Kind**: method

Updates the provided gesture state property as the gesture’s value changes.

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
@MainActor
@preconcurrency func updating<State>(_ state: GestureState<State>, body: @escaping (Self.Value, inout State, inout Transaction) -> Void) -> GestureStateGesture<Self, State>
```

## Mentions

- [Adding interactivity with gestures](adding-interactivity-with-gestures.md)

#### Return Value

A version of the gesture that updates the provided `state` as the originating gesture’s value changes and that resets the `state` to its initial value when the user or the system ends or cancels the gesture.

#### Discussion

Use this callback to update transient UI state as described in [`Adding interactivity with gestures`](adding-interactivity-with-gestures.md).

## Parameters

- `state`: A binding to a view’s   property.
- `body`: The callback that SwiftUI invokes as the gesture’s value   changes. Its   parameter is the updated state of the   gesture. The   parameter is the previous state of the   gesture, and the   is the context of the gesture.

## See Also

- [func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>](gesture/onchanged(_:).md)
  Adds an action to perform when the gesture’s value changes.
- [func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>](gesture/onended(_:).md)
  Adds an action to perform when the gesture ends.
- [associatedtype Value](gesture/value.md)
  The type representing the gesture’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/updating(_:body:))*