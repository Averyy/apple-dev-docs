# newLineItems

**Framework**: Apple Pay on the Web  
**Kind**: property

An optional list of updated line items.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
sequence <ApplePayLineItem> newLineItems;
```

#### Discussion

Supply an updated list of line items if the change in the shipping contact caused any changes in the line items.

## See Also

- [errors](applepayshippingcontactupdate/errors.md)
  A list of custom errors to display on the payment sheet.
- [newShippingMethods](applepayshippingcontactupdate/newshippingmethods.md)
  A list of shipping methods that are available to the updated shipping contact.
- [newTotal](applepayshippingcontactupdate/newtotal.md)
  The new total that results from a change in the shipping contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingcontactupdate/newlineitems)*