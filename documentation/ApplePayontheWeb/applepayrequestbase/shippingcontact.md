# shippingContact

**Framework**: Apple Pay on the Web  
**Kind**: property

The customer’s address, used for sending products or services for to the person.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayPaymentContact shippingContact;
```

#### Discussion

If you have an up-to-date shipping address on file for the customer, you can set it here. See [`ApplePayPaymentContact`](applepaypaymentcontact.md) for the fields in [`shippingContact`](applepaypaymentrequest/shippingcontact.md).

The payment sheet displays the information you provide in [`shippingContact`](applepaypaymentrequest/shippingcontact.md) as the default shipping address. The user can either keep the address you provide or select another address.

Provide your user’s shipping contact info only if you request shipping information by setting `requestShipping` to `true` in your [`PaymentOptions`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentoptions-dictionary) dictionary.

## See Also

- [billingContact](applepayrequestbase/billingcontact.md)
  A prepopulated billing address.
- [shippingContactEditingMode](applepayrequestbase/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequestbase/shippingcontact)*