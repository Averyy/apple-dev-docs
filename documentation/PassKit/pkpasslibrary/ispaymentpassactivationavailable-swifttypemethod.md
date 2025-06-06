# isPaymentPassActivationAvailable()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns a Boolean value that indicates whether the device supports adding payment passes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func isPaymentPassActivationAvailable() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the device supports adding payment passes.

## See Also

- [func activate(PKPaymentPass, withActivationCode: String, completion: ((Bool, any Error) -> Void)?)](pkpasslibrary/activate(_:withactivationcode:completion:).md)
  Activates a payment pass using the provided activation code.
- [func activate(PKPaymentPass, withActivationData: Data, completion: ((Bool, any Error) -> Void)?)](pkpasslibrary/activate(_:withactivationdata:completion:).md)
  Activates a payment pass using the provided activation code.
- [func canAddPaymentPass(withPrimaryAccountIdentifier: String) -> Bool](pkpasslibrary/canaddpaymentpass(withprimaryaccountidentifier:).md)
  A Boolean value that indicates whether the app can add a card to Apple Pay for the provided primary account identifier.
- [func isPaymentPassActivationAvailable() -> Bool](pkpasslibrary/ispaymentpassactivationavailable-swift.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func present(PKPaymentPass)](pkpasslibrary/present(_:)-67jce.md)
  Presents the payment pass for use in-store.
- [func remotePaymentPasses() -> [PKPaymentPass]](pkpasslibrary/remotepaymentpasses.md)
  Returns a list of passes from a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/ispaymentpassactivationavailable()-swift.type.method)*