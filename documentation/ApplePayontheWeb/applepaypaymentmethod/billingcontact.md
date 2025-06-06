# billingContact

**Framework**: Apple Pay on the Web  
**Kind**: property

The billing contact associated with the card.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayPaymentContact billingContact;
```

## Mentions

- [Apple Pay on the Web Version 10 Release Notes](apple-pay-on-the-web-version-10-release-notes.md)

#### Discussion

Before the user authorizes the transaction, you receive redacted billing contact information in a callback event. The redacted information includes only the necessary data for completing transaction tasks, such as calculating taxes or shipping costs.

## See Also

- [displayName](applepaypaymentmethod/displayname.md)
  A string, suitable for display, that describes the card.
- [network](applepaypaymentmethod/network.md)
  A string, suitable for display, that is the name of the payment network backing the card.
- [type](applepaypaymentmethod/type.md)
  A string value representing the card’s type of payment.
- [paymentPass](applepaypaymentmethod/paymentpass.md)
  The payment pass object currently selected to complete the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethod/billingcontact)*