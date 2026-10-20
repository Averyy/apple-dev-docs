# init(paymentRequest:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Initializes and returns a payment authorization controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(paymentRequest request: PKPaymentRequest)
```

#### Return Value

The newly initialized view controller.

#### Discussion

If the user can’t make payments on any of the payment request’s supported networks, initialization fails and this method returns `nil`.

Present and dismiss the controller by calling its [`present(completion:)`](pkpaymentauthorizationcontroller/present(completion:).md) and [`dismiss(completion:)`](pkpaymentauthorizationcontroller/dismiss(completion:).md) methods.

## Parameters

- `request`: The payment request to be authorized.

## See Also

- [convenience init(disbursementRequest: PKDisbursementRequest)](pkpaymentauthorizationcontroller/init(disbursementrequest:).md)
  Creates a new payment authorization controller with the disbursement request you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/init(paymentrequest:))*