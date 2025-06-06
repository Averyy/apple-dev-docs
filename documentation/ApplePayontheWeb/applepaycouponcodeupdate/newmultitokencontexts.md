# newMultiTokenContexts

**Framework**: Apple Pay on the Web  
**Kind**: property

An array of updated multitoken contexts for a multimerchant payment request.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
sequence <ApplePayPaymentTokenContext> newMultiTokenContexts;
```

#### Discussion

Provide this object to update the [`multiTokenContexts`](applepaypaymentrequest/multitokencontexts.md) value in the original [`ApplePayPaymentRequest`](applepaypaymentrequest.md), if necessary, after the user updated the coupon code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaycouponcodeupdate/newmultitokencontexts)*