# TransactionPicker

**Framework**: FinanceKitUI  
**Kind**: struct

A view that displays a transaction picker for choosing transactions from FinanceKit.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency struct TransactionPicker<Label> where Label : View
```

## Topics

### Initializers
- [init(selection: Binding<[Transaction]>, label: () -> Label)](transactionpicker/init(selection:label:).md)
  Creates a picker that selects a collection of transactions.
### Instance Properties
- [var body: some View](transactionpicker/body-swift.property.md)
  The content and behavior of the view.
### Type Aliases
- [TransactionPicker.Body](transactionpicker/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](transactionpicker/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker)*