# mtu

**Framework**: Network Extension  
**Kind**: property

The Maximum Transmission Unit (MTU) size in bytes to assign to the tunnel interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var mtu: Int { get set }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/mtu)*