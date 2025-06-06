# present(completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Presents the payment sheet modally over your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func present() async -> Bool
```

#### Discussion

You are responsible for dismissing the payment sheet.

## Parameters

- `completion`: A block that is called after the sheet is presented. This block is passed the following parameters:

## See Also

- [var delegate: (any PKPaymentAuthorizationControllerDelegate)?](pkpaymentauthorizationcontroller/delegate.md)
  The controller’s delegate.
- [protocol PKPaymentAuthorizationControllerDelegate](pkpaymentauthorizationcontrollerdelegate.md)
  Methods that let you respond to user interactions with your payment authorization controller.
- [func dismiss(completion: (() -> Void)?)](pkpaymentauthorizationcontroller/dismiss(completion:).md)
  Dismisses the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/present(completion:))*