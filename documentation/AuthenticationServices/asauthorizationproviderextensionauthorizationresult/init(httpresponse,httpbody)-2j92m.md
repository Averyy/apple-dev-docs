# init(httpResponse:httpBody:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Initializes an authorization with a HTTP response and body.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(httpResponse: HTTPURLResponse, httpBody: Data?)
```

```objc
- (instancetype) initWithHTTPResponse:(NSHTTPURLResponse *) httpResponse httpBody:(NSData *) httpBody;
```

## Parameters

- `httpResponse`: The HTTP response.
- `httpBody`: The HTTP body.

## See Also

### Initializers
- [init(httpAuthorizationHeaders: [String : String])](./init%28httpauthorizationheaders%29-ywja.md)
  Initializes an authorization with tokens stored in HTTP headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationresult/init(httpresponse:httpbody:)-2j92m)*