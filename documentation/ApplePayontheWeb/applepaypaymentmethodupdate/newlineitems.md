# newLineItems

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

An optional list of updated line items for the payment request that results from the user’s change to the payment method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
sequence <ApplePayLineItem> newLineItems;
```

## Discussion

Supply an updated list of line items if the user’s change in the payment method caused any changes in the line items.

## See Also

### Updating payment method properties
- [newTotal](./newtotal.md)
  The new total that results from the user’s change to the payment method.
- [errors](./errors.md)
  A list of customized errors you provide that results from the user’s change to the payment method.
- [newShippingMethods](./newshippingmethods.md)
  The updated list of available shipping methods that results from the user’s change to the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethodupdate/newlineitems)*