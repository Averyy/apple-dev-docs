# uuid

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var uuid: UUID { get }
```

```objc
@property (nonatomic, readonly) NSUUID * UUID;
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](../supporting-single-sign-on-in-a-web-browser-app.md)

## See Also

### Interpreting a request
- [var url: URL](./url.md)
  The web address the browser should use to perform the authentication request.
- [var shouldUseEphemeralSession: Bool](./shoulduseephemeralsession.md)
  A Boolean that indicates whether the browser should use a private browsing session.
- [var additionalHeaderFields: [String : String]?](./additionalheaderfields.md)
  Additional headers to send when loading the initial URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/uuid)*