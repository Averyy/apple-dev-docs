# init(paymentRequest:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Initializes and returns a payment authorization view controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(paymentRequest request: PKPaymentRequest)
```

#### Return Value

The newly initialized view controller.

#### Discussion

If the user can’t make payments on any of the payment request’s supported networks, initialization fails and this method returns `nil`.

Present and dismiss the view controller using the appropriate mechanism and style for the current device idiom.

## Parameters

- `request`: The payment request to be authorized.

## See Also

- [convenience init(disbursementRequest: PKDisbursementRequest)](pkpaymentauthorizationviewcontroller/init(disbursementrequest:).md)
  Initializes and returns a new payment authorization view controller with the provided disbursement request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller/init(paymentrequest:))*