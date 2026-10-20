# complete(httpResponse:httpBody:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Indicates the requested authorization succeeded with an HTTP response.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func complete(httpResponse: HTTPURLResponse, httpBody: Data?)
```

```objc
- (void) completeWithHTTPResponse:(NSHTTPURLResponse *) httpResponse httpBody:(NSData *) httpBody;
```

## Parameters

- `httpResponse`: The metadata associated with the HTTP response.
- `httpBody`: The body of the HTTP response.

## See Also

### Completing a Request
- [func complete(authorizationResult: ASAuthorizationProviderExtensionAuthorizationResult)](./complete%28authorizationresult%29.md)
- [func complete()](./complete%28%29.md)
  Indicates the requested authorization completed with no output.
- [func complete(httpAuthorizationHeaders: [String : String])](./complete%28httpauthorizationheaders%29.md)
  Indicates the requested authorization succeeded with tokens in the HTTP headers.
- [func complete(error: any Error)](./complete%28error%29.md)
  Indicates the requested authorization failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationrequest/complete(httpresponse:httpbody:))*