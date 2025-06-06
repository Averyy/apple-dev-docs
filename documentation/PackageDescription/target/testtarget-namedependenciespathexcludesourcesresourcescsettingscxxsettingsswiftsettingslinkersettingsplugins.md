# testTarget(name:dependencies:path:exclude:sources:resources:cSettings:cxxSettings:swiftSettings:linkerSettings:plugins:)

**Framework**: PackageDescription  
**Kind**: method

Creates a test target.

## Declaration

```swift
static func testTarget(name: String, dependencies: [Target.Dependency] = [], path: String? = nil, exclude: [String] = [], sources: [String]? = nil, resources: [Resource]? = nil, cSettings: [CSetting]? = nil, cxxSettings: [CXXSetting]? = nil, swiftSettings: [SwiftSetting]? = nil, linkerSettings: [LinkerSetting]? = nil, plugins: [Target.PluginUsage]? = nil) -> Target
```

#### Discussion

Write test targets using the XCTest testing framework. Test targets generally declare a dependency on the targets they test.

## Parameters

- `name`: The name of the target.
- `dependencies`: The dependencies of the target. A dependency can be another target in the package or a product from a package dependency.
- `path`: The custom path for the target. By default, the Swift Package Manager requires a target’s sources to reside at predefined search paths;   for example,  .   Don’t escape the package root; for example, values like   or   are invalid.
- `exclude`: A list of paths to files or directories that the Swift Package Manager shouldn’t consider to be source or resource files.   A path is relative to the target’s directory.   This parameter has precedence over the   parameter.
- `sources`: An explicit list of source files. If you provide a path to a directory,   the Swift Package Manager searches for valid source files recursively.
- `resources`: An explicit list of resources files.
- `cSettings`: The C settings for this target.
- `cxxSettings`: The C++ settings for this target.
- `swiftSettings`: The Swift settings for this target.
- `linkerSettings`: The linker settings for this target.
- `plugins`: The plug-ins used by this target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/testtarget(name:dependencies:path:exclude:sources:resources:csettings:cxxsettings:swiftsettings:linkersettings:plugins:))*