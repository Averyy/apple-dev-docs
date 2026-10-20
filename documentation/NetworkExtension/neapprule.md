# NEAppRule

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

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

```objc
@interface NEAppRule : NSObject
```

## Topics

### Initializing an app rule
- [init(signingIdentifier: String)](./neapprule/init%28signingidentifier%29.md)
  Create an app rule that matches an app with a given signing identifier.
- [init(signingIdentifier: String, designatedRequirement: String)](./neapprule/init%28signingidentifier,designatedrequirement%29.md)
  Create an app rule that matches an app with a given signing identifier and a given designated requirement.
### Accessing app rule properties
- [var matchSigningIdentifier: String](./neapprule/matchsigningidentifier.md)
  The signing identifier of the app that matches the rule.
- [var matchDesignatedRequirement: String](./neapprule/matchdesignatedrequirement.md)
  The designated requirement of the app that matches the rule.
- [var matchPath: String?](./neapprule/matchpath.md)
  The file system path of the app that matches the rule.
- [var matchDomains: [Any]?](./neapprule/matchdomains.md)
  The hostname domains that match the rule.
- [var matchTools: [NEAppRule]?](./neapprule/matchtools.md)
  An array of app rule objects that restrict the rule so it only matches network traffic generated from helper processes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### VPN configuration
- [class NEAppProxyProviderManager](./neappproxyprovidermanager.md)
  An object to create and manage the app proxy provider’s VPN configuration.
- [class NETunnelProviderManager](./netunnelprovidermanager.md)
  An object to create and manage the tunnel provider’s VPN configuration.
- [class NEVPNManager](./nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
- [class NETunnelProviderProtocol](./netunnelproviderprotocol.md)
  Configuration parameters for a VPN tunnel.
- [VPN On Demand Rules](./vpn-on-demand-rules.md)
  Set up VPN On Demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule)*