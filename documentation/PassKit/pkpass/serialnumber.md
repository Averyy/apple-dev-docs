# serialNumber

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A value that uniquely identifies the pass.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
var serialNumber: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * serialNumber;
```

## See Also

### Identifying a pass
- [var passType: PKPassType](./passtype.md)
  The pass’s type.
- [enum PKPassType](../pkpasstype.md)
  Types of passes.
- [var secureElementPass: PKSecureElementPass?](./secureelementpass.md)
  The pass that contains an accompanying credential that the device stores in the Secure Element.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/serialnumber)*