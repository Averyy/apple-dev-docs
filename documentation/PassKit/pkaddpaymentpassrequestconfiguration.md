# PKAddPaymentPassRequestConfiguration

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

Contains the configuration data for a view controller that lets the user add a payment pass.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class PKAddPaymentPassRequestConfiguration
```

#### Overview

The encryption scheme, cardholder name, and primary account suffix are required for configuration. The configuration information is used for setup and display only. It should not contain any sensitive information.

> ❗ **Important**:  Adding payment passes requires a special entitlement issued by Apple. Your app must include this entitlement before you can use this class. For more information on requesting this entitlement, see the Card Issuers section at [`developer.apple.com/apple-pay/`](https://developer.apple.comhttps://developer.apple.com/apple-pay/).

 Adding payment passes requires a special entitlement issued by Apple. Your app must include this entitlement before you can use this class. For more information on requesting this entitlement, see the Card Issuers section at [`developer.apple.com/apple-pay/`](https://developer.apple.comhttps://developer.apple.com/apple-pay/).

## Topics

### Creating a request configuration
- [init?(encryptionScheme: PKEncryptionScheme)](pkaddpaymentpassrequestconfiguration/init(encryptionscheme:).md)
  Instantiates a new request configuration with the given encryption scheme.
- [struct PKEncryptionScheme](pkencryptionscheme.md)
  Encryption schemes.
### Filtering pass libraries
- [var paymentNetwork: PKPaymentNetwork?](pkaddpaymentpassrequestconfiguration/paymentnetwork.md)
  The payment network.
- [var primaryAccountIdentifier: String?](pkaddpaymentpassrequestconfiguration/primaryaccountidentifier.md)
  A primary account identifier, used to filter out pass libraries.
- [var requiresFelicaSecureElement: Bool](pkaddpaymentpassrequestconfiguration/requiresfelicasecureelement.md)
  A Boolean value that indicates whether the payment pass requires the Felica Secure Element.
### Payment pass request properties
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
- [enum PKAddPaymentPassStyle](pkaddpaymentpassstyle.md)
  The type of payment pass.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init?(requestConfiguration: PKAddPaymentPassRequestConfiguration, delegate: (any PKAddPaymentPassViewControllerDelegate)?)](pkaddpaymentpassviewcontroller/init(requestconfiguration:delegate:).md)
  Returns an initialized add payment view controller object, using the provided configuration and delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration)*