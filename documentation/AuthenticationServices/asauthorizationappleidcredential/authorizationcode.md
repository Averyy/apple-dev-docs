# authorizationCode

**Framework**: Authentication Services  
**Kind**: property

A token that the app uses to interact with the server.

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
var authorizationCode: Data? { get }
```

#### Discussion

Your app uses this short-lived token as proof that it has authorization to interact with the server.

The system encodes the object as a string using [`NSUTF8StringEncoding`](https://developer.apple.com/documentation/Foundation/NSUTF8StringEncoding).

## See Also

- [var identityToken: Data?](asauthorizationappleidcredential/identitytoken.md)
  A JSON Web Token (JWT) that securely communicates information about the user to the app.
- [var state: String?](asauthorizationappleidcredential/state.md)
  An arbitrary string that your app provides to the request that generates the credential.
- [var user: String](asauthorizationappleidcredential/user.md)
  An identifier for the authenticated user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/authorizationcode)*