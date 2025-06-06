# newTotal

**Framework**: Apple Pay on the Web  
**Kind**: property

The new total that results from a change in the shipping contact.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required ApplePayLineItem newTotal;
```

#### Discussion

Recalculate the total for the payment, because it may change as a result of shipping contact changes.  The [`newTotal`](applepayshippingcontactupdate/newtotal.md) value is required.

## See Also

- [errors](applepayshippingcontactupdate/errors.md)
  A list of custom errors to display on the payment sheet.
- [newLineItems](applepayshippingcontactupdate/newlineitems.md)
  An optional list of updated line items.
- [newShippingMethods](applepayshippingcontactupdate/newshippingmethods.md)
  A list of shipping methods that are available to the updated shipping contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingcontactupdate/newtotal)*