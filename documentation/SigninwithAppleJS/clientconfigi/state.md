# state

**Framework**: SigninwithAppleJS  
**Kind**: property  
**Role**: Instance Property

The current state of the request.

**Availability**:
- Sign in with Apple JS 1.0+

## Declaration

```
attribute string state;
```

#### Discussion

You create and send this property to Apple, and Apple returns it during authentication. Provide information about the state of your app inside of the property, such as “Initial user authentication request”. Use this property to help authenticate the returned response by comparing Apple’s response to the state you sent.

## See Also

### Configuring the client object
- [clientId](./clientid.md)
  The developer’s client identifier, as provided by WWDR.
- [redirectURI](./redirecturi.md)
  The URI to which the authorization redirects.
- [scope](./scope.md)
  The amount of user information requested from Apple.
- [nonce](./nonce.md)
  The value that associates a client session and an ID token.
- [usePopup](./usepopup.md)
  A Boolean that enables showing the flow in a popup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplejs/clientconfigi/state)*