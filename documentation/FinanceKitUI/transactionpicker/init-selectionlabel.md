# init(selection:label:)

**Framework**: FinanceKitUI  
**Kind**: init

Creates a picker that selects a collection of transactions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
@preconcurrency init(selection: Binding<[Transaction]>, @ViewBuilder label: () -> Label)
```

## Parameters

- `selection`: The selection of transactions from the transaction picker.
- `label`: The view that describes the action of choosing transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/init(selection:label:))*