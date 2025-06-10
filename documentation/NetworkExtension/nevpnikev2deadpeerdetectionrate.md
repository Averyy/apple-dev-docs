# NEVPNIKEv2DeadPeerDetectionRate

**Framework**: Network Extension  
**Kind**: enum

An enumeration of values for the frequency at which the IKEv2 client runs the dead peer detection algorithm.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEVPNIKEv2DeadPeerDetectionRate
```

## Topics

### Detection rates
- [NEVPNIKEv2DeadPeerDetectionRate.none](nevpnikev2deadpeerdetectionrate/none.md)
  Do not perform dead peer detection.
- [NEVPNIKEv2DeadPeerDetectionRate.low](nevpnikev2deadpeerdetectionrate/low.md)
  Run dead peer detection once every 30 minutes. If the peer does not respond, retry 5 times at 1 second intervals before declaring the peer dead and terminating the session.
- [NEVPNIKEv2DeadPeerDetectionRate.medium](nevpnikev2deadpeerdetectionrate/medium.md)
  Run dead peer detection once every 10 minutes. If the peer does not respond, retry 5 times at 1 second intervals before declaring the peer dead and terminating the session.
- [NEVPNIKEv2DeadPeerDetectionRate.high](nevpnikev2deadpeerdetectionrate/high.md)
  Run dead peer detection once every 1 minute. If the peer does not respond, retry 5 times at 1 second intervals before declaring the peer dead and terminating the session.
### Initializers
- [init?(rawValue: Int)](nevpnikev2deadpeerdetectionrate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var deadPeerDetectionRate: NEVPNIKEv2DeadPeerDetectionRate](nevpnprotocolikev2/deadpeerdetectionrate.md)
  The frequency at which the IKEv2 client will run the dead peer detection algorithm.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2deadpeerdetectionrate)*