# init(oAuthToken:tokenSecret:)

**Framework**: Accounts  
**Kind**: init

Initializes an account credential using OAuth.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
init!(oAuthToken token: String!, tokenSecret secret: String!)
```

#### Return Value

Newly initialized account credential.

#### Discussion

Accounts can optionally use the OAuth open authentication standard to authenticate your client application. Instead of the user giving their username and password to log in, the server authenticates the user, and your client application receives a token that grants it access to specific resources for a defined duration. The authentication mechanism uses a key and secret scheme similar to the public and private keys used by `ssh`. A token is a unique, random string of letters and numbers that’s paired with a secret to protect the token from being abused. You initialize account credentials using this token and secret token.

To learn more about OAuth, go to [`OAuth`](https://developer.apple.comhttp://oauth.net).

## Parameters

- `token`: The client application’s token.
- `secret`: The client application’s secret token.

## See Also

- [init!(oAuth2Token: String!, refreshToken: String!, expiryDate: Date!)](acaccountcredential/init(oauth2token:refreshtoken:expirydate:).md)
  Initializes an account credential using OAuth 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountcredential/init(oauthtoken:tokensecret:))*