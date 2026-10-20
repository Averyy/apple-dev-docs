# id

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The stable identity of the entity associated with this instance, corresponding to the `id` of the binding’s wrapped value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var id: Value.ID { get }
```

Available when `Value` conforms to `Identifiable`.

## See Also

### Managing changes
- [func animation(Animation?) -> Binding<Value>](./animation%28_%29.md)
  Specifies an animation to perform when the binding value changes.
- [func transaction(Transaction) -> Binding<Value>](./transaction%28_%29.md)
  Specifies a transaction for the binding.
- [var transaction: Transaction](./transaction.md)
  The binding’s transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/id)*