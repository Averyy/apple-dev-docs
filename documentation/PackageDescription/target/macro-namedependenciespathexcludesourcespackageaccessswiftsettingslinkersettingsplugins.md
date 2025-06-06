# macro(name:dependencies:path:exclude:sources:packageAccess:swiftSettings:linkerSettings:plugins:)

**Framework**: PackageDescription  
**Kind**: method

**Availability**:
- SwiftPM 5.9+

## Declaration

```swift
static func macro(name: String, dependencies: [Target.Dependency] = [], path: String? = nil, exclude: [String] = [], sources: [String]? = nil, packageAccess: Bool = true, swiftSettings: [SwiftSetting]? = nil, linkerSettings: [LinkerSetting]? = nil, plugins: [Target.PluginUsage]? = nil) -> Target
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/macro(name:dependencies:path:exclude:sources:packageaccess:swiftsettings:linkersettings:plugins:))*