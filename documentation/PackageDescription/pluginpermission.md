# PluginPermission

**Framework**: PackageDescription  
**Kind**: enum

The type of permission a plug-in requires.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
enum PluginPermission
```

#### Overview

Supported types are [`PluginPermission.allowNetworkConnections(scope:reason:)`](pluginpermission/allownetworkconnections(scope:reason:).md) and [`PluginPermission.writeToPackageDirectory(reason:)`](pluginpermission/writetopackagedirectory(reason:).md).

## Topics

### Create a permission
- [case allowNetworkConnections(scope: PluginNetworkPermissionScope, reason: String)](pluginpermission/allownetworkconnections(scope:reason:).md)
  Create a permission to make network connections.
- [PluginPermission.writeToPackageDirectory(reason:)](pluginpermission/writetopackagedirectory(reason:).md)
  Create a permission to modify files in the package’s directory.
### Allow network connection
- [enum PluginNetworkPermissionScope](pluginnetworkpermissionscope.md)
  The scope of a network permission.

## See Also

- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, packageAccess: Bool) -> Target](target/plugin(name:capability:dependencies:path:exclude:sources:packageaccess:).md)
  Defines a new package plug-in target.
- [var pluginCapability: Target.PluginCapability?](target/plugincapability-swift.property.md)
  The capability provided by a package plug-in target.
- [Target.PluginCapability](target/plugincapability-swift.enum.md)
  The different types of capability that a plug-in can provide.
- [enum PluginCommandIntent](plugincommandintent.md)
  The intended use case of the command plug-in.
- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?) -> Target](target/plugin(name:capability:dependencies:path:exclude:sources:).md)
  Defines a new package plugin target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/pluginpermission)*