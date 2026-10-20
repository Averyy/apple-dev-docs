# base

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The originating gesture.

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
var base: Base
```

## See Also

### Creating an in-progress gesture
- [init(base: Base, state: GestureState<State>, body: (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void)](./init%28base,state,body%29.md)
  Creates a new gesture that’s the result of an ongoing gesture.
- [var state: GestureState<State>](./state.md)
  A value that changes as the user performs the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturestategesture/base)*