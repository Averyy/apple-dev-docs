# PKBarcodeEventSignatureResponse

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
class PKBarcodeEventSignatureResponse
```

```objc
@interface PKBarcodeEventSignatureResponse : NSObject
```

## Topics

### Creating a Signature Response
- [init(signedData: Data)](./pkbarcodeeventsignatureresponse/init%28signeddata%29.md)
### Returning the Signature
- [var signedData: Data](./pkbarcodeeventsignatureresponse/signeddata.md)

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
- [class PKBarcodeEventSignatureRequest](./pkbarcodeeventsignaturerequest.md)
- [typealias PKSignatureRequestCompletionBlock](./pksignaturerequestcompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkbarcodeeventsignatureresponse)*