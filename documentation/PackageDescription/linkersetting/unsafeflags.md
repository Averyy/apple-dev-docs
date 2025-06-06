# unsafeFlags(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func unsafeFlags(_ flags: [String], _ condition: BuildSettingCondition? = nil) -> LinkerSetting
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

- [static func linkedFramework(String, BuildSettingCondition?) -> LinkerSetting](linkersetting/linkedframework(_:_:).md)
  Declares linkage to a system framework.
- [static func linkedLibrary(String, BuildSettingCondition?) -> LinkerSetting](linkersetting/linkedlibrary(_:_:).md)
  Declares linkage to a system library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/linkersetting/unsafeflags(_:_:))*