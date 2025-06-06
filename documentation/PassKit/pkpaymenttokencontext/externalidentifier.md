# externalIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An external identifier for the merchant.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var externalIdentifier: String { get set }
```

#### Discussion

An external identifier for the merchant that the app developer provides. If you request a payment token for another merchant, always use the same external identifier for that merchant in your app.

## See Also

- [var merchantIdentifier: String](pkpaymenttokencontext/merchantidentifier.md)
  The Apply Pay merchant identifier.
- [var merchantDomain: String?](pkpaymenttokencontext/merchantdomain.md)
  The merchant’s top-level domain that the Apple Pay server associates with the payment token.
- [var merchantName: String](pkpaymenttokencontext/merchantname.md)
  The merchant’s display name that the Apple Pay server associates with the payment token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttokencontext/externalidentifier)*