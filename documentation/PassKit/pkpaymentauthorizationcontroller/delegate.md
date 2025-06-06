# delegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The controller’s delegate.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
weak var delegate: (any PKPaymentAuthorizationControllerDelegate)? { get set }
```

#### Discussion

The delegate is called at various points in the interaction, such as when the user selects shipping or billing information and when the user authorizes the payment request.

## See Also

- [protocol PKPaymentAuthorizationControllerDelegate](pkpaymentauthorizationcontrollerdelegate.md)
  Methods that let you respond to user interactions with your payment authorization controller.
- [func present(completion: ((Bool) -> Void)?)](pkpaymentauthorizationcontroller/present(completion:).md)
  Presents the payment sheet modally over your app.
- [func dismiss(completion: (() -> Void)?)](pkpaymentauthorizationcontroller/dismiss(completion:).md)
  Dismisses the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/delegate)*