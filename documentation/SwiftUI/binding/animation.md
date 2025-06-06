# animation(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies an animation to perform when the binding value changes.

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
func animation(_ animation: Animation? = .default) -> Binding<Value>
```

#### Return Value

A new binding.

## Parameters

- `animation`: An animation sequence performed when the binding   value changes.

## See Also

- [var id: Value.ID](binding/id.md)
  The stable identity of the entity associated with this instance, corresponding to the `id` of the binding’s wrapped value.
- [func transaction(Transaction) -> Binding<Value>](binding/transaction(_:).md)
  Specifies a transaction for the binding.
- [var transaction: Transaction](binding/transaction.md)
  The binding’s transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/animation(_:))*