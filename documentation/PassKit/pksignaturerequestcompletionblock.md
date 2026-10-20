# PKSignatureRequestCompletionBlock

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
typealias PKSignatureRequestCompletionBlock = (PKBarcodeEventSignatureResponse) -> Void
```

```c
typedef void (^)(PKBarcodeEventSignatureResponse *) PKSignatureRequestCompletionBlock;
```

## See Also

### Signing the transaction
- [func handle(PKBarcodeEventSignatureRequest, completion: (PKBarcodeEventSignatureResponse) -> Void)](./pkpaymentinformationrequesthandling/handle%28_,completion%29-18x2y.md)
- [class PKBarcodeEventSignatureRequest](./pkbarcodeeventsignaturerequest.md)
- [class PKBarcodeEventSignatureResponse](./pkbarcodeeventsignatureresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksignaturerequestcompletionblock)*