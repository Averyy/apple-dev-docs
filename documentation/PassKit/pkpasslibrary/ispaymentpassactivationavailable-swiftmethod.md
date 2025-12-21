# isPaymentPassActivationAvailable()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns a Boolean value that indicates whether the device supports adding payment passes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isPaymentPassActivationAvailable() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the device supports adding payment passes.

#### Discussion

Activating payment passes requires a special entitlement from Apple. If the entitlement isn’t present, this method returns [`false`](https://developer.apple.com/documentation/Swift/false).  For more information about requesting this entitlement, see [`developer.apple.com/apple-pay/`](https://developer.apple.comhttps://developer.apple.com/apple-pay/).

## See Also

- [func activate(PKPaymentPass, withActivationCode: String, completion: ((Bool, any Error) -> Void)?)](pkpasslibrary/activate(_:withactivationcode:completion:).md)
  Activates a payment pass using the provided activation code.
- [func activate(PKPaymentPass, withActivationData: Data, completion: ((Bool, any Error) -> Void)?)](pkpasslibrary/activate(_:withactivationdata:completion:).md)
  Activates a payment pass using the provided activation code.
- [func canAddPaymentPass(withPrimaryAccountIdentifier: String) -> Bool](pkpasslibrary/canaddpaymentpass(withprimaryaccountidentifier:).md)
  A Boolean value that indicates whether the app can add a card to Apple Pay for the provided primary account identifier.
- [class func isPaymentPassActivationAvailable() -> Bool](pkpasslibrary/ispaymentpassactivationavailable-swift.type.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func present(PKPaymentPass)](pkpasslibrary/present(_:)-67jce.md)
  Presents the payment pass for use in-store.
- [func remotePaymentPasses() -> [PKPaymentPass]](pkpasslibrary/remotepaymentpasses.md)
  Returns a list of passes from a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/ispaymentpassactivationavailable()-swift.method)*