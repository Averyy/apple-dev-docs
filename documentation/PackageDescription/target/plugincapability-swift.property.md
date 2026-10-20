# pluginCapability

**Framework**: PackageDescription  
**Kind**: property  
**Role**: Instance Property

The capability provided by a package plug-in target.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
final var pluginCapability: Target.PluginCapability?
```

## See Also

### Creating a Plugin Target
- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, packageAccess: Bool) -> Target](./plugin%28name,capability,dependencies,path,exclude,sources,packageaccess%29.md)
  Defines a new package plug-in target.
- [Target.PluginCapability](./plugincapability-swift.enum.md)
  The different types of capability that a plug-in can provide.
- [enum PluginCommandIntent](../plugincommandintent.md)
  The intended use case of the command plug-in.
- [enum PluginPermission](../pluginpermission.md)
  The type of permission a plug-in requires.
- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?) -> Target](./plugin%28name,capability,dependencies,path,exclude,sources%29.md)
  Defines a new package plugin target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/plugincapability-swift.property)*