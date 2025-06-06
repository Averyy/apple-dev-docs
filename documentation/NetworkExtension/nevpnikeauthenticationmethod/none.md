# NEVPNIKEAuthenticationMethod.none

**Framework**: Network Extension  
**Kind**: case

Do not authenticate with the IPSec server. Note that extended authentication may still be performed if the [`useExtendedAuthentication`](nevpnprotocolipsec/useextendedauthentication.md) property is set. This value is only valid for IKE version 2 (IKEv2)

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

## See Also

- [NEVPNIKEAuthenticationMethod.certificate](nevpnikeauthenticationmethod/certificate.md)
  Use a certificate and private key as the authentication credential. The certificate and private key set in the [`identityReference`](nevpnprotocol/identityreference.md) or [`identityData`](nevpnprotocol/identitydata.md) property will be used.
- [NEVPNIKEAuthenticationMethod.sharedSecret](nevpnikeauthenticationmethod/sharedsecret.md)
  Use a shared secret as the authentication credential. The shared secret set in the [`sharedSecretReference`](nevpnprotocolipsec/sharedsecretreference.md) property will be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikeauthenticationmethod/none)*