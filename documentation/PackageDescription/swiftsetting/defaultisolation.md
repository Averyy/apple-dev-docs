# defaultIsolation(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Set the default isolation to the given global actor type.

**Availability**:
- SwiftPM 6.2+

## Declaration

```swift
static func defaultIsolation(_ isolation: MainActor.Type?, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

> **Note**: First available in PackageDescription 6.2.

## Parameters

- `isolation`: The type of global actor to use for default actor isolation   inference. The only valid arguments are   and  .
- `condition`: A condition that restricts the application of the build   setting.

## See Also

- [static func define(String, BuildSettingCondition?) -> SwiftSetting](swiftsetting/define(_:_:).md)
  Defines a compilation condition.
- [static func unsafeFlags([String], BuildSettingCondition?) -> SwiftSetting](swiftsetting/unsafeflags(_:_:).md)
  Set unsafe flags to pass arbitrary command-line flags to the corresponding build tool.
- [static func strictMemorySafety(BuildSettingCondition?) -> SwiftSetting](swiftsetting/strictmemorysafety(_:).md)
  Enable strict memory safety checking.
- [static func swiftLanguageMode(SwiftLanguageMode, BuildSettingCondition?) -> SwiftSetting](swiftsetting/swiftlanguagemode(_:_:).md)
  Defines a `-language-mode` to pass  to the corresponding build tool.
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

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/defaultisolation(_:_:))*