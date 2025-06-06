# complete(httpAuthorizationHeaders:)

**Framework**: Authentication Services  
**Kind**: method

Indicates the requested authorization succeeded with tokens in the HTTP headers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func complete(httpAuthorizationHeaders: [String : String])
```

## Parameters

- `httpAuthorizationHeaders`: The collection of tokens from the header.

## See Also

- [func complete(authorizationResult: ASAuthorizationProviderExtensionAuthorizationResult)](asauthorizationproviderextensionauthorizationrequest/complete(authorizationresult:).md)
- [func complete()](asauthorizationproviderextensionauthorizationrequest/complete.md)
  Indicates the requested authorization completed with no output.
- [func complete(httpResponse: HTTPURLResponse, httpBody: Data?)](asauthorizationproviderextensionauthorizationrequest/complete(httpresponse:httpbody:).md)
  Indicates the requested authorization succeeded with an HTTP response.
- [func complete(error: any Error)](asauthorizationproviderextensionauthorizationrequest/complete(error:).md)
  Indicates the requested authorization failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/complete(httpauthorizationheaders:))*