# init(disbursementRequest:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Creates a new payment authorization controller with the disbursement request you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(disbursementRequest request: PKDisbursementRequest)
```

```objc
- (instancetype) initWithDisbursementRequest:(PKDisbursementRequest *) request;
```

## Parameters

- `request`: A [`PKDisbursementRequest`](../pkdisbursementrequest.md) that contains the details of the request.

## See Also

### Creating a payment authorization controller
- [init(paymentRequest: PKPaymentRequest)](./init%28paymentrequest%29.md)
  Initializes and returns a payment authorization controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/init(disbursementrequest:))*