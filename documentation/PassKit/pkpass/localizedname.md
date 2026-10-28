# localizedName

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The localized name for the pass’s template.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
var localizedName: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * localizedName;
```

## Discussion

The pass’s template defines the pass’s basic layout. For more information about the available templates, see [Pass Style Sets the Overall Visual Appearance](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/Creating.html#//apple_ref/doc/uid/TP40012195-CH4-SW45) in [Wallet Developer Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/index.html#//apple_ref/doc/uid/TP40012195).

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
- [var localizedDescription: String](./localizeddescription.md)
  The pass’s localized description.
- [var isRemotePass: Bool](./isremotepass.md)
  A Boolean value that indicates whether the pass is on a paired device, such as an Apple Watch.
- [var paymentPass: PKPaymentPass?](./paymentpass.md)
  The underlying payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/localizedname)*