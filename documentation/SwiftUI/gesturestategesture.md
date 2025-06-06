# GestureStateGesture

**Framework**: SwiftUI  
**Kind**: struct

A gesture that updates the state provided by a gesture’s updating callback.

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
@frozen
struct GestureStateGesture<Base, State> where Base : Gesture
```

#### Overview

A gesture’s [`updating(_:body:)`](gesture/updating(_:body:).md) callback returns a `GestureStateGesture` instance for updating a transient state property that’s annotated with the [`GestureState`](gesturestate.md) property wrapper.

## Topics

### Creating an in-progress gesture
- [init(base: Base, state: GestureState<State>, body: (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void)](gesturestategesture/init(base:state:body:).md)
  Creates a new gesture that’s the result of an ongoing gesture.
- [var base: Base](gesturestategesture/base.md)
  The originating gesture.
- [var state: GestureState<State>](gesturestategesture/state.md)
  A value that changes as the user performs the gesture.
### Supporting types
- [var body: (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void](gesturestategesture/body.md)
  The updating gesture containing the originating gesture’s value, the updated state of the gesture, and a transaction.

## Relationships

### Conforms To
- [Gesture](gesture.md)

## See Also

- [struct GestureState](gesturestate.md)
  A property wrapper type that updates a property while the user performs a gesture and resets the property back to its initial state when the gesture ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturestategesture)*