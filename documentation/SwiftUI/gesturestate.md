# GestureState

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper type that updates a property while the user performs a gesture and resets the property back to its initial state when the gesture ends.

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
@propertyWrapper
@frozen struct GestureState<Value>
```

## Mentions

- [Adding interactivity with gestures](adding-interactivity-with-gestures.md)

#### Overview

Declare a property as `@GestureState`, pass as a binding to it as a parameter to a gesture’s [`updating(_:body:)`](gesture/updating(_:body:).md) callback, and receive updates to it. A property that’s declared as `@GestureState` implicitly resets when the gesture becomes inactive, making it suitable for tracking transient state.

Add a long-press gesture to a [`Circle`](circle.md), and update the interface during the gesture by declaring a property as `@GestureState`:

```swift
struct SimpleLongPressGestureView: View {
    @GestureState private var isDetectingLongPress = false

    var longPress: some Gesture {
        LongPressGesture(minimumDuration: 3)
            .updating($isDetectingLongPress) { currentState, gestureState, transaction in
                gestureState = currentState
            }
    }

    var body: some View {
        Circle()
            .fill(self.isDetectingLongPress ? Color.red : Color.green)
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(longPress)
    }
}
```

## Topics

### Creating a gesture state
- [init(initialValue: Value)](gesturestate/init(initialvalue:).md)
  Creates a view state that’s derived from a gesture with an initial value.
- [init(initialValue: Value, reset: (Value, inout Transaction) -> Void)](gesturestate/init(initialvalue:reset:).md)
  Creates a view state that’s derived from a gesture with an initial state value and a closure that provides a transaction to reset it.
- [init(initialValue: Value, resetTransaction: Transaction)](gesturestate/init(initialvalue:resettransaction:).md)
  Creates a view state that’s derived from a gesture with an initial state value and a transaction to reset it.
- [init(reset: (Value, inout Transaction) -> Void)](gesturestate/init(reset:).md)
  Creates a view state that’s derived from a gesture with a closure that provides a transaction to reset it.
- [init(resetTransaction: Transaction)](gesturestate/init(resettransaction:).md)
  Creates a view state that’s derived from a gesture with a transaction to reset it.
- [init(wrappedValue: Value)](gesturestate/init(wrappedvalue:).md)
  Creates a view state that’s derived from a gesture.
- [init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)](gesturestate/init(wrappedvalue:reset:).md)
  Creates a view state that’s derived from a gesture with a wrapped state value and a closure that provides a transaction to reset it.
- [init(wrappedValue: Value, resetTransaction: Transaction)](gesturestate/init(wrappedvalue:resettransaction:).md)
  Creates a view state that’s derived from a gesture with a wrapped state value and a transaction to reset it.
### Getting the state
- [var wrappedValue: Value](gesturestate/wrappedvalue.md)
  The wrapped value referenced by the gesture state property.
- [var projectedValue: GestureState<Value>](gesturestate/projectedvalue.md)
  A binding to the gesture state property.

## Relationships

### Conforms To
- [DynamicProperty](dynamicproperty.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct GestureStateGesture](gesturestategesture.md)
  A gesture that updates the state provided by a gesture’s updating callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturestate)*