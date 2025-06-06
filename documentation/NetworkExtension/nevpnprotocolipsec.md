# NEVPNProtocolIPSec

**Framework**: Network Extension  
**Kind**: class

Settings for an IPsec VPN configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEVPNProtocolIPSec
```

#### Overview

To configure IKE version 2 (IKEv2), use the [`NEVPNProtocolIKEv2`](nevpnprotocolikev2.md) subclass. Instantiating [`NEVPNProtocolIPSec`](nevpnprotocolipsec.md) directly implies IKE version 1.

## Topics

### Accessing IPSec properties
- [var authenticationMethod: NEVPNIKEAuthenticationMethod](nevpnprotocolipsec/authenticationmethod.md)
  The method used to authenticate the device with the IPSec server. For IKE version 2, when using extended authentication, this authentication method only affects how the client validates the authentication payload presented by the server.
- [enum NEVPNIKEAuthenticationMethod](nevpnikeauthenticationmethod.md)
  Internet Key Exchange (IKE) authentication methods used to authenticate with the IPSec server.
- [var useExtendedAuthentication: Bool](nevpnprotocolipsec/useextendedauthentication.md)
  A flag indicating if extended authentication will be negotiated.
- [var sharedSecretReference: Data?](nevpnprotocolipsec/sharedsecretreference.md)
  A persistent keychain reference to a keychain item containing the IKE shared secret.
- [var localIdentifier: String?](nevpnprotocolipsec/localidentifier.md)
  A string identifying the iOS or macOS device for authentication purposes
- [var remoteIdentifier: String?](nevpnprotocolipsec/remoteidentifier.md)
  A string identifying the IPSec server for authentication purposes

## Relationships

### Inherits From
- [NEVPNProtocol](nevpnprotocol.md)
### Inherited By
- [NEVPNProtocolIKEv2](nevpnprotocolikev2.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NEVPNManager](nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
- [class NEVPNProtocolIKEv2](nevpnprotocolikev2.md)
  Settings for an IKEv2 VPN configuration.
- [class NEVPNProtocol](nevpnprotocol.md)
  Settings common to both IKEv2 and IPsec VPN configurations.
- [VPN On Demand Rules](vpn-on-demand-rules.md)
  Set up VPN On Demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolipsec)*