# init(paymentRequest:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithPaymentRequest:(PKPaymentRequest *) request;
```

## Return Value

The newly initialized view controller.

## Discussion

If the user can’t make payments on any of the payment request’s supported networks, initialization fails and this method returns `nil`.

Present and dismiss the controller by calling its [`present(completion:)`](./present%28completion%29.md) and [`dismiss(completion:)`](./dismiss%28completion%29.md) methods.

## Parameters

- `request`: The payment request to be authorized.

## See Also

### Creating a payment authorization controller
- [convenience init(disbursementRequest: PKDisbursementRequest)](./init%28disbursementrequest%29.md)
  Creates a new payment authorization controller with the disbursement request you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/init(paymentrequest:))*