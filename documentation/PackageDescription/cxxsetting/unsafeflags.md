# unsafeFlags(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func unsafeFlags(_ flags: [String], _ condition: BuildSettingCondition? = nil) -> CXXSetting
```

#### Discussion

As the usage of the word “unsafe” implies, Swift Package Manager can’t safely determine if the build flags have any negative side effect on the build since certain flags can change the behavior of how it performs a build.

As some build flags can be exploited for unsupported or malicious behavior, you can’t use products with unsafe build flags as dependencies in another package.

> **Note**: First available in PackageDescription 5.0.

## Parameters

- `flags`: The unsafe flags to set.
- `condition`: A condition that restricts the application of the build   setting.

## See Also

- [static func define(String, to: String?, BuildSettingCondition?) -> CXXSetting](cxxsetting/define(_:to:_:).md)
  Defines a value for a macro.
- [static func headerSearchPath(String, BuildSettingCondition?) -> CXXSetting](cxxsetting/headersearchpath(_:_:).md)
  Provides a header search path relative to the target’s directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/cxxsetting/unsafeflags(_:_:))*