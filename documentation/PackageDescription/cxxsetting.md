# CXXSetting

**Framework**: PackageDescription  
**Kind**: struct

A CXX-language build setting.

## Declaration

```swift
struct CXXSetting
```

## Topics

### Configuring CXX Settings
- [static func define(String, to: String?, BuildSettingCondition?) -> CXXSetting](cxxsetting/define(_:to:_:).md)
  Defines a value for a macro.
- [static func headerSearchPath(String, BuildSettingCondition?) -> CXXSetting](cxxsetting/headersearchpath(_:_:).md)
  Provides a header search path relative to the target’s directory.
- [static func unsafeFlags([String], BuildSettingCondition?) -> CXXSetting](cxxsetting/unsafeflags(_:_:).md)
  Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.
### Type Methods
- [static func disableWarning(String, BuildSettingCondition?) -> CXXSetting](cxxsetting/disablewarning(_:_:).md)
  Disable a specific C++ compiler warning group.
- [static func enableWarning(String, BuildSettingCondition?) -> CXXSetting](cxxsetting/enablewarning(_:_:).md)
  Enable a specific C++ compiler warning group.
- [static func treatAllWarnings(as: WarningLevel, BuildSettingCondition?) -> CXXSetting](cxxsetting/treatallwarnings(as:_:).md)
  Controls how all C++ compiler warnings are treated during compilation.
- [static func treatWarning(String, as: WarningLevel, BuildSettingCondition?) -> CXXSetting](cxxsetting/treatwarning(_:as:_:).md)
  Controls how a specific C++ compiler warning is treated during compilation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct SwiftSetting](swiftsetting.md)
  A Swift language build setting.
- [struct LinkerSetting](linkersetting.md)
  A linker build setting.
- [Target.PluginUsage](target/pluginusage.md)
  A plug-in used in a target.
- [let packageAccess: Bool](target/packageaccess.md)
  If true, access to package declarations from other targets in the package is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/cxxsetting)*