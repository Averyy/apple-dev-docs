# serialNumber

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A value that uniquely identifies the pass.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var serialNumber: String { get }
```

## See Also

- [var passType: PKPassType](pkpass/passtype.md)
  The pass’s type.
- [enum PKPassType](pkpasstype.md)
  Types of passes.
- [var secureElementPass: PKSecureElementPass?](pkpass/secureelementpass.md)
  The pass that contains an accompanying credential that the device stores in the Secure Element.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/serialnumber)*