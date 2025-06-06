# plugin(name:)

**Framework**: PackageDescription  
**Kind**: method

Specifies use of a plugin target in the same package.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func plugin(name: String) -> Target.PluginUsage
```

#### Return Value

A `PluginUsage` instance.

## Parameters

- `name`: The name of the plugin target.

## See Also

- [case plugin(name: String, package: String?)](target/pluginusage/plugin(name:package:).md)
  Specifies the use of a plug-in product in a package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/pluginusage/plugin(name:))*