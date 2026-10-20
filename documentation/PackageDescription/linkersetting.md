# LinkerSetting

**Framework**: PackageDescription  
**Kind**: struct  
**Role**: Structure

A linker build setting.

## Declaration

```swift
struct LinkerSetting
```

## Topics

### Configuring Linker Settings
- [static func linkedFramework(String, BuildSettingCondition?) -> LinkerSetting](./linkersetting/linkedframework%28_,_%29.md)
  Declares linkage to a system framework.
- [static func linkedLibrary(String, BuildSettingCondition?) -> LinkerSetting](./linkersetting/linkedlibrary%28_,_%29.md)
  Declares linkage to a system library.
- [static func unsafeFlags([String], BuildSettingCondition?) -> LinkerSetting](./linkersetting/unsafeflags%28_,_%29.md)
  Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the Target
- [var cSettings: [CSetting]?](./target/csettings.md)
  The target’s C build settings.
- [var cxxSettings: [CXXSetting]?](./target/cxxsettings.md)
  The target’s C++ build settings.
- [var swiftSettings: [SwiftSetting]?](./target/swiftsettings.md)
  The target’s Swift build settings.
- [var linkerSettings: [LinkerSetting]?](./target/linkersettings.md)
  The target’s linker settings.
- [var plugins: [Target.PluginUsage]?](./target/plugins.md)
  The uses of package plug-ins by the target.
- [struct BuildConfiguration](./buildconfiguration.md)
  The build configuration, such as debug or release.
- [struct BuildSettingCondition](./buildsettingcondition.md)
  A condition that limits the application of a build setting.
- [struct CSetting](./csetting.md)
  A C language build setting.
- [struct CXXSetting](./cxxsetting.md)
  A CXX-language build setting.
- [struct SwiftSetting](./swiftsetting.md)
  A Swift language build setting.
- [Target.PluginUsage](./target/pluginusage.md)
  A plug-in used in a target.
- [let packageAccess: Bool](./target/packageaccess.md)
  If true, access to package declarations from other targets in the package is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/linkersetting)*