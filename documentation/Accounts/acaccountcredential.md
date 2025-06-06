# ACAccountCredential

**Framework**: Accounts  
**Kind**: class

A credential object that encapsulates the information needed to authenticate a user.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
class ACAccountCredential
```

#### Overview

To create an account credential that uses the OAuth open authentication standard, use the [`init(oAuthToken:tokenSecret:)`](acaccountcredential/init(oauthtoken:tokensecret:).md) method.

## Topics

### Initializing Credentials
- [init!(oAuthToken: String!, tokenSecret: String!)](acaccountcredential/init(oauthtoken:tokensecret:).md)
  Initializes an account credential using OAuth.
- [init!(oAuth2Token: String!, refreshToken: String!, expiryDate: Date!)](acaccountcredential/init(oauth2token:refreshtoken:expirydate:).md)
  Initializes an account credential using OAuth 2.
### Accessing Credential Properties
- [var oauthToken: String!](acaccountcredential/oauthtoken.md)
  The token used for the credential.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ACAccountStore](acaccountstore.md)
  The object you use to request, manage, and store the user’s account information.
- [class ACAccount](acaccount.md)
  The information associated with one of the user’s accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountcredential)*