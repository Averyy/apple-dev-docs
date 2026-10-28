# paymentNetwork

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The payment network.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+

## Declaration

```swift
var paymentNetwork: PKPaymentNetwork? { get set }
```

```objc
@property (nonatomic, copy, nullable) PKPaymentNetwork paymentNetwork;
```

## Discussion

This property determines which cards are shown in the [`PKAddPaymentPassViewController`](../pkaddpaymentpassviewcontroller.md) class’s intro screen. The property defaults to `nil`, and the [`PKAddPaymentPassViewController`](../pkaddpaymentpassviewcontroller.md) shows all the networks for the card’s region. To specify a single network, assign a constant to the property. See Payment Networks in [`PKPaymentRequest`](../pkpaymentrequest.md).

## See Also

### Filtering pass libraries
- [var primaryAccountIdentifier: String?](./primaryaccountidentifier.md)
  A primary account identifier, used to filter out pass libraries.
- [var requiresFelicaSecureElement: Bool](./requiresfelicasecureelement.md)
  A Boolean value that indicates whether the payment pass requires the Felica Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/paymentnetwork)*