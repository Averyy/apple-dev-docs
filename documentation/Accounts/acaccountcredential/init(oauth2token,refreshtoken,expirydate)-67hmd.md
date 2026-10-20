# init(oAuth2Token:refreshToken:expiryDate:)

**Framework**: Accounts  
**Kind**: init  
**Role**: Initializer

Initializes an account credential using OAuth 2.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
init!(oAuth2Token token: String!, refreshToken: String!, expiryDate: Date!)
```

```objc
- (instancetype) initWithOAuth2Token:(NSString *) token refreshToken:(NSString *) refreshToken expiryDate:(NSDate *) expiryDate;
```

#### Discussion

Accounts can optionally use the OAuth open authentication standard to authenticate your client application. Instead of the user giving their username and password to log in, the server authenticates the user, and your client application receives a token that grants it access to specific resources for a defined duration. The authentication mechanism uses a key and secret scheme similar to the public and private keys used by `ssh`. A token is a unique, random string of letters and numbers that’s paired with a secret to protect the token from being abused. You initialize account credentials using this token and secret token.

To learn more about OAuth, go to [OAuth](http://oauth.net).

## Parameters

- `token`: The client application’s token.
- `refreshToken`: The client application’s refresh token.
- `expiryDate`: The date the token expires.

## See Also

### Initializing Credentials
- [init!(oAuthToken: String!, tokenSecret: String!)](./init%28oauthtoken,tokensecret%29-6bfyf.md)
  Initializes an account credential using OAuth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountcredential/init(oauth2token:refreshtoken:expirydate:)-67hmd)*