# NETunnelProviderProtocol

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

Configuration parameters for a VPN tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NETunnelProviderProtocol
```

```objc
@interface NETunnelProviderProtocol : NEVPNProtocol
```

## Overview

`NETunnelProviderProtocol` objects are used to specify configuration parameters for Tunnel Provider extensions.

## Topics

### Accessing the tunnel configuration
- [var providerConfiguration: [String : Any]?](./netunnelproviderprotocol/providerconfiguration.md)
  A dictionary containing keys and values defined by the Tunnel Provider developer.
- [var providerBundleIdentifier: String?](./netunnelproviderprotocol/providerbundleidentifier.md)
  A string identifying the specific Tunnel Provider extension that should be used with this configuration.

## Relationships

### Inherits From
- [NEVPNProtocol](./nevpnprotocol.md)
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
- [class NEAppRule](./neapprule.md)
  The identity of an app whose traffic is to be routed through the tunnel.
- [VPN On Demand Rules](./vpn-on-demand-rules.md)
  Set up VPN On Demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelproviderprotocol)*