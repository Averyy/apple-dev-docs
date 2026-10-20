# strictRevocationCheck

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

Require a “not revoked” result when checking if the certificate identifying the server is revoked.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var strictRevocationCheck: Bool { get set }
```

```objc
@property BOOL strictRevocationCheck;
```

#### Discussion

The default value is NO. If this property is set to NO, then either a “not revoked” result from the certificate revocation server or a failure to communicate with the certificate revocation server will result in a successful revocation check. If this property is set to YES, then only a “not revoked” result from the certificate revocation server will result in a successful revocation check.

## See Also

### Accessing other IKEv2 properties
- [var deadPeerDetectionRate: NEVPNIKEv2DeadPeerDetectionRate](./deadpeerdetectionrate.md)
  The frequency at which the IKEv2 client will run the dead peer detection algorithm.
- [enum NEVPNIKEv2DeadPeerDetectionRate](../nevpnikev2deadpeerdetectionrate.md)
  An enumeration of values for the frequency at which the IKEv2 client runs the dead peer detection algorithm.
- [var useConfigurationAttributeInternalIPSubnet: Bool](./useconfigurationattributeinternalipsubnet.md)
  A Boolean indicating whether or not the IKEv2 client should use the INTERNAL_IP4_SUBNET and/or INTERNAL_IP6_SUBNET attributes sent by the IKEv2 server.
- [var disableMOBIKE: Bool](./disablemobike.md)
  A Boolean indicating whether or not MOBIKE should be disabled for the IKEv2 sessions.
- [var disableRedirect: Bool](./disableredirect.md)
  A Boolean indicating whether or not IKEv2 server redirects are disabled.
- [var enablePFS: Bool](./enablepfs.md)
  A Boolean indicating whether or not Perfect Forward Secrecy is enabled.
- [var enableRevocationCheck: Bool](./enablerevocationcheck.md)
  Enable revocation checking of the IKEv2 server certificate.
- [var mtu: Int](./mtu.md)
  The Maximum Transmission Unit (MTU) size in bytes to assign to the tunnel interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/strictrevocationcheck)*