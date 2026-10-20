# PKInformationRequestCompletionBlock

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
typealias PKInformationRequestCompletionBlock = (PKBarcodeEventMetadataResponse) -> Void
```

```c
typedef void (^)(PKBarcodeEventMetadataResponse *) PKInformationRequestCompletionBlock;
```

## See Also

### Getting the transaction information
- [func handle(PKBarcodeEventConfigurationRequest, completion: () -> Void)](./pkpaymentinformationrequesthandling/handle%28_,completion%29-3cth8.md)
- [func handleInformationRequest(PKBarcodeEventMetadataRequest, completion: (PKBarcodeEventMetadataResponse) -> Void)](./pkpaymentinformationrequesthandling/handleinformationrequest%28_,completion%29.md)
- [class PKBarcodeEventConfigurationRequest](./pkbarcodeeventconfigurationrequest.md)
- [class PKBarcodeEventMetadataRequest](./pkbarcodeeventmetadatarequest.md)
- [class PKBarcodeEventMetadataResponse](./pkbarcodeeventmetadataresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkinformationrequestcompletionblock)*