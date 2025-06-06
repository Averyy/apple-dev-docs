# requiredBillingContactFields

**Framework**: Apple Pay on the Web  
**Kind**: property

The fields of billing information the user must provide to process the transaction.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
sequence <ApplePayContactField> requiredBillingContactFields;
```

#### Discussion

Use `requiredBillingContactFields` to request the user’s billing address that is associated with their payment method. The field you can request for a billing contact is shown in the following sample code:

```javascript
"requiredBillingContactFields": [
    "postalAddress"
]
```

You will receive the postal address as well as the user’s name after the user authorizes the transaction.

The source of the information may be the user’s Me contact card, the back of credit card in Wallet, or may be entered by the user directly into the payment sheet.

## See Also

- [requiredShippingContactFields](applepaypaymentrequest/requiredshippingcontactfields.md)
  The fields of shipping information the user must provide to fulfill the order.
- [shippingContactEditingMode](applepaypaymentrequest/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
- [ApplePayContactField](applepaycontactfield.md)
  Field names for requesting contact information in a payment request.
- [ApplePayShippingContactEditingMode](applepayshippingcontacteditingmode.md)
  Values that indicate whether the shipping mode prevents the user from editing fields of the shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/requiredbillingcontactfields)*