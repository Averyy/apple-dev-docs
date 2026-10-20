# handle(_:completion:)

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
func handle(_ configurationRequest: PKBarcodeEventConfigurationRequest, completion: @escaping @Sendable () -> Void)
```

```swift
func handle(_ configurationRequest: PKBarcodeEventConfigurationRequest) async
```

```objc
- (void) handleConfigurationRequest:(PKBarcodeEventConfigurationRequest *) configurationRequest completion:(void (^)()) completion;
```

## See Also

### Getting the transaction information
- [func handleInformationRequest(PKBarcodeEventMetadataRequest, completion: (PKBarcodeEventMetadataResponse) -> Void)](./handleinformationrequest%28_,completion%29.md)
- [class PKBarcodeEventConfigurationRequest](../pkbarcodeeventconfigurationrequest.md)
- [class PKBarcodeEventMetadataRequest](../pkbarcodeeventmetadatarequest.md)
- [class PKBarcodeEventMetadataResponse](../pkbarcodeeventmetadataresponse.md)
- [typealias PKInformationRequestCompletionBlock](../pkinformationrequestcompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentinformationrequesthandling/handle(_:completion:)-3cth8)*