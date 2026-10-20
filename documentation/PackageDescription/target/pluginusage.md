# Target.PluginUsage

**Framework**: PackageDescription  
**Kind**: enum  
**Role**: Enumeration

A plug-in used in a target.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
enum PluginUsage
```

## Topics

### Creating a Plugin Usage
- [static func plugin(name: String) -> Target.PluginUsage](./pluginusage/plugin%28name%29.md)
  Specifies use of a plugin target in the same package.
- [case plugin(name: String, package: String?)](./pluginusage/plugin%28name,package%29.md)
  Specifies the use of a plug-in product in a package dependency.
### Default Implementations
- [ExpressibleByStringLiteral Implementations](./pluginusage/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)

## See Also

### Configuring the Target
- [var cSettings: [CSetting]?](./csettings.md)
  The target’s C build settings.
- [var cxxSettings: [CXXSetting]?](./cxxsettings.md)
  The target’s C++ build settings.
- [var swiftSettings: [SwiftSetting]?](./swiftsettings.md)
  The target’s Swift build settings.
- [var linkerSettings: [LinkerSetting]?](./linkersettings.md)
  The target’s linker settings.
- [var plugins: [Target.PluginUsage]?](./plugins.md)
  The uses of package plug-ins by the target.
- [struct BuildConfiguration](../buildconfiguration.md)
  The build configuration, such as debug or release.
- [struct BuildSettingCondition](../buildsettingcondition.md)
  A condition that limits the application of a build setting.
- [struct CSetting](../csetting.md)
  A C language build setting.
- [struct CXXSetting](../cxxsetting.md)
  A CXX-language build setting.
- [struct SwiftSetting](../swiftsetting.md)
  A Swift language build setting.
- [struct LinkerSetting](../linkersetting.md)
  A linker build setting.
- [let packageAccess: Bool](./packageaccess.md)
  If true, access to package declarations from other targets in the package is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/pluginusage)*