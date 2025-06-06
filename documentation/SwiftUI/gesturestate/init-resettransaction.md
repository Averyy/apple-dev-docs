# init(resetTransaction:)

**Framework**: SwiftUI  
**Kind**: init

Creates a view state that’s derived from a gesture with a transaction to reset it.

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
init(resetTransaction: Transaction = Transaction())
```

## Parameters

- `resetTransaction`: A transaction that provides metadata for   view updates.

## See Also

- [init(initialValue: Value)](gesturestate/init(initialvalue:).md)
  Creates a view state that’s derived from a gesture with an initial value.
- [init(initialValue: Value, reset: (Value, inout Transaction) -> Void)](gesturestate/init(initialvalue:reset:).md)
  Creates a view state that’s derived from a gesture with an initial state value and a closure that provides a transaction to reset it.
- [init(initialValue: Value, resetTransaction: Transaction)](gesturestate/init(initialvalue:resettransaction:).md)
  Creates a view state that’s derived from a gesture with an initial state value and a transaction to reset it.
- [init(reset: (Value, inout Transaction) -> Void)](gesturestate/init(reset:).md)
  Creates a view state that’s derived from a gesture with a closure that provides a transaction to reset it.
- [init(wrappedValue: Value)](gesturestate/init(wrappedvalue:).md)
  Creates a view state that’s derived from a gesture.
- [init(wrappedValue: Value, reset: (Value, inout Transaction) -> Void)](gesturestate/init(wrappedvalue:reset:).md)
  Creates a view state that’s derived from a gesture with a wrapped state value and a closure that provides a transaction to reset it.
- [init(wrappedValue: Value, resetTransaction: Transaction)](gesturestate/init(wrappedvalue:resettransaction:).md)
  Creates a view state that’s derived from a gesture with a wrapped state value and a transaction to reset it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturestate/init(resettransaction:))*