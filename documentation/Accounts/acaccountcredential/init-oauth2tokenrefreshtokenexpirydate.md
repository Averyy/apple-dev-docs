# init(oAuth2Token:refreshToken:expiryDate:)

**Framework**: Accounts  
**Kind**: init

Initializes an account credential using OAuth 2.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
init!(oAuth2Token token: String!, refreshToken: String!, expiryDate: Date!)
```

#### Discussion

Accounts can optionally use the OAuth open authentication standard to authenticate your client application. Instead of the user giving their username and password to log in, the server authenticates the user, and your client application receives a token that grants it access to specific resources for a defined duration. The authentication mechanism uses a key and secret scheme similar to the public and private keys used by `ssh`. A token is a unique, random string of letters and numbers that’s paired with a secret to protect the token from being abused. You initialize account credentials using this token and secret token.

To learn more about OAuth, go to [`OAuth`](https://developer.apple.comhttp://oauth.net).

## Parameters

- `token`: The client application’s token.
- `refreshToken`: The client application’s refresh token.
- `expiryDate`: The date the token expires.

## See Also

- [init!(oAuthToken: String!, tokenSecret: String!)](acaccountcredential/init(oauthtoken:tokensecret:).md)
  Initializes an account credential using OAuth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountcredential/init(oauth2token:refreshtoken:expirydate:))*