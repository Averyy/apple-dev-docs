# network

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

A string, suitable for display, that is the name of the payment network backing the card.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
DOMString network;
```

#### Discussion

The value is one of the supported networks specified in the [`supportedNetworks`](../applepaypaymentrequest/supportednetworks.md) property of the [`ApplePayPaymentRequest`](../applepaypaymentrequest.md).

## See Also

### Accessing payment method data
- [displayName](./displayname.md)
  A string, suitable for display, that describes the card.
- [type](./type.md)
  A string value representing the card’s type of payment.
- [paymentPass](./paymentpass.md)
  The payment pass object currently selected to complete the payment.
- [billingContact](./billingcontact.md)
  The billing contact associated with the card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethod/network)*