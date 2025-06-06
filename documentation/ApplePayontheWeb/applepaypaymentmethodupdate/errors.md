# errors

**Framework**: Apple Pay on the Web  
**Kind**: property

A list of customized errors you provide that results from the user’s change to the payment method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
sequence <ApplePayError> errors;
```

#### Discussion

List the errors in order of importance.

For information on the possible errors, see [`ApplePayError`](applepayerror.md).

## See Also

- [newLineItems](applepaypaymentmethodupdate/newlineitems.md)
  An optional list of updated line items for the payment request that results from the user’s change to the payment method.
- [newTotal](applepaypaymentmethodupdate/newtotal.md)
  The new total that results from the user’s change to the payment method.
- [newShippingMethods](applepaypaymentmethodupdate/newshippingmethods.md)
  The updated list of available shipping methods that results from the user’s change to the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethodupdate/errors)*