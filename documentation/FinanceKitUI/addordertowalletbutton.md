# AddOrderToWalletButton

**Framework**: FinanceKitUI  
**Kind**: struct  
**Role**: Structure

A button you use to add an order to a person’s Apple Wallet.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
@MainActor
@preconcurrency struct AddOrderToWalletButton
```

## Topics

### Initializers
- [init(signedArchive: Data, onCompletion: (Result<FinanceStore.SaveOrderResult, any Error>) -> Void)](./addordertowalletbutton/init%28signedarchive,oncompletion%29.md)
  Returns an initialized Add to Order Button.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Related Documentation
- [struct AddOrderToWalletButtonStyle](./addordertowalletbuttonstyle.md)
  Values that determine the style of an Add Order to Apple Wallet button.
### Adding an order to Apple Wallet
- [struct AddOrderToWalletButtonStyle](./addordertowalletbuttonstyle.md)
  Values that determine the style of an Add Order to Apple Wallet button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton)*