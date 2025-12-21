# url

**Framework**: Authentication Services  
**Kind**: property

The web address the browser should use to perform the authentication request.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var url: URL { get }
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

## See Also

- [var shouldUseEphemeralSession: Bool](aswebauthenticationsessionrequest/shoulduseephemeralsession.md)
  A Boolean that indicates whether the browser should use a private browsing session.
- [var uuid: UUID](aswebauthenticationsessionrequest/uuid.md)
  A unique identifier for the request.
- [var additionalHeaderFields: [String : String]?](aswebauthenticationsessionrequest/additionalheaderfields.md)
  Additional headers to send when loading the initial URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/url)*