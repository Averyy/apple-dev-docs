# complete(authorizationResult:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func complete(authorizationResult: ASAuthorizationProviderExtensionAuthorizationResult)
```

```objc
- (void) completeWithAuthorizationResult:(ASAuthorizationProviderExtensionAuthorizationResult *) authorizationResult;
```

## See Also

### Completing a Request
- [func complete()](./complete%28%29.md)
  Indicates the requested authorization completed with no output.
- [func complete(httpAuthorizationHeaders: [String : String])](./complete%28httpauthorizationheaders%29.md)
  Indicates the requested authorization succeeded with tokens in the HTTP headers.
- [func complete(httpResponse: HTTPURLResponse, httpBody: Data?)](./complete%28httpresponse,httpbody%29.md)
  Indicates the requested authorization succeeded with an HTTP response.
- [func complete(error: any Error)](./complete%28error%29.md)
  Indicates the requested authorization failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/complete(authorizationresult:))*