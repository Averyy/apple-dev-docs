# merchantDomain

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The merchant’s top-level domain that the Apple Pay server associates with the payment token.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var merchantDomain: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * merchantDomain;
```

## Discussion

This value is optional; provide the top-level domain for the merchant if it’s available.

## See Also

### Specifying the merchant
- [var merchantIdentifier: String](./merchantidentifier.md)
  The Apply Pay merchant identifier.
- [var merchantName: String](./merchantname.md)
  The merchant’s display name that the Apple Pay server associates with the payment token.
- [var externalIdentifier: String](./externalidentifier.md)
  An external identifier for the merchant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttokencontext/merchantdomain)*