# identityData

**Framework**: Network Extension  
**Kind**: property

The certificate and private key components of the tunneling protocol authentication credential, in PKCS12 format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var identityData: Data? { get set }
```

#### Discussion

In macOS, the system ignores this property for [`NEVPNProtocolIKEv2`](nevpnprotocolikev2.md) and [`NETunnelProviderProtocol`](netunnelproviderprotocol.md) objects. On iOS, the system ignores this property for [`NETunnelProviderProtocol`](netunnelproviderprotocol.md) objects. In cases where the system ignores this property, set the identity using the [`identityReference`](nevpnprotocol/identityreference.md) property.

## See Also

- [var username: String?](nevpnprotocol/username.md)
  The user name component of the tunneling protocol authentication credential.
- [var passwordReference: Data?](nevpnprotocol/passwordreference.md)
  A persistent keychain reference to a keychain item containing the password component of the tunneling protocol authentication credential.
- [var identityReference: Data?](nevpnprotocol/identityreference.md)
  A persistent keychain reference to a keychain item containing the certificate and private key components of the tunneling protocol authentication credential.
- [var identityDataPassword: String?](nevpnprotocol/identitydatapassword.md)
  The password for the PKCS12 tunneling protocol authentication credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/identitydata)*