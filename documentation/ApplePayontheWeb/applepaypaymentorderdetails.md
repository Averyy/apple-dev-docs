# ApplePayPaymentOrderDetails

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that contains metadata related to an order.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayPaymentOrderDetails {
	required DOMString orderTypeIdentifier;
	required DOMString orderIdentifier;
	required DOMString webServiceURL;
	required DOMString authenticationToken;
};
```

## Topics

### Providing order information
- [authenticationToken](applepaypaymentorderdetails/authenticationtoken.md)
  The authentication token supplied to your web service.
- [orderIdentifier](applepaypaymentorderdetails/orderidentifier.md)
  A unique order identifier scoped to your order type identifier.
- [orderTypeIdentifier](applepaypaymentorderdetails/ordertypeidentifier.md)
  An identifier for the order type associated with the order.
- [webServiceURL](applepaypaymentorderdetails/webserviceurl.md)
  The URL of your web service.

## See Also

- [orderDetails](applepaypaymentauthorizationresult/orderdetails.md)
  Optional metadata for an order that the customer placed using this payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentorderdetails)*