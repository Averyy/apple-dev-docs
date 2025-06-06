# NEVPNProtocol

**Framework**: Network Extension  
**Kind**: class

Settings common to both IKEv2 and IPsec VPN configurations.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEVPNProtocol
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Overview

The [`NEVPNProtocol`](nevpnprotocol.md) class is an abstract base class with one subclass for each type of supported VPN configuration. This class provides properties for configuring the VPN, authenticating network connections, and routing network traffic. You can include all network traffic, with some exceptions, and selectively exclude types of network traffic.

Instances of this class are thread-safe.

## Topics

### Configuring the VPN
- [var serverAddress: String?](nevpnprotocol/serveraddress.md)
  The address of the VPN server.
- [var disconnectOnSleep: Bool](nevpnprotocol/disconnectonsleep.md)
  A Boolean value that indicates whether the VPN disconnects when the device sleeps.
- [var proxySettings: NEProxySettings?](nevpnprotocol/proxysettings.md)
  The proxy settings to use for HTTP and HTTPS connections that route through the VPN.
### Authenticating the user
- [var username: String?](nevpnprotocol/username.md)
  The user name component of the tunneling protocol authentication credential.
- [var passwordReference: Data?](nevpnprotocol/passwordreference.md)
  A persistent keychain reference to a keychain item containing the password component of the tunneling protocol authentication credential.
- [var identityReference: Data?](nevpnprotocol/identityreference.md)
  A persistent keychain reference to a keychain item containing the certificate and private key components of the tunneling protocol authentication credential.
- [var identityData: Data?](nevpnprotocol/identitydata.md)
  The certificate and private key components of the tunneling protocol authentication credential, in PKCS12 format.
- [var identityDataPassword: String?](nevpnprotocol/identitydatapassword.md)
  The password for the PKCS12 tunneling protocol authentication credentials.
### Routing network traffic
- [var includeAllNetworks: Bool](nevpnprotocol/includeallnetworks.md)
  A Boolean value that indicates whether the system sends most network traffic over the tunnel.
- [var excludeAPNs: Bool](nevpnprotocol/excludeapns.md)
  A Boolean value that indicates whether the system excludes all APNs network traffic from the tunnel.
- [var excludeCellularServices: Bool](nevpnprotocol/excludecellularservices.md)
  A Boolean value that indicates whether the system excludes all cellular services network traffic from the tunnel.
- [var excludeLocalNetworks: Bool](nevpnprotocol/excludelocalnetworks.md)
  A Boolean value that indicates whether the system excludes all traffic destined for local networks from the tunnel.
- [var enforceRoutes: Bool](nevpnprotocol/enforceroutes.md)
  A Boolean value that indicates whether route rules for the tunnel take precedence over any locally defined routes.
### Instance Properties
- [var excludeDeviceCommunication: Bool](nevpnprotocol/excludedevicecommunication.md)
- [var sliceUUID: String?](nevpnprotocol/sliceuuid.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NEDNSProxyProviderProtocol](nednsproxyproviderprotocol.md)
- [NETunnelProviderProtocol](netunnelproviderprotocol.md)
- [NEVPNProtocolIPSec](nevpnprotocolipsec.md)
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
- [class NEVPNProtocolIPSec](nevpnprotocolipsec.md)
  Settings for an IPsec VPN configuration.
- [VPN On Demand Rules](vpn-on-demand-rules.md)
  Set up VPN On Demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocol)*