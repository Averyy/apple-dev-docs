# NEAppRule

**Framework**: Network Extension  
**Kind**: class

The identity of an app whose traffic is to be routed through the tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class NEAppRule
```

## Topics

### Initializing an app rule
- [init(signingIdentifier: String)](neapprule/init(signingidentifier:).md)
  Create an app rule that matches an app with a given signing identifier.
- [init(signingIdentifier: String, designatedRequirement: String)](neapprule/init(signingidentifier:designatedrequirement:).md)
  Create an app rule that matches an app with a given signing identifier and a given designated requirement.
### Accessing app rule properties
- [var matchSigningIdentifier: String](neapprule/matchsigningidentifier.md)
  The signing identifier of the app that matches the rule.
- [var matchDesignatedRequirement: String](neapprule/matchdesignatedrequirement.md)
  The designated requirement of the app that matches the rule.
- [var matchPath: String?](neapprule/matchpath.md)
  The file system path of the app that matches the rule.
- [var matchDomains: [Any]?](neapprule/matchdomains.md)
  The hostname domains that match the rule.
- [var matchTools: [NEAppRule]?](neapprule/matchtools.md)
  An array of app rule objects that restrict the rule so it only matches network traffic generated from helper processes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [class NEAppProxyProviderManager](neappproxyprovidermanager.md)
  An object to create and manage the app proxy provider’s VPN configuration.
- [class NETunnelProviderManager](netunnelprovidermanager.md)
  An object to create and manage the tunnel provider’s VPN configuration.
- [class NEVPNManager](nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
- [class NETunnelProviderProtocol](netunnelproviderprotocol.md)
  Configuration parameters for a VPN tunnel.
- [VPN On Demand Rules](vpn-on-demand-rules.md)
  Set up VPN On Demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule)*