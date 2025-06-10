# Target.PluginCapability

**Framework**: PackageDescription  
**Kind**: enum

The different types of capability that a plug-in can provide.

## Declaration

```swift
enum PluginCapability
```

#### Overview

In this version of SwiftPM, only build tool and command plug-ins are supported; this enumeration will be extended as new plug-in capabilities are added.

## Topics

### Creating a Plugin Capability
- [static func buildTool() -> Target.PluginCapability](target/plugincapability-swift.enum/buildtool.md)
  The plug-in is a build tool.
- [case command(intent: PluginCommandIntent, permissions: [PluginPermission])](target/plugincapability-swift.enum/command(intent:permissions:).md)
  Specifies that the plug-in provides a user command capability.
### Enumeration Cases
- [Target.PluginCapability.buildTool](target/plugincapability-swift.enum/buildtool.md)
  Specifies that the plug-in provides a build tool capability.

## See Also

- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, packageAccess: Bool) -> Target](target/plugin(name:capability:dependencies:path:exclude:sources:packageaccess:).md)
  Defines a new package plug-in target.
- [var pluginCapability: Target.PluginCapability?](target/plugincapability-swift.property.md)
  The capability provided by a package plug-in target.
- [enum PluginCommandIntent](plugincommandintent.md)
  The intended use case of the command plug-in.
- [enum PluginPermission](pluginpermission.md)
  The type of permission a plug-in requires.
- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?) -> Target](target/plugin(name:capability:dependencies:path:exclude:sources:).md)
  Defines a new package plugin target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/plugincapability-swift.enum)*