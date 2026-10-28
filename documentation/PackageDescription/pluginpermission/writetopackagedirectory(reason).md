# PluginPermission.writeToPackageDirectory(reason:)

**Framework**: PackageDescription  
**Kind**: case  
**Role**: Case

Create a permission to modify files in the package’s directory.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
case writeToPackageDirectory(reason: String)
```

## Discussion

The command plug-in requires permission to modify the files under the package directory. The `reason` string is shown to the user at the time of request for approval, explaining why the plug-in requests access.

## Parameters

- `reason`: A reason why the permission is needed. This is shown to the user when permission is sought.

## See Also

### Create a permission
- [case allowNetworkConnections(scope: PluginNetworkPermissionScope, reason: String)](./allownetworkconnections%28scope,reason%29.md)
  Create a permission to make network connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/pluginpermission/writetopackagedirectory(reason:))*