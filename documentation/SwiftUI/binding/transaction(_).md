# transaction(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Specifies a transaction for the binding.

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
func transaction(_ transaction: Transaction) -> Binding<Value>
```

## Return Value

A new binding.

## Parameters

- `transaction`: An instance of a [`Transaction`](../transaction.md).

## See Also

### Managing changes
- [var id: Value.ID](./id.md)
  The stable identity of the entity associated with this instance, corresponding to the `id` of the binding’s wrapped value.
- [func animation(Animation?) -> Binding<Value>](./animation%28_%29.md)
  Specifies an animation to perform when the binding value changes.
- [var transaction: Transaction](./transaction.md)
  The binding’s transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/transaction(_:))*