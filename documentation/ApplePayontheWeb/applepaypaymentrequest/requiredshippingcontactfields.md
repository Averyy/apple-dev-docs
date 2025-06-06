# requiredShippingContactFields

**Framework**: Apple Pay on the Web  
**Kind**: property

The fields of shipping information the user must provide to fulfill the order.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
sequence <ApplePayContactField> requiredShippingContactFields;
```

#### Discussion

Use `requiredShippingContactFields` to request the user’s address and other contact information that you require to fulfill the order.

You will receive the customer’s name when you request `postalAddress`. If you don’t need the customer’s address, you can request the `name` contact field directly.

The following listing is an example of requesting fields for a shipping contact:

```javascript
"requiredShippingContactFields": [
    "postalAddress",
    "name",
    "phoneticName",
    "phone",
    "email"
]
```

The source of the information may be the user’s “My card” in Contacts, Wallet settings, or may be entered into the payment sheet by the user, either directly or through Contacts.

## See Also

- [requiredBillingContactFields](applepaypaymentrequest/requiredbillingcontactfields.md)
  The fields of billing information the user must provide to process the transaction.
- [shippingContactEditingMode](applepaypaymentrequest/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
- [ApplePayContactField](applepaycontactfield.md)
  Field names for requesting contact information in a payment request.
- [ApplePayShippingContactEditingMode](applepayshippingcontacteditingmode.md)
  Values that indicate whether the shipping mode prevents the user from editing fields of the shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/requiredshippingcontactfields)*