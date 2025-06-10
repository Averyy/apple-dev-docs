# billingContact

**Framework**: Apple Pay on the Web  
**Kind**: property

A prepopulated billing address.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayPaymentContact billingContact;
```

#### Discussion

If you have an up-to-date billing address for the customer on file, you can set it here. This billing address appears in the payment sheet. The user can either use the address you specify or select a different address.

> **Note**:  If you supply a billing address, you must also request `“postalAddress”` in [`requiredBillingContactFields`](applepaypaymentrequest/requiredbillingcontactfields.md).

## See Also

- [shippingContact](applepayrequestbase/shippingcontact.md)
  The customer’s address, used for sending products or services for to the person.
- [shippingContactEditingMode](applepayrequestbase/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequestbase/billingcontact)*