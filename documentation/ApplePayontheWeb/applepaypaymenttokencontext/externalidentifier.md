# externalIdentifier

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

An external identifier for the merchant.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
required DOMString externalIdentifier;
```

#### Discussion

An external identifier for the merchant that the developer provides. If you request a payment token for another merchant, always use the same external identifier for that merchant on your website.

## See Also

### Specifying the merchant
- [merchantIdentifier](./merchantidentifier.md)
  The Apply Pay merchant identifier.
- [merchantName](./merchantname.md)
  The merchant’s display name that the Apple Pay server associates with the payment token.
- [merchantDomain](./merchantdomain.md)
  The merchant’s top-level domain that the Apple Pay server associates with the payment token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymenttokencontext/externalidentifier)*