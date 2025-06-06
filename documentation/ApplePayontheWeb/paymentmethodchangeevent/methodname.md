# methodName

**Framework**: Apple Pay on the Web  
**Kind**: property

The identifier for the payment method to use for the transaction.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
readonly attribute DOMString methodName;
```

#### Discussion

The [`methodName`](paymentmethodchangeevent/methodname.md) for Apple Pay transactions is the Apple Pay URL.

For more information, see [`W3C payment method identifiers (PMIs)`](https://developer.apple.comhttps://www.w3.org/TR/payment-method-id/#dfn-pmi).

## See Also

- [methodDetails](paymentmethodchangeevent/methoddetails.md)
  A dictionary that contains the details of the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/paymentmethodchangeevent/methodname)*