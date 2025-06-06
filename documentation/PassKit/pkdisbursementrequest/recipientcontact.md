# recipientContact

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A contact object that describes the recipient.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var recipientContact: PKContact? { get set }
```

#### Discussion

If the merchant already has recipient contact information on file, set it here. Merchants should also include the corresponding contact fields in their [`requiredRecipientContactFields`](pkdisbursementrequest/requiredrecipientcontactfields.md) to ensure the data is visible on the payment sheet. Doing so enables people to select alternative contact information on the payment sheet, which merchants need to anticipate when they receive the final Apple Pay payment data.

## See Also

- [var requiredRecipientContactFields: [PKContactField]](pkdisbursementrequest/requiredrecipientcontactfields.md)
  An array that indicates which of the recipient’s contact details the merchant requires in order to process a disbursement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/recipientcontact)*