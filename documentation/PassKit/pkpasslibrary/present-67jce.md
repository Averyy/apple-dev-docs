# present(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Presents the payment pass for use in-store.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
func present(_ pass: PKPaymentPass)
```

#### Discussion

You can use [`present(_:)`](pkpasslibrary/present(_:)-67jce.md)  to present your payment pass for use in-store.  Your app must have the proper entitlement to see the payment pass that you present. Therefore, this method is mostly relevant to a bank or merchant app that presents its own payment method for use in-store.

## Parameters

- `pass`: The pass to present.

## See Also

- [func activate(PKPaymentPass, withActivationCode: String, completion: ((Bool, any Error) -> Void)?)](pkpasslibrary/activate(_:withactivationcode:completion:).md)
  Activates a payment pass using the provided activation code.
- [func activate(PKPaymentPass, withActivationData: Data, completion: ((Bool, any Error) -> Void)?)](pkpasslibrary/activate(_:withactivationdata:completion:).md)
  Activates a payment pass using the provided activation code.
- [func canAddPaymentPass(withPrimaryAccountIdentifier: String) -> Bool](pkpasslibrary/canaddpaymentpass(withprimaryaccountidentifier:).md)
  A Boolean value that indicates whether the app can add a card to Apple Pay for the provided primary account identifier.
- [class func isPaymentPassActivationAvailable() -> Bool](pkpasslibrary/ispaymentpassactivationavailable-swift.type.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func isPaymentPassActivationAvailable() -> Bool](pkpasslibrary/ispaymentpassactivationavailable-swift.method.md)
  Returns a Boolean value that indicates whether the device supports adding payment passes.
- [func remotePaymentPasses() -> [PKPaymentPass]](pkpasslibrary/remotepaymentpasses.md)
  Returns a list of passes from a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/present(_:)-67jce)*