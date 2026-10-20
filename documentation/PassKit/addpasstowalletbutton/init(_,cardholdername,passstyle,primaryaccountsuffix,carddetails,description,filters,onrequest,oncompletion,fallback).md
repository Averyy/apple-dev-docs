# init(_:cardholderName:passStyle:primaryAccountSuffix:cardDetails:description:filters:onRequest:onCompletion:fallback:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
nonisolated
init(_ encryptionScheme: PKEncryptionScheme, cardholderName: String, passStyle: PKAddPaymentPassStyle = .payment, primaryAccountSuffix: String? = nil, cardDetails: [PKLabeledValue]? = nil, description: String? = nil, filters: [AddPassToWalletButtonFilter] = [], onRequest: @escaping (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: @escaping (Result<PKSecureElementPass, any Error>) -> Void, @ViewBuilder fallback: () -> Fallback)
```

Available when `Fallback` conforms to `View`.

## See Also

### Creating the button
- [init(PKEncryptionScheme, cardholderName: String, passStyle: PKAddPaymentPassStyle, primaryAccountSuffix: String?, cardDetails: [PKLabeledValue]?, description: String?, filters: [AddPassToWalletButtonFilter], onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void)](./init%28_,cardholdername,passstyle,primaryaccountsuffix,carddetails,description,filters,onrequest,oncompletion%29.md)
- [init([PKPass], onCompletion: (Bool) -> Void)](./init%28_,oncompletion%29-1inhj.md)
- [init(PKAddSecureElementPassConfiguration, onCompletion: (Result<[PKSecureElementPass], any Error>) -> Void)](./init%28_,oncompletion%29-5wkyi.md)
- [init([PKPass], onCompletion: (Bool) -> Void, fallback: () -> Fallback)](./init%28_,oncompletion,fallback%29-77t5g.md)
- [init(PKAddSecureElementPassConfiguration, onCompletion: (Result<[PKSecureElementPass], any Error>) -> Void, fallback: () -> Fallback)](./init%28_,oncompletion,fallback%29-7adn5.md)
- [init(PKAddPaymentPassRequestConfiguration, onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void)](./init%28_,onrequest,oncompletion%29.md)
- [init(PKAddPaymentPassRequestConfiguration, onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void, fallback: () -> Fallback)](./init%28_,onrequest,oncompletion,fallback%29.md)
- [init(PKEncryptionScheme, primaryAccountSuffix: String, passStyle: PKAddPaymentPassStyle, cardDetails: [PKLabeledValue]?, description: String?, filters: [AddPassToWalletButtonFilter], onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void)](./init%28_,primaryaccountsuffix,passstyle,carddetails,description,filters,onrequest,oncompletion%29.md)
- [init(PKEncryptionScheme, primaryAccountSuffix: String, passStyle: PKAddPaymentPassStyle, cardDetails: [PKLabeledValue]?, description: String?, filters: [AddPassToWalletButtonFilter], onRequest: (AddPassToWalletButtonResponse) async -> PKAddPaymentPassRequest, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void, fallback: () -> Fallback)](./init%28_,primaryaccountsuffix,passstyle,carddetails,description,filters,onrequest,oncompletion,fallback%29.md)
- [init(action: () -> Void)](./init%28action%29.md)
- [init(carKeyPassword: String, supportedRadioTechnologies: PKRadioTechnology, issuerIdentifier: String, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void)](./init%28carkeypassword,supportedradiotechnologies,issueridentifier,oncompletion%29.md)
- [init(carKeyPassword: String, supportedRadioTechnologies: PKRadioTechnology, issuerIdentifier: String, onCompletion: (Result<PKSecureElementPass, any Error>) -> Void, fallback: () -> Fallback)](./init%28carkeypassword,supportedradiotechnologies,issueridentifier,oncompletion,fallback%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/addpasstowalletbutton/init(_:cardholdername:passstyle:primaryaccountsuffix:carddetails:description:filters:onrequest:oncompletion:fallback:))*