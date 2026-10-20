# dismiss(completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Dismisses the payment sheet.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func dismiss() async
```

#### Discussion

Call this method when you receive the [`paymentAuthorizationControllerDidFinish(_:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(_:).md) delegate callback, or otherwise want to dismiss the payment sheet.

## Parameters

- `completion`: A block that is called after the sheet is dismissed.

## See Also

- [var delegate: (any PKPaymentAuthorizationControllerDelegate)?](pkpaymentauthorizationcontroller/delegate.md)
  The controller’s delegate.
- [protocol PKPaymentAuthorizationControllerDelegate](pkpaymentauthorizationcontrollerdelegate.md)
  Methods that let you respond to user interactions with your payment authorization controller.
- [func present(completion: ((Bool) -> Void)?)](pkpaymentauthorizationcontroller/present(completion:).md)
  Presents the payment sheet modally over your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/dismiss(completion:))*