# PKAddPaymentPassStyle

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

The type of payment pass.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
enum PKAddPaymentPassStyle
```

## Topics

### Payment pass styles
- [PKAddPaymentPassStyle.access](pkaddpaymentpassstyle/access.md)
  A pass that authorizes the user to access a location or resource.
- [PKAddPaymentPassStyle.payment](pkaddpaymentpassstyle/payment.md)
  A pass used by a customer for purchasing.
### Initializers
- [init?(rawValue: Int)](pkaddpaymentpassstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [var productIdentifiers: Set<String>](pkaddpaymentpassrequestconfiguration/productidentifiers.md)
- [var style: PKAddPaymentPassStyle](pkaddpaymentpassrequestconfiguration/style.md)
  A value that indicates whether a pass is for access or for payment use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassstyle)*