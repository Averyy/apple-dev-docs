# externalIdentifier

**Framework**: Apple Pay on the Web  
**Kind**: property

An external identifier for the merchant.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required DOMString externalIdentifier;
```

#### Discussion

An external identifier for the merchant that the developer provides. If you request a payment token for another merchant, always use the same external identifier for that merchant on your website.

## See Also

- [merchantIdentifier](applepaypaymenttokencontext/merchantidentifier.md)
  The Apply Pay merchant identifier.
- [merchantName](applepaypaymenttokencontext/merchantname.md)
  The merchant’s display name that the Apple Pay server associates with the payment token.
- [merchantDomain](applepaypaymenttokencontext/merchantdomain.md)
  The merchant’s top-level domain that the Apple Pay server associates with the payment token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymenttokencontext/externalidentifier)*