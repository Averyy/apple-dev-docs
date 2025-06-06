# billingContact

**Framework**: Applepayontheweb  
**Kind**: property

The billing contact selected by the user for this transaction.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayPaymentContact billingContact;
```

#### Discussion

The billing contact information is populated if it is requested in [`ApplePayPaymentRequest`](applepaypaymentrequest.md).

After the user authorizes the transaction with Touch ID, Face ID, or passcode, `billingContact` contains the complete billing contact data. See [`ApplePayPaymentContact`](applepaypaymentcontact.md) for the billing contact field values.

> **Note**:  Address information can come from a wide range of sources. Always validate the information before you use it.

## See Also

- [shippingContact](applepaypayment/shippingcontact.md)
  The shipping contact selected by the user for this transaction.
- [ApplePayPaymentContact](applepaypaymentcontact.md)
  Contact information fields to use for billing and shipping contact information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayontheWeb/applepaypayment/billingcontact)*