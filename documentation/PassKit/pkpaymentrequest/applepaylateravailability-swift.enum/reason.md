# PKPaymentRequest.ApplePayLaterAvailability.Reason

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Values you use to enable or disable Apple Pay Later for a specific transaction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum Reason
```

## Topics

### Reasons
- [PKPaymentRequest.ApplePayLaterAvailability.Reason.itemIneligible](pkpaymentrequest/applepaylateravailability-swift.enum/reason/itemineligible.md)
  Apple Pay Later is unavailable because one or more ineligible or prohibited items are in the shopping cart, such as gift cards.
- [PKPaymentRequest.ApplePayLaterAvailability.Reason.recurringTransaction](pkpaymentrequest/applepaylateravailability-swift.enum/reason/recurringtransaction.md)
  Apple Pay Later is unavailable because there’s a recurring payment or subscription in the shopping cart.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/applepaylateravailability-swift.enum/reason)*