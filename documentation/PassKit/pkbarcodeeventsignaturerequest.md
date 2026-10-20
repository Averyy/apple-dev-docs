# PKBarcodeEventSignatureRequest

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
class PKBarcodeEventSignatureRequest
```

```objc
@interface PKBarcodeEventSignatureRequest : NSObject
```

## Topics

### Getting Transaction Details
- [var amount: NSNumber](./pkbarcodeeventsignaturerequest/amount.md)
- [var currencyCode: String](./pkbarcodeeventsignaturerequest/currencycode.md)
- [var transactionDate: Date](./pkbarcodeeventsignaturerequest/transactiondate.md)
- [var transactionIdentifier: String](./pkbarcodeeventsignaturerequest/transactionidentifier.md)
- [var transactionStatus: String](./pkbarcodeeventsignaturerequest/transactionstatus.md)
- [var merchantName: String](./pkbarcodeeventsignaturerequest/merchantname.md)
- [var rawMerchantName: String](./pkbarcodeeventsignaturerequest/rawmerchantname.md)
### Getting Signing Information
- [var partialSignature: Data](./pkbarcodeeventsignaturerequest/partialsignature.md)
- [var barcodeIdentifier: String](./pkbarcodeeventsignaturerequest/barcodeidentifier.md)
- [var deviceAccountIdentifier: String](./pkbarcodeeventsignaturerequest/deviceaccountidentifier.md)

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

### Signing the transaction
- [func handle(PKBarcodeEventSignatureRequest, completion: (PKBarcodeEventSignatureResponse) -> Void)](./pkpaymentinformationrequesthandling/handle%28_,completion%29-18x2y.md)
- [class PKBarcodeEventSignatureResponse](./pkbarcodeeventsignatureresponse.md)
- [typealias PKSignatureRequestCompletionBlock](./pksignaturerequestcompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkbarcodeeventsignaturerequest)*