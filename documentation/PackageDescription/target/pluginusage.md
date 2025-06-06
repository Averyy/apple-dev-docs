# Target.PluginUsage

**Framework**: PackageDescription  
**Kind**: enum

A plug-in used in a target.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
enum PluginUsage
```

## Topics

### Creating a Plugin Usage
- [static func plugin(name: String) -> Target.PluginUsage](target/pluginusage/plugin(name:).md)
  Specifies use of a plugin target in the same package.
- [case plugin(name: String, package: String?)](target/pluginusage/plugin(name:package:).md)
  Specifies the use of a plug-in product in a package dependency.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](target/pluginusage/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](target/pluginusage/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](target/pluginusage/expressiblebyunicodescalarliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)

## See Also

- [var cSettings: [CSetting]?](target/csettings.md)
  The target’s C build settings.
- [var cxxSettings: [CXXSetting]?](target/cxxsettings.md)
  The target’s C++ build settings.
- [var swiftSettings: [SwiftSetting]?](target/swiftsettings.md)
  The target’s Swift build settings.
- [var linkerSettings: [LinkerSetting]?](target/linkersettings.md)
  The target’s linker settings.
- [var plugins: [Target.PluginUsage]?](target/plugins.md)
  The uses of package plug-ins by the target.
- [struct BuildConfiguration](buildconfiguration.md)
  The build configuration, such as debug or release.
- [struct BuildSettingCondition](buildsettingcondition.md)
  A condition that limits the application of a build setting.
- [struct CSetting](csetting.md)
  A C language build setting.
- [struct CXXSetting](cxxsetting.md)
  A CXX-language build setting.
- [struct SwiftSetting](swiftsetting.md)
  A Swift language build setting.
- [struct LinkerSetting](linkersetting.md)
  A linker build setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/pluginusage)*