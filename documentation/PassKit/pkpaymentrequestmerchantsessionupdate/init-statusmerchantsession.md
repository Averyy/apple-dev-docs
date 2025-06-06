# init(status:merchantSession:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a payment method update with the specified status and merchant session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(status: PKPaymentAuthorizationStatus, merchantSession session: PKPaymentMerchantSession?)
```

## Parameters

- `status`: The current authorization status for the payment.
- `session`: An object that validates the identity of a merchant for a payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestmerchantsessionupdate/init(status:merchantsession:))*