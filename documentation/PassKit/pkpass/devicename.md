# deviceName

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The name of the device that hosts the pass.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var deviceName: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * deviceName;
```

#### Discussion

If [`isRemotePass`](./isremotepass.md) is [`true`](../../Swift/true.md), this property contains the name of the paired device that stores the pass; otherwise, it contains the name of the device.

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
- [var localizedName: String](./localizedname.md)
  The localized name for the pass’s template.
- [var localizedDescription: String](./localizeddescription.md)
  The pass’s localized description.
- [var isRemotePass: Bool](./isremotepass.md)
  A Boolean value that indicates whether the pass is on a paired device, such as an Apple Watch.
- [var paymentPass: PKPaymentPass?](./paymentpass.md)
  The underlying payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/devicename)*