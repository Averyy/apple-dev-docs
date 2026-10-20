# ApplePayMerchandisingView

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency struct ApplePayMerchandisingView<Fallback> where Fallback : View
```

## Topics

### Initializers
- [init(amount: Decimal, currency: Locale.Currency, region: Locale.Region, action: ApplePayMerchandisingAction, style: ApplePayMerchandisingStyle, partners: ApplePayMerchandisingPartnerConfiguration, fallback: () -> Fallback)](./applepaymerchandisingview/init%28amount,currency,region,action,style,partners,fallback%29.md)
  Constructs a view displaying Pay Later Promotional information given a configuration

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/applepaymerchandisingview)*