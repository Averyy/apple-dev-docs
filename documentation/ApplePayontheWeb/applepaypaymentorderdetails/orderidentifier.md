# orderIdentifier

**Framework**: Apple Pay on the Web  
**Kind**: property

A unique order identifier scoped to your order type identifier.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required DOMString orderIdentifier;
```

#### Discussion

In combination with the order type identifier, this uniquely identifies an order within the system. The framework doesn’t display this value to the customer.

## See Also

- [authenticationToken](applepaypaymentorderdetails/authenticationtoken.md)
  The authentication token supplied to your web service.
- [orderTypeIdentifier](applepaypaymentorderdetails/ordertypeidentifier.md)
  An identifier for the order type associated with the order.
- [webServiceURL](applepaypaymentorderdetails/webserviceurl.md)
  The URL of your web service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentorderdetails/orderidentifier)*