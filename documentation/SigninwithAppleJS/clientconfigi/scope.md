# scope

**Framework**: SigninwithAppleJS  
**Kind**: property  
**Role**: Instance Property

The amount of user information requested from Apple.

**Availability**:
- Sign in with Apple JS 1.0+

## Declaration

```
attribute string scope;
```

## Mentions

- [Configuring your webpage for Sign in with Apple](../../SigninwithApple/configuring-your-webpage-for-sign-in-with-apple.md)
- [Incorporating Sign in with Apple into other platforms](../../SigninwithApple/incorporating-sign-in-with-apple-into-other-platforms.md)

#### Discussion

You can request the user’s name or email. You can also choose to request both, or neither. Use space separation when requesting multiple scopes; for example, `"scope=name email"`.

## See Also

### Configuring the client object
- [clientId](./clientid.md)
  The developer’s client identifier, as provided by WWDR.
- [redirectURI](./redirecturi.md)
  The URI to which the authorization redirects.
- [state](./state.md)
  The current state of the request.
- [nonce](./nonce.md)
  The value that associates a client session and an ID token.
- [usePopup](./usepopup.md)
  A Boolean that enables showing the flow in a popup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs/clientconfigi/scope)*