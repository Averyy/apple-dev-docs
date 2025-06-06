# shippingContact

**Framework**: Apple Pay on the Web  
**Kind**: property

Shipping contact information for the user.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayPaymentContact shippingContact;
```

#### Discussion

If you have an up-to-date shipping address on file, you can set it here. See [`ApplePayPaymentContact`](applepaypaymentcontact.md) for the fields in [`shippingContact`](applepaypaymentrequest/shippingcontact.md).

The information you provide in [`shippingContact`](applepaypaymentrequest/shippingcontact.md) is displayed in the payment sheet as the default shipping address. The user can either keep the address you provided or select another address.

Provide your user’s shipping contact info only if you are requiring shipping contact information.

## See Also

- [billingContact](applepaypaymentrequest/billingcontact.md)
  Billing contact information for the user.
- [ApplePayPaymentContact](applepaypaymentcontact.md)
  Contact information fields to use for billing and shipping contact information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/shippingcontact)*