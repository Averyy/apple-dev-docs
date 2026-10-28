# redirectURI

**Framework**: SigninwithAppleJS  
**Kind**: property  
**Role**: Instance Property

The URI to which the authorization redirects.

**Availability**:
- Sign in with Apple JS 1.0+

## Declaration

```
attribute string redirectURI;
```

## Mentions

- [Configuring your webpage for Sign in with Apple](../../SigninwithApple/configuring-your-webpage-for-sign-in-with-apple.md)
- [Incorporating Sign in with Apple into other platforms](../../SigninwithApple/incorporating-sign-in-with-apple-into-other-platforms.md)

## Discussion

The URI provided must redirect to a website under your control. Supply this URI to WWDR to enable this feature.

## See Also

### Configuring the client object
- [clientId](./clientid.md)
  The developer’s client identifier, as provided by WWDR.
- [scope](./scope.md)
  The amount of user information requested from Apple.
- [state](./state.md)
  The current state of the request.
- [nonce](./nonce.md)
  The value that associates a client session and an ID token.
- [usePopup](./usepopup.md)
  A Boolean that enables showing the flow in a popup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs/clientconfigi/redirecturi)*