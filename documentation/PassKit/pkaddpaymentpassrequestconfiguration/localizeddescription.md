# localizedDescription

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A short description of the card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+

## Declaration

```swift
var localizedDescription: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * localizedDescription;
```

## Discussion

This property provides a user-visible description that clearly identifies the card.

## See Also

### Payment pass request properties
- [var cardholderName: String?](./cardholdername.md)
  The name of the person as shown on the card.
- [var encryptionScheme: PKEncryptionScheme](./encryptionscheme.md)
  The encryption scheme to be used in this request.
- [struct PKEncryptionScheme](../pkencryptionscheme.md)
  Encryption schemes.
- [var primaryAccountSuffix: String?](./primaryaccountsuffix.md)
  The last four or five digits of the card’s number.
- [var cardDetails: [PKLabeledValue]](./carddetails.md)
  An array of labeled values that describe a card.
- [class PKLabeledValue](../pklabeledvalue.md)
  An object that can represent a detail about a payment card or other item.
- [var productIdentifiers: Set<String>](./productidentifiers.md)
- [var style: PKAddPaymentPassStyle](./style.md)
  A value that indicates whether a pass is for access or for payment use.
- [enum PKAddPaymentPassStyle](../pkaddpaymentpassstyle.md)
  The type of payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/localizeddescription)*