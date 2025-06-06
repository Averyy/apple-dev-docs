# init(_:onRequest:onCompletion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(_ configuration: PKAddPaymentPassRequestConfiguration, onRequest: @escaping (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: @escaping (Result<PKSecureElementPass, any Error>) -> Void)
```

## See Also

- [init(PKEncryptionScheme, cardholderName: String, passStyle: PKAddPaymentPassStyle, primaryAccountSuffix: String?, cardDetails: [PKLabeledValue]?, description: String?, filters: [AddPassToWalletButtonFilter], onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void)](addpasstowalletbutton/init(_:cardholdername:passstyle:primaryaccountsuffix:carddetails:description:filters:onrequest:oncompletion:).md)
- [init(PKEncryptionScheme, cardholderName: String, passStyle: PKAddPaymentPassStyle, primaryAccountSuffix: String?, cardDetails: [PKLabeledValue]?, description: String?, filters: [AddPassToWalletButtonFilter], onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void, fallback: () -> Fallback)](addpasstowalletbutton/init(_:cardholdername:passstyle:primaryaccountsuffix:carddetails:description:filters:onrequest:oncompletion:fallback:).md)
- [init([PKPass], onCompletion: (Bool) -> Void)](addpasstowalletbutton/init(_:oncompletion:)-1inhj.md)
- [init(PKAddSecureElementPassConfiguration, onCompletion: (Result<[PKSecureElementPass], any Error>) -> Void)](addpasstowalletbutton/init(_:oncompletion:)-5wkyi.md)
- [init([PKPass], onCompletion: (Bool) -> Void, fallback: () -> Fallback)](addpasstowalletbutton/init(_:oncompletion:fallback:)-77t5g.md)
- [init(PKAddSecureElementPassConfiguration, onCompletion: (Result<[PKSecureElementPass], any Error>) -> Void, fallback: () -> Fallback)](addpasstowalletbutton/init(_:oncompletion:fallback:)-7adn5.md)
- [init(PKAddPaymentPassRequestConfiguration, onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void, fallback: () -> Fallback)](addpasstowalletbutton/init(_:onrequest:oncompletion:fallback:).md)
- [init(PKEncryptionScheme, primaryAccountSuffix: String, passStyle: PKAddPaymentPassStyle, cardDetails: [PKLabeledValue]?, description: String?, filters: [AddPassToWalletButtonFilter], onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void)](addpasstowalletbutton/init(_:primaryaccountsuffix:passstyle:carddetails:description:filters:onrequest:oncompletion:).md)
- [init(PKEncryptionScheme, primaryAccountSuffix: String, passStyle: PKAddPaymentPassStyle, cardDetails: [PKLabeledValue]?, description: String?, filters: [AddPassToWalletButtonFilter], onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void, fallback: () -> Fallback)](addpasstowalletbutton/init(_:primaryaccountsuffix:passstyle:carddetails:description:filters:onrequest:oncompletion:fallback:).md)
- [init(action: () -> Void)](addpasstowalletbutton/init(action:).md)
- [init(carKeyPassword: String, supportedRadioTechnologies: PKRadioTechnology, issuerIdentifier: String, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void)](addpasstowalletbutton/init(carkeypassword:supportedradiotechnologies:issueridentifier:oncompletion:).md)
- [init(carKeyPassword: String, supportedRadioTechnologies: PKRadioTechnology, issuerIdentifier: String, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void, fallback: () -> Fallback)](addpasstowalletbutton/init(carkeypassword:supportedradiotechnologies:issueridentifier:oncompletion:fallback:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/addpasstowalletbutton/init(_:onrequest:oncompletion:))*