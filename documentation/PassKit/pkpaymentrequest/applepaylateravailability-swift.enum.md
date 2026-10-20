# PKPaymentRequest.ApplePayLaterAvailability

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Values you use to enable or disable Apple Pay Later for a specific transaction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS
- watchOS

## Declaration

```swift
enum ApplePayLaterAvailability
```

## Topics

### Availability
- [case unavailable(PKPaymentRequest.ApplePayLaterAvailability.Reason)](./applepaylateravailability-swift.enum/unavailable%28_%29.md)
  Apple Pay Later is not available.
- [PKPaymentRequest.ApplePayLaterAvailability.available](./applepaylateravailability-swift.enum/available.md)
  Apple Pay Later is available.
### Transaction availability reasons
- [PKPaymentRequest.ApplePayLaterAvailability.Reason](./applepaylateravailability-swift.enum/reason.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.

## See Also

### Deprecated
- [var applePayLaterAvailability: PKPaymentRequest.ApplePayLaterAvailability](./applepaylateravailability-3dxrt.md)
  A value that indicates whether Apple Pay Later is available for a transaction.
- [struct PKAddressField](../pkaddressfield.md)
  Billing or shipping address fields.
- [enum PKApplePayLaterAvailability](../pkapplepaylateravailability.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/applepaylateravailability-swift.enum)*