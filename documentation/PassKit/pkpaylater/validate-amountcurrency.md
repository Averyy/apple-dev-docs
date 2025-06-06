# validate(amount:currency:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Checks if the framework can display Apple Pay Later visual merchandising widget information for the given amount and currency.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS ?+

## Declaration

```swift
static func validate(amount: Decimal, currency: Locale.Currency) async -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the framework can display the requested information; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `amount`: The customer’s cart price or item pricing.
- `currency`: The   currency code for the country or region of the merchant’s principle place of business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylater/validate(amount:currency:))*