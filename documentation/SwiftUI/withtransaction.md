# withTransaction(_:_:_:)

**Framework**: SwiftUI  
**Kind**: func

Executes a closure with the specified transaction key path and value and returns the result.

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
func withTransaction<R, V>(_ keyPath: WritableKeyPath<Transaction, V>, _ value: V, _ body: () throws -> R) rethrows -> R
```

#### Return Value

The result of executing the closure with the specified transaction value.

## Parameters

- `keyPath`: A key path that indicates the property of the    structure to update.
- `value`: The new value to set for the item specified by  .
- `body`: A closure to execute.

## See Also

- [func withTransaction<Result>(Transaction, () throws -> Result) rethrows -> Result](withtransaction(_:_:).md)
  Executes a closure with the specified transaction and returns the result.
- [func transaction((inout Transaction) -> Void) -> some View](view/transaction(_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction(value: some Equatable, (inout Transaction) -> Void) -> some View](view/transaction(value:_:).md)
  Applies the given transaction mutation function to all animations used within the view.
- [func transaction<V>((inout Transaction) -> Void, body: (PlaceholderContentView<Self>) -> V) -> some View](view/transaction(_:body:).md)
  Applies the given transaction mutation function to all animations used within the `body` closure.
- [struct Transaction](transaction.md)
  The context of the current state-processing update.
- [macro Entry()](entry().md)
  Creates an environment values, transaction, container values, or focused values entry.
- [protocol TransactionKey](transactionkey.md)
  A key for accessing values in a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/withtransaction(_:_:_:))*