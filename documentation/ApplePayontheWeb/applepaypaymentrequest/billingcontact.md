# billingContact

**Framework**: Apple Pay on the Web  
**Kind**: property

Billing contact information for the user.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayPaymentContact billingContact;
```

#### Discussion

If you have an up-to-date billing address on file, you can set it here. This billing address appears in the payment sheet. The user can either use the address you specify or select a different address.

> **Note**:  If you supply a billing address, you must also request “`postalAddress`” in [`requiredBillingContactFields`](applepaypaymentrequest/requiredbillingcontactfields.md).

 If you supply a billing address, you must also request “`postalAddress`” in [`requiredBillingContactFields`](applepaypaymentrequest/requiredbillingcontactfields.md).

## See Also

- [shippingContact](applepaypaymentrequest/shippingcontact.md)
  Shipping contact information for the user.
- [ApplePayPaymentContact](applepaypaymentcontact.md)
  Contact information fields to use for billing and shipping contact information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/billingcontact)*