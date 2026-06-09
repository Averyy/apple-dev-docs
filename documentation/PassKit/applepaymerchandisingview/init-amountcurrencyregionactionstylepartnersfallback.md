# init(amount:currency:region:action:style:partners:fallback:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Constructs a view displaying Pay Later Promotional information given a configuration

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
nonisolated
init(amount: Decimal, currency: Locale.Currency, region: Locale.Region, action: ApplePayMerchandisingAction = .learnMore, style: ApplePayMerchandisingStyle = .standard, partners: ApplePayMerchandisingPartnerConfiguration = .all, @ViewBuilder fallback: () -> Fallback = { EmptyView() })
```

## Parameters

- `amount`: The users bag price or item pricing
- `currency`: The ISO 4217 code for the country or region of the merchant’s principle place of business.
- `region`: The merchant’s ISO 3166 country code.
- `action`: The type of action that is taken when the user taps on the call to action in the view
- `style`: The style of view that should be shown. This dictates the strings / image content
- `partners`: List of partners the view should show if they are supported.
- `fallback`: The fallback view will be shown when the contents cannot rendered


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/applepaymerchandisingview/init(amount:currency:region:action:style:partners:fallback:))*