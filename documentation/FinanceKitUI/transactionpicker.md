# TransactionPicker

**Framework**: FinanceKitUI  
**Kind**: struct  
**Role**: Structure

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
- [init(selection: Binding<[Transaction]>, label: () -> Label)](./transactionpicker/init%28selection,label%29.md)
  Creates a picker that selects a collection of transactions.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker)*