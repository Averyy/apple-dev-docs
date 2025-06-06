# disableRedirect

**Framework**: Network Extension  
**Kind**: property

A Boolean indicating whether or not IKEv2 server redirects are disabled.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var disableRedirect: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var deadPeerDetectionRate: NEVPNIKEv2DeadPeerDetectionRate](nevpnprotocolikev2/deadpeerdetectionrate.md)
  The frequency at which the IKEv2 client will run the dead peer detection algorithm.
- [enum NEVPNIKEv2DeadPeerDetectionRate](nevpnikev2deadpeerdetectionrate.md)
  An enumeration of values for the frequency at which the IKEv2 client runs the dead peer detection algorithm.
- [var useConfigurationAttributeInternalIPSubnet: Bool](nevpnprotocolikev2/useconfigurationattributeinternalipsubnet.md)
  A Boolean indicating whether or not the IKEv2 client should use the INTERNAL_IP4_SUBNET and/or INTERNAL_IP6_SUBNET attributes sent by the IKEv2 server.
- [var disableMOBIKE: Bool](nevpnprotocolikev2/disablemobike.md)
  A Boolean indicating whether or not MOBIKE should be disabled for the IKEv2 sessions.
- [var enablePFS: Bool](nevpnprotocolikev2/enablepfs.md)
  A Boolean indicating whether or not Perfect Forward Secrecy is enabled.
- [var enableRevocationCheck: Bool](nevpnprotocolikev2/enablerevocationcheck.md)
  Enable revocation checking of the IKEv2 server certificate.
- [var strictRevocationCheck: Bool](nevpnprotocolikev2/strictrevocationcheck.md)
  Require a “not revoked” result when checking if the certificate identifying the server is revoked.
- [var mtu: Int](nevpnprotocolikev2/mtu.md)
  The Maximum Transmission Unit (MTU) size in bytes to assign to the tunnel interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/disableredirect)*