# handle(_:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func handle(_ configurationRequest: PKBarcodeEventConfigurationRequest) async
```

## See Also

- [func handleInformationRequest(PKBarcodeEventMetadataRequest, completion: PKInformationRequestCompletionBlock)](pkpaymentinformationrequesthandling/handleinformationrequest(_:completion:).md)
- [class PKBarcodeEventConfigurationRequest](pkbarcodeeventconfigurationrequest.md)
- [class PKBarcodeEventMetadataRequest](pkbarcodeeventmetadatarequest.md)
- [class PKBarcodeEventMetadataResponse](pkbarcodeeventmetadataresponse.md)
- [typealias PKInformationRequestCompletionBlock](pkinformationrequestcompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentinformationrequesthandling/handle(_:completion:)-3cth8)*