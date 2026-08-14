# PKBarcodeEventMetadataResponse

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
class PKBarcodeEventMetadataResponse
```

## Topics

### Creating an Event Metadata Response
- [init(paymentInformation: Data)](pkbarcodeeventmetadataresponse/init(paymentinformation:).md)
### Getting QR Payment Information
- [var paymentInformation: Data](pkbarcodeeventmetadataresponse/paymentinformation.md)

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
- [class PKBarcodeEventConfigurationRequest](pkbarcodeeventconfigurationrequest.md)
- [class PKBarcodeEventMetadataRequest](pkbarcodeeventmetadatarequest.md)
- [typealias PKInformationRequestCompletionBlock](pkinformationrequestcompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkbarcodeeventmetadataresponse)*