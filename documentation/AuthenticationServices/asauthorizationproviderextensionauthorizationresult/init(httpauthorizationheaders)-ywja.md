# init(httpAuthorizationHeaders:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Initializes an authorization with tokens stored in HTTP headers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(httpAuthorizationHeaders: [String : String])
```

```objc
- (instancetype) initWithHTTPAuthorizationHeaders:(NSDictionary<NSString *,NSString *> *) httpAuthorizationHeaders;
```

## Parameters

- `httpAuthorizationHeaders`: The HTTP authorization headers.

## See Also

### Initializers
- [init(httpResponse: HTTPURLResponse, httpBody: Data?)](./init%28httpresponse,httpbody%29-2j92m.md)
  Initializes an authorization with a HTTP response and body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationresult/init(httpauthorizationheaders:)-ywja)*