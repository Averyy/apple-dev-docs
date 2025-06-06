# sharedSecretReference

**Framework**: Network Extension  
**Kind**: property

A persistent keychain reference to a keychain item containing the IKE shared secret.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var sharedSecretReference: Data? { get set }
```

#### Discussion

The persistent keychain reference must refer to a kerychain item of class [`kSecClassGenericPassword`](https://developer.apple.com/documentation/Security/kSecClassGenericPassword)

## See Also

- [var authenticationMethod: NEVPNIKEAuthenticationMethod](nevpnprotocolipsec/authenticationmethod.md)
  The method used to authenticate the device with the IPSec server. For IKE version 2, when using extended authentication, this authentication method only affects how the client validates the authentication payload presented by the server.
- [enum NEVPNIKEAuthenticationMethod](nevpnikeauthenticationmethod.md)
  Internet Key Exchange (IKE) authentication methods used to authenticate with the IPSec server.
- [var useExtendedAuthentication: Bool](nevpnprotocolipsec/useextendedauthentication.md)
  A flag indicating if extended authentication will be negotiated.
- [var localIdentifier: String?](nevpnprotocolipsec/localidentifier.md)
  A string identifying the iOS or macOS device for authentication purposes
- [var remoteIdentifier: String?](nevpnprotocolipsec/remoteidentifier.md)
  A string identifying the IPSec server for authentication purposes


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec/sharedsecretreference)*