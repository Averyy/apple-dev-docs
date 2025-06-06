# init(base:state:body:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new gesture that’s the result of an ongoing gesture.

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
init(base: Base, state: GestureState<State>, body: @escaping (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void)
```

## Parameters

- `base`: The originating gesture.
- `state`: The wrapped value of a   property.
- `body`: The callback that SwiftUI invokes as the gesture’s value   changes.

## See Also

- [var base: Base](gesturestategesture/base.md)
  The originating gesture.
- [var state: GestureState<State>](gesturestategesture/state.md)
  A value that changes as the user performs the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturestategesture/init(base:state:body:))*