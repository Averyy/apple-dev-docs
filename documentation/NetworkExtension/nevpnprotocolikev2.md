# NEVPNProtocolIKEv2

**Framework**: Network Extension  
**Kind**: class

Settings for an IKEv2 VPN configuration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEVPNProtocolIKEv2
```

#### Overview

Instances of this class are thread safe.

## Topics

### Accessing IKEv2 Security Association parameters
- [var ikeSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters](nevpnprotocolikev2/ikesecurityassociationparameters.md)
  An [`NEVPNIKEv2SecurityAssociationParameters`](nevpnikev2securityassociationparameters.md) object containing the parameters for the initial IKE security association to be negotiated with the IKEv2 server.
- [var childSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters](nevpnprotocolikev2/childsecurityassociationparameters.md)
  An [`NEVPNIKEv2SecurityAssociationParameters`](nevpnikev2securityassociationparameters.md) object containing the parameters for the child IPSec security associations to be negotiated for each IKEv2 policy.
- [class NEVPNIKEv2SecurityAssociationParameters](nevpnikev2securityassociationparameters.md)
  Parameters for an IKEv2 Security Association.
### Accessing certificate properties
- [var serverCertificateIssuerCommonName: String?](nevpnprotocolikev2/servercertificateissuercommonname.md)
  A string containing the value of the Subject Common Name field of the Certificate Authority certificate that issued the IKEv2 server’s certificate.
- [var serverCertificateCommonName: String?](nevpnprotocolikev2/servercertificatecommonname.md)
  A string containing the value of the Subject Common Name field of the IKEv2 server’s certificate.
- [var certificateType: NEVPNIKEv2CertificateType](nevpnprotocolikev2/certificatetype.md)
  The type of the certificate in the identity configured in `identityReference` or `identityData`.
- [enum NEVPNIKEv2CertificateType](nevpnikev2certificatetype.md)
  An enumeration of certificate type values.
### Accessing TLS version properties
- [var minimumTLSVersion: NEVPNIKEv2TLSVersion](nevpnprotocolikev2/minimumtlsversion.md)
  The minimum TLS version to allow for EAP-TLS authentication.
- [var maximumTLSVersion: NEVPNIKEv2TLSVersion](nevpnprotocolikev2/maximumtlsversion.md)
  The minimum TLS version to allow for EAP-TLS authentication.
- [enum NEVPNIKEv2TLSVersion](nevpnikev2tlsversion.md)
  An enumeration of TLS Versions for use in EAP-TLS.
### Accessing other IKEv2 properties
- [var deadPeerDetectionRate: NEVPNIKEv2DeadPeerDetectionRate](nevpnprotocolikev2/deadpeerdetectionrate.md)
  The frequency at which the IKEv2 client will run the dead peer detection algorithm.
- [enum NEVPNIKEv2DeadPeerDetectionRate](nevpnikev2deadpeerdetectionrate.md)
  An enumeration of values for the frequency at which the IKEv2 client runs the dead peer detection algorithm.
- [var useConfigurationAttributeInternalIPSubnet: Bool](nevpnprotocolikev2/useconfigurationattributeinternalipsubnet.md)
  A Boolean indicating whether or not the IKEv2 client should use the INTERNAL_IP4_SUBNET and/or INTERNAL_IP6_SUBNET attributes sent by the IKEv2 server.
- [var disableMOBIKE: Bool](nevpnprotocolikev2/disablemobike.md)
  A Boolean indicating whether or not MOBIKE should be disabled for the IKEv2 sessions.
- [var disableRedirect: Bool](nevpnprotocolikev2/disableredirect.md)
  A Boolean indicating whether or not IKEv2 server redirects are disabled.
- [var enablePFS: Bool](nevpnprotocolikev2/enablepfs.md)
  A Boolean indicating whether or not Perfect Forward Secrecy is enabled.
- [var enableRevocationCheck: Bool](nevpnprotocolikev2/enablerevocationcheck.md)
  Enable revocation checking of the IKEv2 server certificate.
- [var strictRevocationCheck: Bool](nevpnprotocolikev2/strictrevocationcheck.md)
  Require a “not revoked” result when checking if the certificate identifying the server is revoked.
- [var mtu: Int](nevpnprotocolikev2/mtu.md)
  The Maximum Transmission Unit (MTU) size in bytes to assign to the tunnel interface.
### Supporting Wi-Fi assist
- [var enableFallback: Bool](nevpnprotocolikev2/enablefallback.md)
  A property to enable the use of cellular data when Wi-Fi connectivity is poor.
### Instance Properties
- [var allowPostQuantumKeyExchangeFallback: Bool](nevpnprotocolikev2/allowpostquantumkeyexchangefallback.md)
- [var ppkConfiguration: NEVPNIKEv2PPKConfiguration?](nevpnprotocolikev2/ppkconfiguration.md)

## Relationships

### Inherits From
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
- [class NEVPNProtocolIPSec](nevpnprotocolipsec.md)
  Settings for an IPsec VPN configuration.
- [class NEVPNProtocol](nevpnprotocol.md)
  Settings common to both IKEv2 and IPsec VPN configurations.
- [VPN On Demand Rules](vpn-on-demand-rules.md)
  Set up VPN On Demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2)*