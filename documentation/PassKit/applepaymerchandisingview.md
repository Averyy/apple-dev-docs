# ApplePayMerchandisingView

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct ApplePayMerchandisingView<Fallback> where Fallback : View
```

## Topics

### Initializers
- [init(amount: Decimal, currency: Locale.Currency, region: Locale.Region, action: ApplePayMerchandisingAction, style: ApplePayMerchandisingStyle, partners: ApplePayMerchandisingPartnerConfiguration, fallback: () -> Fallback)](applepaymerchandisingview/init(amount:currency:region:action:style:partners:fallback:).md)
  Constructs a view displaying Pay Later Promotional information given a configuration

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/applepaymerchandisingview)*