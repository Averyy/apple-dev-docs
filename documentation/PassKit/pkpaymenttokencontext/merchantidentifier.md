# merchantIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The Apply Pay merchant identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var merchantIdentifier: String { get set }
```

```objc
@property (nonatomic, copy) NSString * merchantIdentifier;
```

## Discussion

The merchant identifier you provide when you make an Apple Pay payment request. If you request a payment token for another merchant, use their merchant identifier if available. Otherwise, use your own merchant identifier.

For more information about merchant identifiers, see [Setting up Apple Pay](../setting-up-apple-pay.md).

## See Also

### Specifying the merchant
- [var merchantDomain: String?](./merchantdomain.md)
  The merchant’s top-level domain that the Apple Pay server associates with the payment token.
- [var merchantName: String](./merchantname.md)
  The merchant’s display name that the Apple Pay server associates with the payment token.
- [var externalIdentifier: String](./externalidentifier.md)
  An external identifier for the merchant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttokencontext/merchantidentifier)*