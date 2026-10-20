# complete()

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Indicates the requested authorization completed with no output.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func complete()
```

```objc
- (void) complete;
```

## See Also

### Completing a Request
- [func complete(authorizationResult: ASAuthorizationProviderExtensionAuthorizationResult)](./complete%28authorizationresult%29.md)
- [func complete(httpAuthorizationHeaders: [String : String])](./complete%28httpauthorizationheaders%29.md)
  Indicates the requested authorization succeeded with tokens in the HTTP headers.
- [func complete(httpResponse: HTTPURLResponse, httpBody: Data?)](./complete%28httpresponse,httpbody%29.md)
  Indicates the requested authorization succeeded with an HTTP response.
- [func complete(error: any Error)](./complete%28error%29.md)
  Indicates the requested authorization failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/complete())*