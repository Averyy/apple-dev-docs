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

## Mentions

- [Apple Pay on the Web Version 6 Release Notes](apple-pay-on-the-web-version-6-release-notes.md)

#### Discussion

Use [`requiredShippingContactFields`](applepayrequest/requiredshippingcontactfields.md) to request the user’s address and other contact information that you require to fulfill the order.

You receive the customer’s name when you request `postalAddress`. If you don’t need the customer’s address, you can request the name contact field directly.

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

The source of the information may be the user’s My Card in Contacts or in Wallet. The user can also enter the information into the payment sheet, either directly or through Contacts.

The [`requiredShippingContactFields`](applepayrequest/requiredshippingcontactfields.md) for [`ApplePayRequest`](applepayrequest.md) is available in Apple Pay version 6.

## See Also

- [requiredBillingContactFields](applepayrequest/requiredbillingcontactfields.md)
  The fields of billing information the user must provide to process the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequest/requiredshippingcontactfields)*