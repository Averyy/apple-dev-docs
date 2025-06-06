# init(merchantIdentifier:externalIdentifier:merchantName:merchantDomain:amount:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Create a payment token context for a single merchant.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(merchantIdentifier: String, externalIdentifier: String, merchantName: String, merchantDomain: String?, amount: NSDecimalNumber)
```

## Parameters

- `merchantIdentifier`: The Apple Pay merchant identifier.
- `externalIdentifier`: An external identifier for the merchant.
- `merchantName`: The merchant’s display name that the Apple Pay server associates with the payment token.
- `merchantDomain`: The merchant’s top-level domain that the Apple Pay server associates with the payment token.
- `amount`: The amount to authorize for the payment token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttokencontext/init(merchantidentifier:externalidentifier:merchantname:merchantdomain:amount:))*