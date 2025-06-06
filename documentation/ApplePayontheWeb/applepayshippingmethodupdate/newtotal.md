# newTotal

**Framework**: Apple Pay on the Web  
**Kind**: property

The new total that results from a change in the shipping method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required ApplePayLineItem newTotal;
```

#### Discussion

Recalculate the total for the payment, because it may change as a result of shipping method changes. The [`newTotal`](applepayshippingcontactupdate/newtotal.md) value is required.

## See Also

- [newLineItems](applepayshippingmethodupdate/newlineitems.md)
  An optional list of updated line items.
- [newShippingMethods](applepayshippingmethodupdate/newshippingmethods.md)
  An updated list of new shipping methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingmethodupdate/newtotal)*