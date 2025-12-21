# TransactionPicker

**Framework**: FinanceKitUI  
**Kind**: struct

A view that displays a transaction picker for choosing transactions from FinanceKit.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
@preconcurrency struct TransactionPicker<Label> where Label : View
```

## Topics

### Initializers
- [init(selection: Binding<[Transaction]>, label: () -> Label)](transactionpicker/init(selection:label:).md)
  Creates a picker that selects a collection of transactions.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker)*