# canAddPaymentPass(withPrimaryAccountIdentifier:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

A Boolean value that indicates whether the app can add a card to Apple Pay for the provided primary account identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func canAddPaymentPass(withPrimaryAccountIdentifier primaryAccountIdentifier: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if PassKit can add the pass.

#### Discussion

Adding payment passes requires a special entitlement from Apple. If the entitlement isn’t present, this method returns [`false`](https://developer.apple.com/documentation/Swift/false).  For more information about requesting this entitlement, see [`developer.apple.com/apple-pay/`](https://developer.apple.comhttps://developer.apple.com/apple-pay/).

## Parameters

- `primaryAccountIdentifier`: A unique identifier for the underlying funding primary account number (PAN). This isn’t the PAN itself.

## See Also

- [func activate(PKPaymentPass, withActivationCode: String, completion: ((Bool, any Error) -> Void)?)](pkpasslibrary/activate(_:withactivationcode:completion:).md)
  Activates a payment pass using the provided activation code.
- [func activate(PKPaymentPass, withActivationData: Data, completion: ((Bool, any Error) -> Void)?)](pkpasslibrary/activate(_:withactivationdata:completion:).md)
  Activates a payment pass using the provided activation code.
- [class func isPaymentPassActivationAvailable() -> Bool](pkpasslibrary/ispaymentpassactivationavailable-swift.type.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func isPaymentPassActivationAvailable() -> Bool](pkpasslibrary/ispaymentpassactivationavailable-swift.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func present(PKPaymentPass)](pkpasslibrary/present(_:)-67jce.md)
  Presents the payment pass for use in-store.
- [func remotePaymentPasses() -> [PKPaymentPass]](pkpasslibrary/remotepaymentpasses.md)
  Returns a list of passes from a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/canaddpaymentpass(withprimaryaccountidentifier:))*