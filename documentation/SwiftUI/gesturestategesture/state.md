# state

**Framework**: SwiftUI  
**Kind**: property

A value that changes as the user performs the gesture.

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
var state: GestureState<State>
```

## See Also

- [init(base: Base, state: GestureState<State>, body: (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void)](gesturestategesture/init(base:state:body:).md)
  Creates a new gesture that’s the result of an ongoing gesture.
- [var base: Base](gesturestategesture/base.md)
  The originating gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturestategesture/state)*