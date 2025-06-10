# BuildSettingCondition

**Framework**: PackageDescription  
**Kind**: struct

A condition that limits the application of a build setting.

## Declaration

```swift
struct BuildSettingCondition
```

#### Overview

By default, build settings are applicable for all platforms and build configurations. Use the `.when` modifier to define a build setting for a specific condition. Invalid usage of `.when` emits an error during manifest parsing. For example, it’s invalid to specify a `.when` condition with both parameters as `nil`.

The following example shows how to use build setting conditions with various APIs:

```swift
...
.target(
    name: "MyTool",
    dependencies: ["Utility"],
    cSettings: [
        .headerSearchPath("path/relative/to/my/target"),
        .define("DISABLE_SOMETHING", .when(platforms: [.iOS], configuration: .release)),
    ],
    swiftSettings: [
        .define("ENABLE_SOMETHING", .when(configuration: .release)),
    ],
    linkerSettings: [
        .linkLibrary("openssl", .when(platforms: [.linux])),
    ]
),
```

## Topics

### Checking for a Build Condition
- [static func when(platforms: [Platform]) -> BuildSettingCondition](buildsettingcondition/when(platforms:).md)
  Creates a build setting condition.
- [static func when(configuration: BuildConfiguration) -> BuildSettingCondition](buildsettingcondition/when(configuration:).md)
  Creates a build setting condition.
- [static func when(platforms: [Platform], configuration: BuildConfiguration) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:)-475co.md)
  Creates a build setting condition.
- [static func when(platforms: [Platform]?, configuration: BuildConfiguration?, traits: Set<String>?) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:traits:).md)
  Creates a build setting condition.
- [static func when(platforms: [Platform]?, configuration: BuildConfiguration?) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:)-2991l.md)
  Creates a build setting condition.

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
- [struct CSetting](csetting.md)
  A C language build setting.
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

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/buildsettingcondition)*