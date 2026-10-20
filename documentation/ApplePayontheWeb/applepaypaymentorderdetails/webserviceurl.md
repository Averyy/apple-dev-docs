# webServiceURL

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

The URL of your web service.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
required DOMString webServiceURL;
```

#### Discussion

The URL for your web service needs to begin with `https://`; for example, `https://example.com`.

## See Also

### Providing order information
- [authenticationToken](./authenticationtoken.md)
  The authentication token supplied to your web service.
- [orderIdentifier](./orderidentifier.md)
  A unique order identifier scoped to your order type identifier.
- [orderTypeIdentifier](./ordertypeidentifier.md)
  An identifier for the order type associated with the order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentorderdetails/webserviceurl)*