# PluginNetworkPermissionScope

**Framework**: PackageDescription  
**Kind**: enum  
**Role**: Enumeration

The scope of a network permission.

**Availability**:
- SwiftPM 5.9+

## Declaration

```swift
enum PluginNetworkPermissionScope
```

## Overview

The scope can be none, local connections only, or all connections.

## Topics

### Enumeration Cases
- [PluginNetworkPermissionScope.all(ports:)](./pluginnetworkpermissionscope/all%28ports%29-swift.enum.case.md)
  Allow local and outgoing network connections; can be limited to a list of allowed ports.
- [PluginNetworkPermissionScope.docker](./pluginnetworkpermissionscope/docker.md)
  Allow connections to Docker through UNIX domain sockets.
- [PluginNetworkPermissionScope.local(ports:)](./pluginnetworkpermissionscope/local%28ports%29-swift.enum.case.md)
  Allow local network connections; can be limited to a list of allowed ports.
- [PluginNetworkPermissionScope.none](./pluginnetworkpermissionscope/none.md)
  Do not allow network access.
- [PluginNetworkPermissionScope.unixDomainSocket](./pluginnetworkpermissionscope/unixdomainsocket.md)
  Allow connections to any UNIX domain socket.
### Type Methods
- [static func all(ports: Range<Int>) -> PluginNetworkPermissionScope](./pluginnetworkpermissionscope/all%28ports%29-swift.type.method.md)
  Allow local and outgoing network connections, limited to a range of allowed ports.
- [static func local(ports: Range<Int>) -> PluginNetworkPermissionScope](./pluginnetworkpermissionscope/local%28ports%29-swift.type.method.md)
  Allow local network connections, limited to a range of allowed ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/pluginnetworkpermissionscope)*