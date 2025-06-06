# useExtendedAuthentication

**Framework**: Network Extension  
**Kind**: property

A flag indicating if extended authentication will be negotiated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var useExtendedAuthentication: Bool { get set }
```

#### Discussion

This authentication is in addition to the IKE authentication used to authenticate the endpoints of the IKE session.

- For IKE version 1, when this flag is set X-Auth authentication will be negotiated as part of the IKE session, using the `username` and `passwordReference` properties as the credential.
- For IKE version 2, when this flag is set EAP authentication will be negotiated as part of the IKE session, using the `username`, `passwordReference`, and/or `identityReference` properties as the credential depending on which EAP method the server requires.

## See Also

- [var authenticationMethod: NEVPNIKEAuthenticationMethod](nevpnprotocolipsec/authenticationmethod.md)
  The method used to authenticate the device with the IPSec server. For IKE version 2, when using extended authentication, this authentication method only affects how the client validates the authentication payload presented by the server.
- [enum NEVPNIKEAuthenticationMethod](nevpnikeauthenticationmethod.md)
  Internet Key Exchange (IKE) authentication methods used to authenticate with the IPSec server.
- [var sharedSecretReference: Data?](nevpnprotocolipsec/sharedsecretreference.md)
  A persistent keychain reference to a keychain item containing the IKE shared secret.
- [var localIdentifier: String?](nevpnprotocolipsec/localidentifier.md)
  A string identifying the iOS or macOS device for authentication purposes
- [var remoteIdentifier: String?](nevpnprotocolipsec/remoteidentifier.md)
  A string identifying the IPSec server for authentication purposes


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec/useextendedauthentication)*