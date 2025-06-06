# localizedDescription

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A short description of the card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var localizedDescription: String? { get set }
```

#### Discussion

This property provides a user-visible description that clearly identifies the card.

## See Also

- [var cardholderName: String?](pkaddpaymentpassrequestconfiguration/cardholdername.md)
  The name of the person as shown on the card.
- [var encryptionScheme: PKEncryptionScheme](pkaddpaymentpassrequestconfiguration/encryptionscheme.md)
  The encryption scheme to be used in this request.
- [struct PKEncryptionScheme](pkencryptionscheme.md)
  Encryption schemes.
- [var primaryAccountSuffix: String?](pkaddpaymentpassrequestconfiguration/primaryaccountsuffix.md)
  The last four or five digits of the card’s number.
- [var cardDetails: [PKLabeledValue]](pkaddpaymentpassrequestconfiguration/carddetails.md)
  An array of labeled values that describe a card.
- [class PKLabeledValue](pklabeledvalue.md)
  An object that can represent a detail about a payment card or other item.
- [var productIdentifiers: Set<String>](pkaddpaymentpassrequestconfiguration/productidentifiers.md)
- [var style: PKAddPaymentPassStyle](pkaddpaymentpassrequestconfiguration/style.md)
  A value that indicates whether a pass is for access or for payment use.
- [enum PKAddPaymentPassStyle](pkaddpaymentpassstyle.md)
  The type of payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/localizeddescription)*