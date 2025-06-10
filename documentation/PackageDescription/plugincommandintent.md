# PluginCommandIntent

**Framework**: PackageDescription  
**Kind**: enum

The intended use case of the command plug-in.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
enum PluginCommandIntent
```

## Topics

### Creating a Command Intent
- [static func documentationGeneration() -> PluginCommandIntent](plugincommandintent/documentationgeneration.md)
  The plugin generates documentation.
- [static func sourceCodeFormatting() -> PluginCommandIntent](plugincommandintent/sourcecodeformatting.md)
  The plug-in formats source code.
- [case custom(verb: String, description: String)](plugincommandintent/custom(verb:description:).md)
  A custom command plug-in intent.
### Enumeration Cases
- [PluginCommandIntent.documentationGeneration](plugincommandintent/documentationgeneration.md)
  The plug-in generates documentation.
- [PluginCommandIntent.sourceCodeFormatting](plugincommandintent/sourcecodeformatting.md)
  The plug-in formats source code.

## See Also

- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, packageAccess: Bool) -> Target](target/plugin(name:capability:dependencies:path:exclude:sources:packageaccess:).md)
  Defines a new package plug-in target.
- [var pluginCapability: Target.PluginCapability?](target/plugincapability-swift.property.md)
  The capability provided by a package plug-in target.
- [Target.PluginCapability](target/plugincapability-swift.enum.md)
  The different types of capability that a plug-in can provide.
- [enum PluginPermission](pluginpermission.md)
  The type of permission a plug-in requires.
- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?) -> Target](target/plugin(name:capability:dependencies:path:exclude:sources:).md)
  Defines a new package plugin target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/plugincommandintent)*