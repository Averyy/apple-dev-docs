# PKBarcodeEventConfigurationRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class PKBarcodeEventConfigurationRequest
```

```objc
@interface PKBarcodeEventConfigurationRequest : NSObject
```

## Topics

### Reading Configuration Information
- [var deviceAccountIdentifier: String](./pkbarcodeeventconfigurationrequest/deviceaccountidentifier.md)
- [var configurationDataType: PKBarcodeEventConfigurationDataType](./pkbarcodeeventconfigurationrequest/configurationdatatype.md)
- [var configurationData: Data](./pkbarcodeeventconfigurationrequest/configurationdata.md)
- [enum PKBarcodeEventConfigurationDataType](./pkbarcodeeventconfigurationdatatype.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Getting the transaction information
- [func handle(PKBarcodeEventConfigurationRequest, completion: () -> Void)](./pkpaymentinformationrequesthandling/handle%28_,completion%29-3cth8.md)
- [func handleInformationRequest(PKBarcodeEventMetadataRequest, completion: (PKBarcodeEventMetadataResponse) -> Void)](./pkpaymentinformationrequesthandling/handleinformationrequest%28_,completion%29.md)
- [class PKBarcodeEventMetadataRequest](./pkbarcodeeventmetadatarequest.md)
- [class PKBarcodeEventMetadataResponse](./pkbarcodeeventmetadataresponse.md)
- [typealias PKInformationRequestCompletionBlock](./pkinformationrequestcompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkbarcodeeventconfigurationrequest)*