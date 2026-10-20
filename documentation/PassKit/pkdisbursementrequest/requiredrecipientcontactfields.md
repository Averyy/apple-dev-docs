# requiredRecipientContactFields

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An array that indicates which of the recipient’s contact details the merchant requires in order to process a disbursement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var requiredRecipientContactFields: [PKContactField] { get set }
```

```objc
@property (nonatomic, strong) NSArray<NSString *> * requiredRecipientContactFields;
```

#### Discussion

The framework uses these details to display the input fields for name, email address, phone number, and so on on the payment sheet. The framework always shows them in a specific order, regardless of the order of API input.

## See Also

### Requesting recipient contact fields
- [var recipientContact: PKContact?](./recipientcontact.md)
  A contact object that describes the recipient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/requiredrecipientcontactfields)*