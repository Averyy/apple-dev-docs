# state

**Framework**: Authentication Services  
**Kind**: property

An arbitrary string that your app provides to the request that generates the credential.

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
var state: String? { get }
```

## See Also

- [var identityToken: Data?](asauthorizationappleidcredential/identitytoken.md)
  A JSON Web Token (JWT) that securely communicates information about the user to the app.
- [var authorizationCode: Data?](asauthorizationappleidcredential/authorizationcode.md)
  A token that the app uses to interact with the server.
- [var user: String](asauthorizationappleidcredential/user.md)
  An identifier for the authenticated user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/state)*