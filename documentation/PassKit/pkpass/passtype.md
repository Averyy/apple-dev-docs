# passType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The pass’s type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var passType: PKPassType { get }
```

#### Discussion

For possible values, see [`PKPassType`](pkpasstype.md).

## See Also

- [enum PKPassType](pkpasstype.md)
  Types of passes.
- [var secureElementPass: PKSecureElementPass?](pkpass/secureelementpass.md)
  The pass that contains an accompanying credential that the device stores in the Secure Element.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/passtype)*