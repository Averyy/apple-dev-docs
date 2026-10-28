# errors

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

A list of errors resulting from the coupon code update.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
sequence <ApplePayError> errors;
```

## Discussion

List the errors in order of importance.

For information on the possible errors, see [`ApplePayError`](../applepayerror.md).

## See Also

### Setting updated transaction details
- [newLineItems](./newlineitems.md)
  The list of updated line items incorporating the coupon code update.
- [newShippingMethods](./newshippingmethods.md)
  The list of available shipping methods.
- [newTotal](./newtotal.md)
  The updated total resulting from the coupon code update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaycouponcodeupdate/errors)*