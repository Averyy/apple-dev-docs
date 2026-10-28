# primaryAccountIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A primary account identifier, used to filter out pass libraries.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+

## Declaration

```swift
var primaryAccountIdentifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * primaryAccountIdentifier;
```

## Discussion

Users may have different passes installed on different paired devices (for example, on an iPhone and an Apple Watch). This property lets you filter out the devices that already contain a matching pass.

## See Also

### Filtering pass libraries
- [var paymentNetwork: PKPaymentNetwork?](./paymentnetwork.md)
  The payment network.
- [var requiresFelicaSecureElement: Bool](./requiresfelicasecureelement.md)
  A Boolean value that indicates whether the payment pass requires the Felica Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/primaryaccountidentifier)*