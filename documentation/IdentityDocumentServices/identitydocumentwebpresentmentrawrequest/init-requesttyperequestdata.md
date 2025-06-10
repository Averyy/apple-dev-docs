# init(requestType:requestData:)

**Framework**: IdentityDocumentServices  
**Kind**: init

Initializes a web presentment raw request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
init(requestType: IdentityDocumentWebPresentmentRawRequest.RequestType, requestData: Data)
```

## Parameters

- `requestType`: The request type for the current request. This aids the document provider in deserializing the request.
- `requestData`: The request data blob. You encode this according to the specified request type.

## See Also

- [var requestData: Data](identitydocumentwebpresentmentrawrequest/requestdata.md)
  The request data blob for the web presentment raw request.
- [var requestType: IdentityDocumentWebPresentmentRawRequest.RequestType](identitydocumentwebpresentmentrawrequest/requesttype-swift.property.md)
  The request type for the current request that the system uses to help the document provider deserialize the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrawrequest/init(requesttype:requestdata:))*