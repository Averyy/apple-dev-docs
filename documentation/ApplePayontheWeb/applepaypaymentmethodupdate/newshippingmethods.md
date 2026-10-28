# newShippingMethods

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

The updated list of available shipping methods that results from the user’s change to the payment method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
sequence <ApplePayShippingMethod> newShippingMethods;
```

## Discussion

Supply an updated list of shipping methods if the user’s change in the payment method caused any changes in the shipping methods.

## See Also

### Updating payment method properties
- [newLineItems](./newlineitems.md)
  An optional list of updated line items for the payment request that results from the user’s change to the payment method.
- [newTotal](./newtotal.md)
  The new total that results from the user’s change to the payment method.
- [errors](./errors.md)
  A list of customized errors you provide that results from the user’s change to the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethodupdate/newshippingmethods)*