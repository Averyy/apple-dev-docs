# shouldUseEphemeralSession

**Framework**: Authentication Services  
**Kind**: property

A Boolean that indicates whether the browser should use a private browsing session.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var shouldUseEphemeralSession: Bool { get }
```

## Mentions

- [Supporting Single Sign-On in a Web Browser App](supporting-single-sign-on-in-a-web-browser-app.md)

## See Also

- [var url: URL](aswebauthenticationsessionrequest/url.md)
  The web address the browser should use to perform the authentication request.
- [var callbackURLScheme: String?](aswebauthenticationsessionrequest/callbackurlscheme.md)
  The scheme the browser should use to return the result of the authentication attempt to the app requesting it.
- [var uuid: UUID](aswebauthenticationsessionrequest/uuid.md)
  A unique identifier for the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/shoulduseephemeralsession)*