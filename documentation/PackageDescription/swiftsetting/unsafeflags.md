# unsafeFlags(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Set unsafe flags to pass arbitrary command-line flags to the corresponding build tool.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func unsafeFlags(_ flags: [String], _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

As the usage of the word “unsafe” implies, Swift Package Manager can’t safely determine if the build flags have any negative side effect on the build since certain flags can change the behavior of how it performs a build.

As some build flags can be exploited for unsupported or malicious behavior, the use of unsafe flags makes the products containing this target ineligible for use by other packages.

> **Note**: First available in PackageDescription 5.0.

First available in PackageDescription 5.0.

## Parameters

- `flags`: The unsafe flags to set.
- `condition`: A condition that restricts the application of the build   setting.

## See Also

- [static func define(String, BuildSettingCondition?) -> SwiftSetting](swiftsetting/define(_:_:).md)
  Defines a compilation condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/unsafeflags(_:_:))*