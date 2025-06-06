# Value

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The type representing the gesture’s value.

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
associatedtype Value
```

## See Also

- [func updating<State>(GestureState<State>, body: (Self.Value, inout State, inout Transaction) -> Void) -> GestureStateGesture<Self, State>](gesture/updating(_:body:).md)
  Updates the provided gesture state property as the gesture’s value changes.
- [func onChanged((Self.Value) -> Void) -> _ChangedGesture<Self>](gesture/onchanged(_:).md)
  Adds an action to perform when the gesture’s value changes.
- [func onEnded((Self.Value) -> Void) -> _EndedGesture<Self>](gesture/onended(_:).md)
  Adds an action to perform when the gesture ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesture/value)*