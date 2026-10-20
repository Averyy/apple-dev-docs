# PKBarcodeEventConfigurationDataType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum PKBarcodeEventConfigurationDataType
```

```c
enum PKBarcodeEventConfigurationDataType : NSInteger;
```

## Topics

### QR Code Purchase Signing Types
- [PKBarcodeEventConfigurationDataType.signingCertificate](./pkbarcodeeventconfigurationdatatype/signingcertificate.md)
- [PKBarcodeEventConfigurationDataType.signingKeyMaterial](./pkbarcodeeventconfigurationdatatype/signingkeymaterial.md)
- [PKBarcodeEventConfigurationDataType.unknown](./pkbarcodeeventconfigurationdatatype/unknown.md)
### Initializers
- [init?(rawValue: Int)](./pkbarcodeeventconfigurationdatatype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Reading Configuration Information
- [var deviceAccountIdentifier: String](./pkbarcodeeventconfigurationrequest/deviceaccountidentifier.md)
- [var configurationDataType: PKBarcodeEventConfigurationDataType](./pkbarcodeeventconfigurationrequest/configurationdatatype.md)
- [var configurationData: Data](./pkbarcodeeventconfigurationrequest/configurationdata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkbarcodeeventconfigurationdatatype)*