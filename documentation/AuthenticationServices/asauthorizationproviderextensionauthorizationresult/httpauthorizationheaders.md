# httpAuthorizationHeaders

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A dictionary of authorization HTTP headers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var httpAuthorizationHeaders: [String : String]? { get set }
```

```objc
@property (nonatomic, nullable) NSDictionary<NSString *,NSString *> * httpAuthorizationHeaders;
```

## See Also

### Instance Properties
- [var httpResponse: HTTPURLResponse?](./httpresponse.md)
  The HTTP response for authentications.
- [var httpBody: Data?](./httpbody.md)
  The HTTP response body.
- [privateKeys](./privatekeys.md)
  An array of private security keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionauthorizationresult/httpauthorizationheaders)*