# displayName

**Framework**: Apple Pay on the Web  
**Kind**: property

A string, suitable for display, that describes the card.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString displayName;
```

#### Discussion

The display name enables a user to recognize a particular card from a list of cards.

For debit and credit cards, the display name often includes the card brand and the last four digits of the credit card number when available, for example: `“Visa 1233”`, `“MasterCard 5678”`, `“AmEx 9876”`. For Apple Pay Cash cards, the display name is `“Apple Pay Cash”`. However, there is no guarantee about the display name’s content or format.

To protect the user’s privacy, Apple Pay sets the display name only after the user authorizes the purchase.

## See Also

- [network](applepaypaymentmethod/network.md)
  A string, suitable for display, that is the name of the payment network backing the card.
- [type](applepaypaymentmethod/type.md)
  A string value representing the card’s type of payment.
- [paymentPass](applepaypaymentmethod/paymentpass.md)
  The payment pass object currently selected to complete the payment.
- [billingContact](applepaypaymentmethod/billingcontact.md)
  The billing contact associated with the card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethod/displayname)*