# Target

**Framework**: PackageDescription  
**Kind**: class

The basic building block of a Swift package.

## Declaration

```swift
final class Target
```

#### Overview

Each target contains a set of source files that Swift Package Manager compiles into a module or test suite. You can vend targets to other packages by defining products that include the targets.

A target may depend on other targets within the same package and on products vended by the package’s dependencies.

## Topics

### Naming the Target
- [var name: String](target/name.md)
  The name of the target.
### Configuring File Locations
- [var path: String?](target/path.md)
  The path of the target, relative to the package root.
- [var exclude: [String]](target/exclude.md)
  The paths to source and resource files that you don’t want to include in the target.
- [var sources: [String]?](target/sources.md)
  The source files in this target.
- [var resources: [Resource]?](target/resources.md)
  The explicit list of resource files in the target.
- [struct Resource](resource.md)
  A resource to bundle with the Swift package.
- [var publicHeadersPath: String?](target/publicheaderspath.md)
  The path to the directory that contains public headers of a C-family target.
### Creating a Binary Target
- [static func binaryTarget(name: String, path: String) -> Target](target/binarytarget(name:path:).md)
  Creates a binary target that references an artifact on disk.
- [static func binaryTarget(name: String, url: String, checksum: String) -> Target](target/binarytarget(name:url:checksum:).md)
  Creates a binary target that references a remote artifact.
- [var url: String?](target/url.md)
  The URL of a binary target.
- [var checksum: String?](target/checksum.md)
  The checksum for the archive file that contains the referenced binary artifact.
### Creating a System Library Target
- [static func systemLibrary(name: String, path: String?, pkgConfig: String?, providers: [SystemPackageProvider]?) -> Target](target/systemlibrary(name:path:pkgconfig:providers:).md)
  Creates a system library target.
- [let pkgConfig: String?](target/pkgconfig.md)
  The name of the package configuration file, without extension, for the system library target.
- [let providers: [SystemPackageProvider]?](target/providers.md)
  The providers array for a system library target.
### Creating an Executable Target
- [static func executableTarget(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, publicHeadersPath: String?, packageAccess: Bool, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?, plugins: [Target.PluginUsage]?) -> Target](target/executabletarget(name:dependencies:path:exclude:sources:resources:publicheaderspath:packageaccess:csettings:cxxsettings:swiftsettings:linkersettings:plugins:).md)
  Creates an executable target.
- [static func executableTarget(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, publicHeadersPath: String?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?, plugins: [Target.PluginUsage]?) -> Target](target/executabletarget(name:dependencies:path:exclude:sources:resources:publicheaderspath:csettings:cxxsettings:swiftsettings:linkersettings:plugins:).md)
  Creates an executable target.
- [static func executableTarget(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, publicHeadersPath: String?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?) -> Target](target/executabletarget(name:dependencies:path:exclude:sources:resources:publicheaderspath:csettings:cxxsettings:swiftsettings:linkersettings:).md)
  Creates an executable target.
### Creating a Regular Target
- [static func target(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, publicHeadersPath: String?, packageAccess: Bool, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?, plugins: [Target.PluginUsage]?) -> Target](target/target(name:dependencies:path:exclude:sources:resources:publicheaderspath:packageaccess:csettings:cxxsettings:swiftsettings:linkersettings:plugins:).md)
  Creates a regular target.
- [static func target(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, publicHeadersPath: String?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?, plugins: [Target.PluginUsage]?) -> Target](target/target(name:dependencies:path:exclude:sources:resources:publicheaderspath:csettings:cxxsettings:swiftsettings:linkersettings:plugins:).md)
  Creates a regular target.
- [static func target(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, publicHeadersPath: String?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?) -> Target](target/target(name:dependencies:path:exclude:sources:resources:publicheaderspath:csettings:cxxsettings:swiftsettings:linkersettings:).md)
  Creates a regular target.
- [static func target(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, publicHeadersPath: String?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?) -> Target](target/target(name:dependencies:path:exclude:sources:publicheaderspath:csettings:cxxsettings:swiftsettings:linkersettings:).md)
  Creates a library or executable target.
- [static func target(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, publicHeadersPath: String?) -> Target](target/target(name:dependencies:path:exclude:sources:publicheaderspath:).md)
  Creates a library or executable target.
### Creating a Test Target
- [static func testTarget(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, packageAccess: Bool, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?, plugins: [Target.PluginUsage]?) -> Target](target/testtarget(name:dependencies:path:exclude:sources:resources:packageaccess:csettings:cxxsettings:swiftsettings:linkersettings:plugins:).md)
  Creates a test target.
- [static func testTarget(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?, plugins: [Target.PluginUsage]?) -> Target](target/testtarget(name:dependencies:path:exclude:sources:resources:csettings:cxxsettings:swiftsettings:linkersettings:plugins:).md)
  Creates a test target.
- [static func testTarget(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?) -> Target](target/testtarget(name:dependencies:path:exclude:sources:resources:csettings:cxxsettings:swiftsettings:linkersettings:).md)
  Creates a test target.
- [static func testTarget(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?) -> Target](target/testtarget(name:dependencies:path:exclude:sources:csettings:cxxsettings:swiftsettings:linkersettings:).md)
  Creates a test target.
- [static func testTarget(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?) -> Target](target/testtarget(name:dependencies:path:exclude:sources:).md)
  Creates a test target.
### Creating a Plugin Target
- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, packageAccess: Bool) -> Target](target/plugin(name:capability:dependencies:path:exclude:sources:packageaccess:).md)
  Defines a new package plug-in target.
- [var pluginCapability: Target.PluginCapability?](target/plugincapability-swift.property.md)
  The capability provided by a package plug-in target.
- [Target.PluginCapability](target/plugincapability-swift.enum.md)
  The different types of capability that a plug-in can provide.
- [enum PluginCommandIntent](plugincommandintent.md)
  The intended use case of the command plug-in.
- [enum PluginPermission](pluginpermission.md)
  The type of permission a plug-in requires.
- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?) -> Target](target/plugin(name:capability:dependencies:path:exclude:sources:).md)
  Defines a new package plugin target.
### Declaring a Dependency Target
- [var dependencies: [Target.Dependency]](target/dependencies.md)
  The target’s dependencies on other entities inside or outside the package.
- [Target.Dependency](target/dependency.md)
  The different types of a target’s dependency on another entity.
- [struct TargetDependencyCondition](targetdependencycondition.md)
  A condition that limits the application of a target’s dependency.
### Configuring the Target
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
- [Target.PluginUsage](target/pluginusage.md)
  A plug-in used in a target.
- [let packageAccess: Bool](target/packageaccess.md)
  If true, access to package declarations from other targets in the package is allowed.
### Describing the Target Type
- [var isTest: Bool](target/istest.md)
  A Boolean value that indicates whether this is a test target.
- [let type: Target.TargetType](target/type.md)
  The type of the target.
- [Target.TargetType](target/targettype.md)
  The different types of a target.
### Type Methods
- [static func macro(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, packageAccess: Bool, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?, plugins: [Target.PluginUsage]?) -> Target](target/macro(name:dependencies:path:exclude:sources:packageaccess:swiftsettings:linkersettings:plugins:).md)

## See Also

- [var targets: [Target]](package/targets.md)
  The list of targets that are part of this package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target)*