# Target.PluginCapability

**Framework**: PackageDescription  
**Kind**: enum  
**Role**: Enumeration

The different types of capability that a plug-in can provide.

## Declaration

```swift
enum PluginCapability
```

#### Overview

In this version of SwiftPM, only build tool and command plug-ins are supported; this enumeration will be extended as new plug-in capabilities are added.

## Topics

### Creating a Plugin Capability
- [static func buildTool() -> Target.PluginCapability](./plugincapability-swift.enum/buildtool%28%29.md)
  The plug-in is a build tool.
- [case command(intent: PluginCommandIntent, permissions: [PluginPermission])](./plugincapability-swift.enum/command%28intent,permissions%29.md)
  Specifies that the plug-in provides a user command capability.
### Enumeration Cases
- [Target.PluginCapability.buildTool](./plugincapability-swift.enum/buildtool.md)
  Specifies that the plug-in provides a build tool capability.

## See Also

### Creating a Plugin Target
- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, packageAccess: Bool) -> Target](./plugin%28name,capability,dependencies,path,exclude,sources,packageaccess%29.md)
  Defines a new package plug-in target.
- [var pluginCapability: Target.PluginCapability?](./plugincapability-swift.property.md)
  The capability provided by a package plug-in target.
- [enum PluginCommandIntent](../plugincommandintent.md)
  The intended use case of the command plug-in.
- [enum PluginPermission](../pluginpermission.md)
  The type of permission a plug-in requires.
- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?) -> Target](./plugin%28name,capability,dependencies,path,exclude,sources%29.md)
  Defines a new package plugin target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/plugincapability-swift.enum)*