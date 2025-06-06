# identityToken

**Framework**: Authentication Services  
**Kind**: property

A JSON Web Token (JWT) that securely communicates information about the user to the app.

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
var identityToken: Data? { get }
```

#### Discussion

The system encodes the object as a string using [`NSUTF8StringEncoding`](https://developer.apple.com/documentation/Foundation/NSUTF8StringEncoding).

## See Also

- [var authorizationCode: Data?](asauthorizationappleidcredential/authorizationcode.md)
  A token that the app uses to interact with the server.
- [var state: String?](asauthorizationappleidcredential/state.md)
  An arbitrary string that your app provides to the request that generates the credential.
- [var user: String](asauthorizationappleidcredential/user.md)
  An identifier for the authenticated user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/identitytoken)*