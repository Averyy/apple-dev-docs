# billingContact

**Framework**: Applepayontheweb  
**Kind**: property

The customer’s billing contact information.

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

- [shippingContact](applepayrequest/shippingcontact.md)
  The customer’s shipping contact information.
- [shippingContactEditingMode](applepayrequest/shippingcontacteditingmode.md)
  A value that indicates if the shipping mode prevents the user editing the shipping address.
- [ApplePayPaymentContact](applepaypaymentcontact.md)
  Contact information fields to use for billing and shipping contact information.
- [ApplePayShippingContactEditingMode](applepayshippingcontacteditingmode.md)
  Values that indicate whether the shipping mode prevents the user from editing fields of the shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayontheWeb/applepayrequest/billingcontact)*