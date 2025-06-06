# orderTypeIdentifier

**Framework**: Apple Pay on the Web  
**Kind**: property

An identifier for the order type associated with the order.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required DOMString orderTypeIdentifier;
```

#### Discussion

This value must correspond with your signing certificate and isn’t displayed to the customer.

## See Also

- [authenticationToken](applepaypaymentorderdetails/authenticationtoken.md)
  The authentication token supplied to your web service.
- [orderIdentifier](applepaypaymentorderdetails/orderidentifier.md)
  A unique order identifier scoped to your order type identifier.
- [webServiceURL](applepaypaymentorderdetails/webserviceurl.md)
  The URL of your web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentorderdetails/ordertypeidentifier)*