# primaryAccountIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A primary account identifier, used to filter out pass libraries.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var primaryAccountIdentifier: String? { get set }
```

#### Discussion

Users may have different passes installed on different paired devices (for example, on an iPhone and an Apple Watch). This property lets you filter out the devices that already contain a matching pass.

## See Also

- [var paymentNetwork: PKPaymentNetwork?](pkaddpaymentpassrequestconfiguration/paymentnetwork.md)
  The payment network.
- [var requiresFelicaSecureElement: Bool](pkaddpaymentpassrequestconfiguration/requiresfelicasecureelement.md)
  A Boolean value that indicates whether the payment pass requires the Felica Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/primaryaccountidentifier)*