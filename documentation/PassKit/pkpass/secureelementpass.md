# secureElementPass

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The pass that contains an accompanying credential that the device stores in the Secure Element.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var secureElementPass: PKSecureElementPass? { get }
```

#### Discussion

Passes that contain sensitive information — for example, payment cards or digital car keys — store that information in the device’s Secure Element as an instance of [`PKSecureElementPass`](pksecureelementpass.md). Use this property to access the accompanying pass, which you can then use for other operations, such as signing data using a cryptographic signature.

## See Also

- [var passType: PKPassType](pkpass/passtype.md)
  The pass’s type.
- [enum PKPassType](pkpasstype.md)
  Types of passes.
- [var serialNumber: String](pkpass/serialnumber.md)
  A value that uniquely identifies the pass.
- [var passTypeIdentifier: String](pkpass/passtypeidentifier.md)
  The pass’s pass type identifier.
- [var deviceName: String](pkpass/devicename.md)
  The name of the device that hosts the pass.
- [var localizedName: String](pkpass/localizedname.md)
  The localized name for the pass’s template.
- [var localizedDescription: String](pkpass/localizeddescription.md)
  The pass’s localized description.
- [var isRemotePass: Bool](pkpass/isremotepass.md)
  A Boolean value that indicates whether the pass is on a paired device, such as an Apple Watch.
- [var paymentPass: PKPaymentPass?](pkpass/paymentpass.md)
  The underlying payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/secureelementpass)*