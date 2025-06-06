# Target.PluginUsage.plugin(name:package:)

**Framework**: PackageDescription  
**Kind**: case

Specifies the use of a plug-in product in a package dependency.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
case plugin(name: String, package: String?)
```

## Parameters

- `name`: The name of the plug-in target.
- `package`: The name of the package that defines the plug-in target.

## See Also

- [static func plugin(name: String) -> Target.PluginUsage](target/pluginusage/plugin(name:).md)
  Specifies use of a plugin target in the same package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/pluginusage/plugin(name:package:))*