# nonce

**Framework**: SigninwithAppleJS  
**Kind**: property  
**Role**: Instance Property

The value that associates a client session and an ID token.

**Availability**:
- Sign in with Apple JS 1.3.1+

## Declaration

```
attribute string nonce;
```

#### Discussion

This value mitigates replay attacks and is present only if passed during the authorization request.

## See Also

### Configuring the client object
- [clientId](./clientid.md)
  The developer’s client identifier, as provided by WWDR.
- [redirectURI](./redirecturi.md)
  The URI to which the authorization redirects.
- [scope](./scope.md)
  The amount of user information requested from Apple.
- [state](./state.md)
  The current state of the request.
- [usePopup](./usepopup.md)
  A Boolean that enables showing the flow in a popup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs/clientconfigi/nonce)*