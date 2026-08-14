# PKBarcodeEventConfigurationRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class PKBarcodeEventConfigurationRequest
```

## Topics

### Reading Configuration Information
- [var deviceAccountIdentifier: String](pkbarcodeeventconfigurationrequest/deviceaccountidentifier.md)
- [var configurationDataType: PKBarcodeEventConfigurationDataType](pkbarcodeeventconfigurationrequest/configurationdatatype.md)
- [var configurationData: Data](pkbarcodeeventconfigurationrequest/configurationdata.md)
- [enum PKBarcodeEventConfigurationDataType](pkbarcodeeventconfigurationdatatype.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [func handle(PKBarcodeEventConfigurationRequest, completion: () -> Void)](pkpaymentinformationrequesthandling/handle(_:completion:)-3cth8.md)
- [func handleInformationRequest(PKBarcodeEventMetadataRequest, completion: (PKBarcodeEventMetadataResponse) -> Void)](pkpaymentinformationrequesthandling/handleinformationrequest(_:completion:).md)
- [class PKBarcodeEventMetadataRequest](pkbarcodeeventmetadatarequest.md)
- [class PKBarcodeEventMetadataResponse](pkbarcodeeventmetadataresponse.md)
- [typealias PKInformationRequestCompletionBlock](pkinformationrequestcompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkbarcodeeventconfigurationrequest)*