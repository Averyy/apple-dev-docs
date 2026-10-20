# plugins

**Framework**: PackageDescription  
**Kind**: property  
**Role**: Instance Property

The uses of package plug-ins by the target.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
final var plugins: [Target.PluginUsage]?
```

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
- [Target.PluginUsage](./pluginusage.md)
  A plug-in used in a target.
- [let packageAccess: Bool](./packageaccess.md)
  If true, access to package declarations from other targets in the package is allowed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/plugins)*