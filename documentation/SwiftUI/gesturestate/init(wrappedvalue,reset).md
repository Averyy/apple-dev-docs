# init(wrappedValue:reset:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a view state that’s derived from a gesture with a wrapped state value and a closure that provides a transaction to reset it.

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
init(wrappedValue: Value, reset: @escaping (Value, inout Transaction) -> Void)
```

## Parameters

- `wrappedValue`: A wrapped value for the gesture state property.
- `reset`: A closure that provides a [`Transaction`](../transaction.md).

## See Also

### Creating a gesture state
- [init(initialValue: Value)](./init%28initialvalue%29.md)
  Creates a view state that’s derived from a gesture with an initial value.
- [init(initialValue: Value, reset: (Value, inout Transaction) -> Void)](./init%28initialvalue,reset%29.md)
  Creates a view state that’s derived from a gesture with an initial state value and a closure that provides a transaction to reset it.
- [init(initialValue: Value, resetTransaction: Transaction)](./init%28initialvalue,resettransaction%29.md)
  Creates a view state that’s derived from a gesture with an initial state value and a transaction to reset it.
- [init(reset: (Value, inout Transaction) -> Void)](./init%28reset%29.md)
  Creates a view state that’s derived from a gesture with a closure that provides a transaction to reset it.
- [init(resetTransaction: Transaction)](./init%28resettransaction%29.md)
  Creates a view state that’s derived from a gesture with a transaction to reset it.
- [init(wrappedValue: Value)](./init%28wrappedvalue%29.md)
  Creates a view state that’s derived from a gesture.
- [init(wrappedValue: Value, resetTransaction: Transaction)](./init%28wrappedvalue,resettransaction%29.md)
  Creates a view state that’s derived from a gesture with a wrapped state value and a transaction to reset it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturestate/init(wrappedvalue:reset:))*