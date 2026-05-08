# transaction

**Framework**: SwiftUI  
**Kind**: property

The binding’s transaction.

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
var transaction: Transaction
```

#### Discussion

The transaction captures the information needed to update the view when the binding value changes.

## See Also

- [var id: Value.ID](binding/id.md)
  The stable identity of the entity associated with this instance, corresponding to the `id` of the binding’s wrapped value.
- [func animation(Animation?) -> Binding<Value>](binding/animation(_:).md)
  Specifies an animation to perform when the binding value changes.
- [func transaction(Transaction) -> Binding<Value>](binding/transaction(_:).md)
  Specifies a transaction for the binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/transaction)*