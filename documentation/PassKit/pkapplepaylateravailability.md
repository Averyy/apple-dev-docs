# PKApplePayLaterAvailability

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Values you use to enable or disable Apple Pay Later for a specific transaction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum PKApplePayLaterAvailability
```

```c
enum PKApplePayLaterAvailability : NSInteger;
```

## Topics

### Availability values
- [PKApplePayLaterAvailability.available](./pkapplepaylateravailability/available.md)
  Apple Pay Later is available.
- [PKApplePayLaterAvailability.unavailableItemIneligible](./pkapplepaylateravailability/unavailableitemineligible.md)
  Apple Pay Later is unavailable because one or more ineligible or prohibited items are in the shopping cart, such as gift cards.
- [PKApplePayLaterAvailability.unavailableRecurringTransaction](./pkapplepaylateravailability/unavailablerecurringtransaction.md)
  Apple Pay Later is unavailable because there’s a recurring payment or subscription in the shopping cart.
### Initializers
- [init?(rawValue: Int)](./pkapplepaylateravailability/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [var applePayLaterAvailability: PKPaymentRequest.ApplePayLaterAvailability](./pkpaymentrequest/applepaylateravailability-3dxrt.md)
  A value that indicates whether Apple Pay Later is available for a transaction.
- [PKPaymentRequest.ApplePayLaterAvailability](./pkpaymentrequest/applepaylateravailability-swift.enum.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.
- [struct PKAddressField](./pkaddressfield.md)
  Billing or shipping address fields.
- [applePayLaterAvailability](./pkpaymentrequest/applepaylateravailability-inpf.md)
  A value that indicates whether Apple Pay Later is available for a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkapplepaylateravailability)*