# requiresFelicaSecureElement

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates whether the payment pass requires the Felica Secure Element.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var requiresFelicaSecureElement: Bool { get set }
```

#### Discussion

This property can be used as a filter to determine which cards are shown in the [`PKAddPaymentPassViewController`](pkaddpaymentpassviewcontroller.md) class’s intro screen. The property defaults to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var paymentNetwork: PKPaymentNetwork?](pkaddpaymentpassrequestconfiguration/paymentnetwork.md)
  The payment network.
- [var primaryAccountIdentifier: String?](pkaddpaymentpassrequestconfiguration/primaryaccountidentifier.md)
  A primary account identifier, used to filter out pass libraries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/requiresfelicasecureelement)*