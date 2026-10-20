# childSecurityAssociationParameters

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An [`NEVPNIKEv2SecurityAssociationParameters`](../nevpnikev2securityassociationparameters.md) object containing the parameters for the child IPSec security associations to be negotiated for each IKEv2 policy.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var childSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters { get }
```

```objc
@property (readonly) NEVPNIKEv2SecurityAssociationParameters * childSecurityAssociationParameters;
```

## See Also

### Accessing IKEv2 Security Association parameters
- [var ikeSecurityAssociationParameters: NEVPNIKEv2SecurityAssociationParameters](./ikesecurityassociationparameters.md)
  An [`NEVPNIKEv2SecurityAssociationParameters`](../nevpnikev2securityassociationparameters.md) object containing the parameters for the initial IKE security association to be negotiated with the IKEv2 server.
- [class NEVPNIKEv2SecurityAssociationParameters](../nevpnikev2securityassociationparameters.md)
  Parameters for an IKEv2 Security Association.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/childsecurityassociationparameters)*