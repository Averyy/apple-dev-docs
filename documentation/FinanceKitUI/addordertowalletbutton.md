# AddOrderToWalletButton

**Framework**: FinanceKitUI  
**Kind**: struct

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
- [init(signedArchive: Data, onCompletion: (Result<FinanceStore.SaveOrderResult, any Error>) -> Void)](addordertowalletbutton/init(signedarchive:oncompletion:).md)
  Returns an initialized Add to Order Button.
### Instance Properties
- [var body: some View](addordertowalletbutton/body-swift.property.md)
  The content and behavior of the view.
### Type Aliases
- [AddOrderToWalletButton.Body](addordertowalletbutton/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](addordertowalletbutton/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct AddOrderToWalletButtonStyle](addordertowalletbuttonstyle.md)
  Values that determine the style of an Add Order to Apple Wallet button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton)*