# merchantName

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The merchant’s display name that the Apple Pay server associates with the payment token.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var merchantName: String { get set }
```

#### Discussion

Provide the name of the merchant associated with the payment token, to display to the user.

## See Also

- [var merchantIdentifier: String](pkpaymenttokencontext/merchantidentifier.md)
  The Apply Pay merchant identifier.
- [var merchantDomain: String?](pkpaymenttokencontext/merchantdomain.md)
  The merchant’s top-level domain that the Apple Pay server associates with the payment token.
- [var externalIdentifier: String](pkpaymenttokencontext/externalidentifier.md)
  An external identifier for the merchant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttokencontext/merchantname)*