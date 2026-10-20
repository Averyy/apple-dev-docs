# cardDetails

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An array of labeled values that describe a card.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+

## Declaration

```swift
var cardDetails: [PKLabeledValue] { get set }
```

```objc
@property (nonatomic, copy) NSArray<PKLabeledValue *> * cardDetails;
```

#### Discussion

This property provides user-visible descriptions that help to identify the card.

## See Also

### Payment pass request properties
- [var cardholderName: String?](./cardholdername.md)
  The name of the person as shown on the card.
- [var encryptionScheme: PKEncryptionScheme](./encryptionscheme.md)
  The encryption scheme to be used in this request.
- [struct PKEncryptionScheme](../pkencryptionscheme.md)
  Encryption schemes.
- [var localizedDescription: String?](./localizeddescription.md)
  A short description of the card.
- [var primaryAccountSuffix: String?](./primaryaccountsuffix.md)
  The last four or five digits of the card’s number.
- [class PKLabeledValue](../pklabeledvalue.md)
  An object that can represent a detail about a payment card or other item.
- [var productIdentifiers: Set<String>](./productidentifiers.md)
- [var style: PKAddPaymentPassStyle](./style.md)
  A value that indicates whether a pass is for access or for payment use.
- [enum PKAddPaymentPassStyle](../pkaddpaymentpassstyle.md)
  The type of payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/carddetails)*