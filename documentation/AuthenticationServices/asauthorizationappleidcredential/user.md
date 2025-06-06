# user

**Framework**: Authentication Services  
**Kind**: property

An identifier for the authenticated user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var user: String { get }
```

## See Also

- [var identityToken: Data?](asauthorizationappleidcredential/identitytoken.md)
  A JSON Web Token (JWT) that securely communicates information about the user to the app.
- [var authorizationCode: Data?](asauthorizationappleidcredential/authorizationcode.md)
  A token that the app uses to interact with the server.
- [var state: String?](asauthorizationappleidcredential/state.md)
  An arbitrary string that your app provides to the request that generates the credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/user)*