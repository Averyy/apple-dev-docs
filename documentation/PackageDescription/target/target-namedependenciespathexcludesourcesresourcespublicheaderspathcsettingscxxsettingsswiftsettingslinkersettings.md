# target(name:dependencies:path:exclude:sources:resources:publicHeadersPath:cSettings:cxxSettings:swiftSettings:linkerSettings:)

**Framework**: PackageDescription  
**Kind**: method

Creates a regular target.

## Declaration

```swift
static func target(name: String, dependencies: [Target.Dependency] = [], path: String? = nil, exclude: [String] = [], sources: [String]? = nil, resources: [Resource]? = nil, publicHeadersPath: String? = nil, cSettings: [CSetting]? = nil, cxxSettings: [CXXSetting]? = nil, swiftSettings: [SwiftSetting]? = nil, linkerSettings: [LinkerSetting]? = nil) -> Target
```

#### Discussion

A target can contain either Swift or C-family source files, but not both. It contains code that is built as a regular module that can be included in a library or executable product, but that cannot itself be used as the main target of an executable product.

## Parameters

- `name`: The name of the target.
- `dependencies`: The dependencies of the target. A dependency can be another target in the package or a product from a package dependency.
- `path`: The custom path for the target. By default, the Swift Package Manager requires a target’s sources to reside at predefined search paths;   for example,  .   Don’t escape the package root; for example, values like   or   are invalid.
- `exclude`: A list of paths to files or directories that the Swift Package Manager shouldn’t consider to be source or resource files.   A path is relative to the target’s directory.   This parameter has precedence over the   parameter.
- `sources`: An explicit list of source files. If you provide a path to a directory,   the Swift Package Manager searches for valid source files recursively.
- `resources`: An explicit list of resources files.
- `publicHeadersPath`: The directory containing public headers of a C-family library target.
- `cSettings`: The C settings for this target.
- `cxxSettings`: The C++ settings for this target.
- `swiftSettings`: The Swift settings for this target.
- `linkerSettings`: The linker settings for this target.

## See Also

- [static func target(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, publicHeadersPath: String?, packageAccess: Bool, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?, plugins: [Target.PluginUsage]?) -> Target](target/target(name:dependencies:path:exclude:sources:resources:publicheaderspath:packageaccess:csettings:cxxsettings:swiftsettings:linkersettings:plugins:).md)
  Creates a regular target.
- [static func target(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, resources: [Resource]?, publicHeadersPath: String?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?, plugins: [Target.PluginUsage]?) -> Target](target/target(name:dependencies:path:exclude:sources:resources:publicheaderspath:csettings:cxxsettings:swiftsettings:linkersettings:plugins:).md)
  Creates a regular target.
- [static func target(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, publicHeadersPath: String?, cSettings: [CSetting]?, cxxSettings: [CXXSetting]?, swiftSettings: [SwiftSetting]?, linkerSettings: [LinkerSetting]?) -> Target](target/target(name:dependencies:path:exclude:sources:publicheaderspath:csettings:cxxsettings:swiftsettings:linkersettings:).md)
  Creates a library or executable target.
- [static func target(name: String, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, publicHeadersPath: String?) -> Target](target/target(name:dependencies:path:exclude:sources:publicheaderspath:).md)
  Creates a library or executable target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/target(name:dependencies:path:exclude:sources:resources:publicheaderspath:csettings:cxxsettings:swiftsettings:linkersettings:))*