# authorizationCode

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) NSData * authorizationCode;
```

#### Discussion

Your app uses this short-lived token as proof that it has authorization to interact with the server.

The system encodes the object as a string using [`NSUTF8StringEncoding`](../../Foundation/nsutf8stringencoding.md).

## See Also

### Identifying a User
- [var identityToken: Data?](./identitytoken.md)
  A JSON Web Token (JWT) that securely communicates information about the user to the app.
- [var state: String?](./state.md)
  An arbitrary string that your app provides to the request that generates the credential.
- [var user: String](./user.md)
  An identifier for the authenticated user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential/authorizationcode)*