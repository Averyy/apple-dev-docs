# TransactionKey

**Framework**: SwiftUI  
**Kind**: protocol

A key for accessing values in a transaction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol TransactionKey
```

#### Overview

You can create custom transaction values by extending the [`Transaction`](transaction.md) structure with new properties. First declare a new transaction key type and specify a value for the required [`defaultValue`](transactionkey/defaultvalue.md) property:

```swift
private struct MyTransactionKey: TransactionKey {
    static let defaultValue = false
}
```

The Swift compiler automatically infers the associated [`Value`](transactionkey/value.md) type as the type you specify for the default value. Then use the key to define a new transaction value property:

```swift
extension Transaction {
    var myCustomValue: Bool {
        get { self[MyTransactionKey.self] }
        set { self[MyTransactionKey.self] = newValue }
    }
}
```

Clients of your transaction value never use the key directly. Instead, they use the key path of your custom transaction value property. To set the transaction value for a change, wrap that change in a call to `withTransaction`:

```swift
withTransaction(\.myCustomValue, true) {
    isActive.toggle()
}
```

To use the value from inside `MyView` or one of its descendants, use the [`transaction(_:)`](view/transaction(_:).md) view modifier:

```swift
MyView()
    .transaction { transaction in
        if transaction.myCustomValue {
            transaction.animation = .default.repeatCount(3)
        }
    }
```

## Topics

### Setting a default value
- [static var defaultValue: Self.Value](transactionkey/defaultvalue.md)
  The default value for the transaction key.
- [associatedtype Value](transactionkey/value.md)
  The associated type representing the type of the transaction key’s value.

## See Also

- [func withTransaction<Result>(Transaction, () throws -> Result) rethrows -> Result](withtransaction(_:_:).md)
  Executes a closure with the specified transaction and returns the result.
- [func withTransaction<R, V>(WritableKeyPath<Transaction, V>, V, () throws -> R) rethrows -> R](withtransaction(_:_:_:).md)
  Executes a closure with the specified transaction key path and value and returns the result.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transactionkey)*