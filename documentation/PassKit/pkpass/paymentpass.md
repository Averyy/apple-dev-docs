# paymentPass

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The underlying payment pass.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [`secureElementPass`](./secureelementpass.md) instead.

## Declaration

```swift
var paymentPass: PKPaymentPass? { get }
```

```objc
@property (nonatomic, readonly, nullable) PKPaymentPass * paymentPass;
```

## See Also

### Identifying a pass
- [var passType: PKPassType](./passtype.md)
  The pass’s type.
- [enum PKPassType](../pkpasstype.md)
  Types of passes.
- [var secureElementPass: PKSecureElementPass?](./secureelementpass.md)
  The pass that contains an accompanying credential that the device stores in the Secure Element.
- [var serialNumber: String](./serialnumber.md)
  A value that uniquely identifies the pass.
- [var passTypeIdentifier: String](./passtypeidentifier.md)
  The pass’s pass type identifier.
- [var deviceName: String](./devicename.md)
  The name of the device that hosts the pass.
- [var localizedName: String](./localizedname.md)
  The localized name for the pass’s template.
- [var localizedDescription: String](./localizeddescription.md)
  The pass’s localized description.
- [var isRemotePass: Bool](./isremotepass.md)
  A Boolean value that indicates whether the pass is on a paired device, such as an Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/paymentpass)*