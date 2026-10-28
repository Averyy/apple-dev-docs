# secureElementPass

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) PKSecureElementPass * secureElementPass;
```

## Discussion

Passes that contain sensitive information — for example, payment cards or digital car keys — store that information in the device’s Secure Element as an instance of [`PKSecureElementPass`](../pksecureelementpass.md). Use this property to access the accompanying pass, which you can then use for other operations, such as signing data using a cryptographic signature.

## See Also

### Identifying a pass
- [var passType: PKPassType](./passtype.md)
  The pass’s type.
- [enum PKPassType](../pkpasstype.md)
  Types of passes.
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
- [var paymentPass: PKPaymentPass?](./paymentpass.md)
  The underlying payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/secureelementpass)*