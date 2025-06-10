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

## Parameters

- `flags`: The unsafe flags to set.
- `condition`: A condition that restricts the application of the build   setting.

## See Also

- [static func define(String, BuildSettingCondition?) -> SwiftSetting](swiftsetting/define(_:_:).md)
  Defines a compilation condition.
- [static func strictMemorySafety(BuildSettingCondition?) -> SwiftSetting](swiftsetting/strictmemorysafety(_:).md)
  Enable strict memory safety checking.
- [static func swiftLanguageMode(SwiftLanguageMode, BuildSettingCondition?) -> SwiftSetting](swiftsetting/swiftlanguagemode(_:_:).md)
  Defines a `-language-mode` to pass  to the corresponding build tool.
- [static func defaultIsolation(MainActor.Type?, BuildSettingCondition?) -> SwiftSetting](swiftsetting/defaultisolation(_:_:).md)
  Set the default isolation to the given global actor type.
- [static func enableExperimentalFeature(String, BuildSettingCondition?) -> SwiftSetting](swiftsetting/enableexperimentalfeature(_:_:).md)
  Enable an experimental feature with the given name.
- [static func enableUpcomingFeature(String, BuildSettingCondition?) -> SwiftSetting](swiftsetting/enableupcomingfeature(_:_:).md)
  Enable an upcoming feature with the given name.
- [static func interoperabilityMode(SwiftSetting.InteroperabilityMode, BuildSettingCondition?) -> SwiftSetting](swiftsetting/interoperabilitymode(_:_:).md)
  Enable Swift interoperability with a given language.
- [SwiftSetting.InteroperabilityMode](swiftsetting/interoperabilitymode.md)
- [static func swiftLanguageVersion(SwiftVersion, BuildSettingCondition?) -> SwiftSetting](swiftsetting/swiftlanguageversion(_:_:).md)
  Defines a `-swift-version` to pass  to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/unsafeflags(_:_:))*