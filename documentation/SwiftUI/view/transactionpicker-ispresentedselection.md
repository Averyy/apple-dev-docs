# transactionPicker(isPresented:selection:)

**Framework**: SwiftUI  
**Kind**: method

Presents a picker that selects a collection of transactions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func transactionPicker(isPresented: Binding<Bool>, selection: Binding<[Transaction]>) -> some View
```

## Parameters

- `isPresented`: The binding to whether the transaction picker should be shown.
- `selection`: The selection of transactions from the transaction picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/transactionpicker(ispresented:selection:))*