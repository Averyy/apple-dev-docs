# ACAccountCredential

**Framework**: Accounts  
**Kind**: class  
**Role**: Class

A credential object that encapsulates the information needed to authenticate a user.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
class ACAccountCredential
```

```objc
@interface ACAccountCredential : NSObject
```

## Overview

To create an account credential that uses the OAuth open authentication standard, use the [`init(oAuthToken:tokenSecret:)`](./acaccountcredential/init%28oauthtoken,tokensecret%29-6bfyf.md) method.

## Topics

### Initializing Credentials
- [init!(oAuthToken: String!, tokenSecret: String!)](./acaccountcredential/init%28oauthtoken,tokensecret%29-6bfyf.md)
  Initializes an account credential using OAuth.
- [init!(oAuth2Token: String!, refreshToken: String!, expiryDate: Date!)](./acaccountcredential/init%28oauth2token,refreshtoken,expirydate%29-67hmd.md)
  Initializes an account credential using OAuth 2.
### Accessing Credential Properties
- [var oauthToken: String!](./acaccountcredential/oauthtoken.md)
  The token used for the credential.
### Initializers
- [init!(OAuth2Token: String!, refreshToken: String!, expiryDate: Date!)](./acaccountcredential/init%28oauth2token,refreshtoken,expirydate%29-8r1ys.md)
- [init!(OAuthToken: String!, tokenSecret: String!)](./acaccountcredential/init%28oauthtoken,tokensecret%29-6328w.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Account Management
- [class ACAccountStore](./acaccountstore.md)
  The object you use to request, manage, and store the user’s account information.
- [class ACAccount](./acaccount.md)
  The information associated with one of the user’s accounts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountcredential)*