# SwiftSetting

**Framework**: PackageDescription  
**Kind**: struct  
**Role**: Structure

A Swift language build setting.

## Declaration

```swift
struct SwiftSetting
```

## Topics

### Configuring Swift Settings
- [static func define(String, BuildSettingCondition?) -> SwiftSetting](./swiftsetting/define%28_,_%29.md)
  Defines a compilation condition.
- [static func unsafeFlags([String], BuildSettingCondition?) -> SwiftSetting](./swiftsetting/unsafeflags%28_,_%29.md)
  Set unsafe flags to pass arbitrary command-line flags to the corresponding build tool.
- [static func strictMemorySafety(BuildSettingCondition?) -> SwiftSetting](./swiftsetting/strictmemorysafety%28_%29.md)
  Enable strict memory safety checking.
- [static func swiftLanguageMode(SwiftLanguageMode, BuildSettingCondition?) -> SwiftSetting](./swiftsetting/swiftlanguagemode%28_,_%29.md)
  Defines a `-language-mode` to pass  to the corresponding build tool.
- [static func defaultIsolation(MainActor.Type?, BuildSettingCondition?) -> SwiftSetting](./swiftsetting/defaultisolation%28_,_%29.md)
  Set the default isolation to the given global actor type.
- [static func enableExperimentalFeature(String, BuildSettingCondition?) -> SwiftSetting](./swiftsetting/enableexperimentalfeature%28_,_%29.md)
  Enable an experimental feature with the given name.
- [static func enableUpcomingFeature(String, BuildSettingCondition?) -> SwiftSetting](./swiftsetting/enableupcomingfeature%28_,_%29.md)
  Enable an upcoming feature with the given name.
- [static func interoperabilityMode(SwiftSetting.InteroperabilityMode, BuildSettingCondition?) -> SwiftSetting](./swiftsetting/interoperabilitymode%28_,_%29.md)
  Enables Swift interoperability with a given language.
- [SwiftSetting.InteroperabilityMode](./swiftsetting/interoperabilitymode.md)
  The interoperability mode
- [static func swiftLanguageVersion(SwiftVersion, BuildSettingCondition?) -> SwiftSetting](./swiftsetting/swiftlanguageversion%28_,_%29.md)
  Defines a `-swift-version` to pass  to the corresponding build tool.
### Type Methods
- [static func treatAllWarnings(as: WarningLevel, BuildSettingCondition?) -> SwiftSetting](./swiftsetting/treatallwarnings%28as,_%29.md)
  Controls how all Swift compiler warnings are treated during compilation.
- [static func treatWarning(String, as: WarningLevel, BuildSettingCondition?) -> SwiftSetting](./swiftsetting/treatwarning%28_,as,_%29.md)
  Controls how a specific Swift compiler warning is treated during compilation.

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
- [struct LinkerSetting](./linkersetting.md)
  A linker build setting.
- [Target.PluginUsage](./target/pluginusage.md)
  A plug-in used in a target.
- [let packageAccess: Bool](./target/packageaccess.md)
  If true, access to package declarations from other targets in the package is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting)*