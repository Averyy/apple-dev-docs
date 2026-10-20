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
func handle(_ signatureRequest: PKBarcodeEventSignatureRequest, completion: @escaping @Sendable (PKBarcodeEventSignatureResponse) -> Void)
```

```swift
func handle(_ signatureRequest: PKBarcodeEventSignatureRequest) async -> PKBarcodeEventSignatureResponse
```

```objc
- (void) handleSignatureRequest:(PKBarcodeEventSignatureRequest *) signatureRequest completion:(PKSignatureRequestCompletionBlock) completion;
```

## See Also

### Signing the transaction
- [class PKBarcodeEventSignatureRequest](../pkbarcodeeventsignaturerequest.md)
- [class PKBarcodeEventSignatureResponse](../pkbarcodeeventsignatureresponse.md)
- [typealias PKSignatureRequestCompletionBlock](../pksignaturerequestcompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentinformationrequesthandling/handle(_:completion:)-18x2y)*