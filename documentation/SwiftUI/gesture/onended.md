# onEnded(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when the gesture ends.

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
func onEnded(_ action: @escaping (Self.Value) -> Void) -> _EndedGesture<Self>
```

## Mentions

- [Adding interactivity with gestures](adding-interactivity-with-gestures.md)

#### Return Value

A gesture that triggers `action` when the gesture ends.

#### Discussion

> ❗ **Important**: The action is only performed if the gesture ends successfully. Use a `@GestureState` property to track state that is reset regardless of how the gesture ends.

## Parameters

- `action`: The action to perform when this gesture ends. The    closure’s parameter contains the final value of the gesture.

## See Also

- [func updating<State>(GestureState<State>, body: (Self.Value, inout State, inout Transaction) -> Void) -> GestureStateGesture<Self, State>](gesture/updating(_:body:).md)
  Updates the provided gesture state property as the gesture’s value changes.
- [func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>](gesture/onchanged(_:).md)
  Adds an action to perform when the gesture’s value changes.
- [associatedtype Value](gesture/value.md)
  The type representing the gesture’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/onended(_:))*