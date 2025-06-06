# productIdentifiers

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

**Availability**:
- iOS 12.3+
- iPadOS 12.3+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var productIdentifiers: Set<String> { get set }
```

## See Also

- [var cardholderName: String?](pkaddpaymentpassrequestconfiguration/cardholdername.md)
  The name of the person as shown on the card.
- [var encryptionScheme: PKEncryptionScheme](pkaddpaymentpassrequestconfiguration/encryptionscheme.md)
  The encryption scheme to be used in this request.
- [struct PKEncryptionScheme](pkencryptionscheme.md)
  Encryption schemes.
- [var localizedDescription: String?](pkaddpaymentpassrequestconfiguration/localizeddescription.md)
  A short description of the card.
- [var primaryAccountSuffix: String?](pkaddpaymentpassrequestconfiguration/primaryaccountsuffix.md)
  The last four or five digits of the card’s number.
- [var cardDetails: [PKLabeledValue]](pkaddpaymentpassrequestconfiguration/carddetails.md)
  An array of labeled values that describe a card.
- [class PKLabeledValue](pklabeledvalue.md)
  An object that can represent a detail about a payment card or other item.
- [var style: PKAddPaymentPassStyle](pkaddpaymentpassrequestconfiguration/style.md)
  A value that indicates whether a pass is for access or for payment use.
- [enum PKAddPaymentPassStyle](pkaddpaymentpassstyle.md)
  The type of payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/productidentifiers)*