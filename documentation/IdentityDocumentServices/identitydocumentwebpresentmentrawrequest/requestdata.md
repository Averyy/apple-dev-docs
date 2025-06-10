# requestData

**Framework**: IdentityDocumentServices  
**Kind**: property

The request data blob for the web presentment raw request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
var requestData: Data
```

#### Discussion

The system encodes this according to the specified request type.

## See Also

- [init(requestType: IdentityDocumentWebPresentmentRawRequest.RequestType, requestData: Data)](identitydocumentwebpresentmentrawrequest/init(requesttype:requestdata:).md)
  Initializes a web presentment raw request.
- [var requestType: IdentityDocumentWebPresentmentRawRequest.RequestType](identitydocumentwebpresentmentrawrequest/requesttype-swift.property.md)
  The request type for the current request that the system uses to help the document provider deserialize the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrawrequest/requestdata)*