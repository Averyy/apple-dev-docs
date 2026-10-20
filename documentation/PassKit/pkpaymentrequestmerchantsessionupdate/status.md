# status

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The current authorization status for the payment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var status: PKPaymentAuthorizationStatus { get set }
```

```objc
@property (nonatomic, assign) PKPaymentAuthorizationStatus status;
```

## See Also

### Getting information for the merchant session update
- [var session: PKPaymentMerchantSession?](./session.md)
  An object that validates the identity of a merchant for the payment request.
- [class PKPaymentMerchantSession](../pkpaymentmerchantsession.md)
  An object that validates the identity of a merchant for a payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestmerchantsessionupdate/status)*