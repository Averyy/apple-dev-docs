# requestData

**Framework**: IdentityDocumentServices  
**Kind**: property  
**Role**: Instance Property

The request data blob for the web presentment raw request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst
- macOS 26.0+

## Declaration

```swift
var requestData: Data
```

#### Discussion

The system encodes this according to the specified request type.

## See Also

### Creating an identity document web presentment raw request
- [init(requestType: IdentityDocumentWebPresentmentRawRequest.RequestType, requestData: Data)](./init%28requesttype,requestdata%29.md)
  Initializes a web presentment raw request.
- [var requestType: IdentityDocumentWebPresentmentRawRequest.RequestType](./requesttype-swift.property.md)
  The request type for the current request that the system uses to help the document provider deserialize the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrawrequest/requestdata)*