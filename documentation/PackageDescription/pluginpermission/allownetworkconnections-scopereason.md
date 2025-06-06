# PluginPermission.allowNetworkConnections(scope:reason:)

**Framework**: PackageDescription  
**Kind**: case

Create a permission to make network connections.

**Availability**:
- SwiftPM 5.9+

## Declaration

```swift
case allowNetworkConnections(scope: PluginNetworkPermissionScope, reason: String)
```

#### Discussion

The command plug-in requires permission to make network connections. The `reason` string is shown to the user at the time of request for approval, explaining why the plug-in is requesting access.

## Parameters

- `scope`: The scope of the permission.
- `reason`: A reason why the permission is needed. This is shown to the user when permission is sought.

## See Also

- [PluginPermission.writeToPackageDirectory(reason:)](pluginpermission/writetopackagedirectory(reason:).md)
  Create a permission to modify files in the package’s directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/pluginpermission/allownetworkconnections(scope:reason:))*