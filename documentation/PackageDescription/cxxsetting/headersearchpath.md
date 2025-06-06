# headerSearchPath(_:_:)

**Framework**: Packagedescription  
**Kind**: method

Provides a header search path relative to the target’s directory.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func headerSearchPath(_ path: String, _ condition: BuildSettingCondition? = nil) -> CXXSetting
```

#### Discussion

Use this setting to add a search path for headers within your target. You can’t use absolute paths and you can’t use this setting to provide headers that are visible to other targets.

The path must be a directory inside the package.

> **Note**: First available in PackageDescription 5.0.

## Parameters

- `path`: The path of the directory that contains the headers. The path is   relative to the target’s directory.
- `condition`: A condition that restricts the application of the build setting.

## See Also

- [static func define(String, to: String?, BuildSettingCondition?) -> CXXSetting](cxxsetting/define(_:to:_:).md)
  Defines a value for a macro.
- [static func unsafeFlags([String], BuildSettingCondition?) -> CXXSetting](cxxsetting/unsafeflags(_:_:).md)
  Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/cxxsetting/headersearchpath(_:_:))*