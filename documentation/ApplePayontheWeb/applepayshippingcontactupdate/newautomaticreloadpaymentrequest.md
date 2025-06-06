# newAutomaticReloadPaymentRequest

**Framework**: Apple Pay on the Web  
**Kind**: property

An updated request for an automatic reload payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayAutomaticReloadPaymentRequest newAutomaticReloadPaymentRequest;
```

#### Discussion

Provide this object to update the [`automaticReloadPaymentRequest`](applepaypaymentrequest/automaticreloadpaymentrequest.md) value in the original [`ApplePayPaymentRequest`](applepaypaymentrequest.md), if necessary, after the user updated their shipping contact information.

## See Also

- [ApplePayAutomaticReloadPaymentRequest](applepayautomaticreloadpaymentrequest.md)
  A dictionary that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingcontactupdate/newautomaticreloadpaymentrequest)*