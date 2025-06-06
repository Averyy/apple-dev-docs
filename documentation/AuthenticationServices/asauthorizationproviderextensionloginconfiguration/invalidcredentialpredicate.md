# invalidCredentialPredicate

**Framework**: Authentication Services  
**Kind**: property

The predicate string that identifies invalid credential errors.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var invalidCredentialPredicate: String? { get set }
```

## Mentions

- [Creating a JSON Web Encryption (JWE) login response](creating-a-json-web-encryption-jwe-login-response.md)

#### Discussion

If the server returns an HTTP 400 or HTTP 401 error when authenticating, the system uses this predicate on the response body JSON. It then determines whether the error is due to an invalid password. If this predicate is `nil`, an HTTP 401 error indicates an invalid credential.

## See Also

- [var accountDisplayName: String?](asauthorizationproviderextensionloginconfiguration/accountdisplayname.md)
  The display name for the account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/invalidcredentialpredicate)*