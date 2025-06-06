# errors

**Framework**: Apple Pay on the Web  
**Kind**: property

A list of custom errors to display on the payment sheet.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
sequence <ApplePayError> errors;
```

#### Discussion

List the errors on the payment sheet for the user to remedy. If there are multiple errors, list the most important error first.

For information on errors, see [`ApplePayError`](applepayerror.md).

## See Also

- [newLineItems](applepayshippingcontactupdate/newlineitems.md)
  An optional list of updated line items.
- [newShippingMethods](applepayshippingcontactupdate/newshippingmethods.md)
  A list of shipping methods that are available to the updated shipping contact.
- [newTotal](applepayshippingcontactupdate/newtotal.md)
  The new total that results from a change in the shipping contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingcontactupdate/errors)*