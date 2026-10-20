# url

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The web address the browser should use to perform the authentication request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var url: URL { get }
```

```objc
@property (nonatomic, readonly) NSURL * URL;
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](../supporting-single-sign-on-in-a-web-browser-app.md)

## See Also

### Interpreting a request
- [var shouldUseEphemeralSession: Bool](./shoulduseephemeralsession.md)
  A Boolean that indicates whether the browser should use a private browsing session.
- [var uuid: UUID](./uuid.md)
  A unique identifier for the request.
- [var additionalHeaderFields: [String : String]?](./additionalheaderfields.md)
  Additional headers to send when loading the initial URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/url)*