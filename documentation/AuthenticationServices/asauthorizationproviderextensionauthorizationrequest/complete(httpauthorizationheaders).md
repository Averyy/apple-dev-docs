# complete(httpAuthorizationHeaders:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) completeWithHTTPAuthorizationHeaders:(NSDictionary<NSString *,NSString *> *) httpAuthorizationHeaders;
```

## Parameters

- `httpAuthorizationHeaders`: The collection of tokens from the header.

## See Also

### Completing a Request
- [func complete(authorizationResult: ASAuthorizationProviderExtensionAuthorizationResult)](./complete%28authorizationresult%29.md)
- [func complete()](./complete%28%29.md)
  Indicates the requested authorization completed with no output.
- [func complete(httpResponse: HTTPURLResponse, httpBody: Data?)](./complete%28httpresponse,httpbody%29.md)
  Indicates the requested authorization succeeded with an HTTP response.
- [func complete(error: any Error)](./complete%28error%29.md)
  Indicates the requested authorization failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/complete(httpauthorizationheaders:))*