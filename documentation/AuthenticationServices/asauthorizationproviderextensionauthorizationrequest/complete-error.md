# complete(error:)

**Framework**: Authentication Services  
**Kind**: method

Indicates the requested authorization failed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func complete(error: any Error)
```

## Parameters

- `error`: An indication of why the authorization failed.

## See Also

- [func complete(authorizationResult: ASAuthorizationProviderExtensionAuthorizationResult)](asauthorizationproviderextensionauthorizationrequest/complete(authorizationresult:).md)
- [func complete()](asauthorizationproviderextensionauthorizationrequest/complete.md)
  Indicates the requested authorization completed with no output.
- [func complete(httpAuthorizationHeaders: [String : String])](asauthorizationproviderextensionauthorizationrequest/complete(httpauthorizationheaders:).md)
  Indicates the requested authorization succeeded with tokens in the HTTP headers.
- [func complete(httpResponse: HTTPURLResponse, httpBody: Data?)](asauthorizationproviderextensionauthorizationrequest/complete(httpresponse:httpbody:).md)
  Indicates the requested authorization succeeded with an HTTP response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/complete(error:))*