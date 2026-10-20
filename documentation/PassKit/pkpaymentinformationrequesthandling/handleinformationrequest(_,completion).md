# handleInformationRequest(_:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func handleInformationRequest(_ infoRequest: PKBarcodeEventMetadataRequest, completion: @escaping @Sendable (PKBarcodeEventMetadataResponse) -> Void)
```

```swift
func handleInformationRequest(_ infoRequest: PKBarcodeEventMetadataRequest) async -> PKBarcodeEventMetadataResponse
```

```objc
- (void) handleInformationRequest:(PKBarcodeEventMetadataRequest *) infoRequest completion:(PKInformationRequestCompletionBlock) completion;
```

## See Also

### Getting the transaction information
- [func handle(PKBarcodeEventConfigurationRequest, completion: () -> Void)](./handle%28_,completion%29-3cth8.md)
- [class PKBarcodeEventConfigurationRequest](../pkbarcodeeventconfigurationrequest.md)
- [class PKBarcodeEventMetadataRequest](../pkbarcodeeventmetadatarequest.md)
- [class PKBarcodeEventMetadataResponse](../pkbarcodeeventmetadataresponse.md)
- [typealias PKInformationRequestCompletionBlock](../pkinformationrequestcompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentinformationrequesthandling/handleinformationrequest(_:completion:))*