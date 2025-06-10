# PKInformationRequestCompletionBlock

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: typealias

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias PKInformationRequestCompletionBlock = (PKBarcodeEventMetadataResponse) -> Void
```

## See Also

- [func handle(PKBarcodeEventConfigurationRequest, completion: () -> Void)](pkpaymentinformationrequesthandling/handle(_:completion:)-3cth8.md)
- [func handleInformationRequest(PKBarcodeEventMetadataRequest, completion: (PKBarcodeEventMetadataResponse) -> Void)](pkpaymentinformationrequesthandling/handleinformationrequest(_:completion:).md)
- [class PKBarcodeEventConfigurationRequest](pkbarcodeeventconfigurationrequest.md)
- [class PKBarcodeEventMetadataRequest](pkbarcodeeventmetadatarequest.md)
- [class PKBarcodeEventMetadataResponse](pkbarcodeeventmetadataresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkinformationrequestcompletionblock)*