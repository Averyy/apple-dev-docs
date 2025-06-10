# strictMemorySafety(_:)

**Framework**: PackageDescription  
**Kind**: method

Enable strict memory safety checking.

**Availability**:
- SwiftPM 6.2+

## Declaration

```swift
static func strictMemorySafety(_ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

Strict memory safety checking is an opt-in compiler feature that identifies any uses of language constructs or APIs that break memory safety. Issues are reported as warnings and can generally be suppressed by adding annotations (such as `@unsafe` and `unsafe`) that acknowledge the presence of unsafe code, making it easier to review and audit at a later time.

> **Note**: First available in PackageDescription 6.2.

## Parameters

- `condition`: A condition that restricts the application of the build   setting.

## See Also

- [static func define(String, BuildSettingCondition?) -> SwiftSetting](swiftsetting/define(_:_:).md)
  Defines a compilation condition.
- [static func unsafeFlags([String], BuildSettingCondition?) -> SwiftSetting](swiftsetting/unsafeflags(_:_:).md)
  Set unsafe flags to pass arbitrary command-line flags to the corresponding build tool.
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

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/strictmemorysafety(_:))*