# onChanged(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when the gesture’s value changes.

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
@preconcurrency func onChanged(_ action: @escaping (Self.Value) -> Void) -> _ChangedGesture<Self>
```

## Mentions

- [Adding interactivity with gestures](adding-interactivity-with-gestures.md)

#### Return Value

A gesture that triggers `action` when this gesture’s value changes.

## Parameters

- `action`: The action to perform when this gesture’s value   changes. The   closure’s parameter contains the gesture’s new   value.

## See Also

- [func updating<State>(GestureState<State>, body: (Self.Value, inout State, inout Transaction) -> Void) -> GestureStateGesture<Self, State>](gesture/updating(_:body:).md)
  Updates the provided gesture state property as the gesture’s value changes.
- [func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>](gesture/onended(_:).md)
  Adds an action to perform when the gesture ends.
- [associatedtype Value](gesture/value.md)
  The type representing the gesture’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/onchanged(_:))*