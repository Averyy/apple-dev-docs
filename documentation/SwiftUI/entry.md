# Entry()

**Framework**: SwiftUI  
**Kind**: macro

Creates an environment values, transaction, container values, or focused values entry.

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
@attached
(accessor) @attached(peer, names: prefixed(__Key_)) macro Entry()
```

#### Environment Values

Create [`EnvironmentValues`](environmentvalues.md) entries by extending the [`EnvironmentValues`](environmentvalues.md) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension EnvironmentValues {
    @Entry var myCustomValue: String = "Default value"
    @Entry var anotherCustomValue = true
}
```

#### Transaction Values

Create [`Transaction`](transaction.md) entries by extending the [`Transaction`](transaction.md) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension Transaction {
    @Entry var myCustomValue: String = "Default value"
}
```

#### Container Values

Create [`ContainerValues`](containervalues.md) entries by extending the [`ContainerValues`](containervalues.md) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension ContainerValues {
    @Entry var myCustomValue: String = "Default value"
}
```

#### Focused Values

Since the default value for [`FocusedValues`](focusedvalues.md) is always `nil`, [`FocusedValues`](focusedvalues.md) entries cannot specify a different default value and must have an Optional type.

Create [`FocusedValues`](focusedvalues.md) entries by extending the [`FocusedValues`](focusedvalues.md) structure with new properties and attaching the @Entry macro to the variable declarations:

```swift
extension FocusedValues {
    @Entry var myCustomValue: String?
}
```

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
- [protocol TransactionKey](transactionkey.md)
  A key for accessing values in a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/entry())*