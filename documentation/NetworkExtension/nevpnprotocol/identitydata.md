# identityData

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSData * identityData;
```

## Discussion

In macOS, the system ignores this property for [`NEVPNProtocolIKEv2`](../nevpnprotocolikev2.md) and [`NETunnelProviderProtocol`](../netunnelproviderprotocol.md) objects. On iOS, the system ignores this property for [`NETunnelProviderProtocol`](../netunnelproviderprotocol.md) objects. In cases where the system ignores this property, set the identity using the [`identityReference`](./identityreference.md) property.

## See Also

### Authenticating the user
- [var username: String?](./username.md)
  The user name component of the tunneling protocol authentication credential.
- [var passwordReference: Data?](./passwordreference.md)
  A persistent keychain reference to a keychain item containing the password component of the tunneling protocol authentication credential.
- [var identityReference: Data?](./identityreference.md)
  A persistent keychain reference to a keychain item containing the certificate and private key components of the tunneling protocol authentication credential.
- [var identityDataPassword: String?](./identitydatapassword.md)
  The password for the PKCS12 tunneling protocol authentication credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol/identitydata)*