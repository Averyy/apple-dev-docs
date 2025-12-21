# CSetting

**Framework**: PackageDescription  
**Kind**: struct

A C language build setting.

## Declaration

```swift
struct CSetting
```

## Topics

### Configuring C Settings
- [static func define(String, to: String?, BuildSettingCondition?) -> CSetting](csetting/define(_:to:_:).md)
  Defines a value for a macro.
- [static func headerSearchPath(String, BuildSettingCondition?) -> CSetting](csetting/headersearchpath(_:_:).md)
  Provides a header search path relative to the target’s directory.
- [static func unsafeFlags([String], BuildSettingCondition?) -> CSetting](csetting/unsafeflags(_:_:).md)
  Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.
### Type Methods
- [static func disableWarning(String, BuildSettingCondition?) -> CSetting](csetting/disablewarning(_:_:).md)
  Disable a specific C compiler warning group.
- [static func enableWarning(String, BuildSettingCondition?) -> CSetting](csetting/enablewarning(_:_:).md)
  Enable a specific C compiler warning group.
- [static func treatAllWarnings(as: WarningLevel, BuildSettingCondition?) -> CSetting](csetting/treatallwarnings(as:_:).md)
  Controls how all C compiler warnings are treated during compilation.
- [static func treatWarning(String, as: WarningLevel, BuildSettingCondition?) -> CSetting](csetting/treatwarning(_:as:_:).md)
  Controls how a specific C compiler warning is treated during compilation.

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
- [struct CXXSetting](cxxsetting.md)
  A CXX-language build setting.
- [struct SwiftSetting](swiftsetting.md)
  A Swift language build setting.
- [struct LinkerSetting](linkersetting.md)
  A linker build setting.
- [Target.PluginUsage](target/pluginusage.md)
  A plug-in used in a target.
- [let packageAccess: Bool](target/packageaccess.md)
  If true, access to package declarations from other targets in the package is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/csetting)*