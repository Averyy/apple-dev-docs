# newTotal

**Framework**: Apple Pay on the Web  
**Kind**: property

The new total that results from the user’s change to the payment method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required ApplePayLineItem newTotal;
```

#### Discussion

Calculate the total for the payment, as it may change after the user updated the payment method. This value is required.

## See Also

- [newLineItems](applepaypaymentmethodupdate/newlineitems.md)
  An optional list of updated line items for the payment request that results from the user’s change to the payment method.
- [errors](applepaypaymentmethodupdate/errors.md)
  A list of customized errors you provide that results from the user’s change to the payment method.
- [newShippingMethods](applepaypaymentmethodupdate/newshippingmethods.md)
  The updated list of available shipping methods that results from the user’s change to the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethodupdate/newtotal)*