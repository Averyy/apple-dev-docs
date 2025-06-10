# enableExperimentalFeature(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Enable an experimental feature with the given name.

**Availability**:
- SwiftPM 5.8+

## Declaration

```swift
static func enableExperimentalFeature(_ name: String, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

An experimental feature is one that’s in development, but is not yet available in Swift as a language feature.

You can add and use multiple experimental features in a given target without affecting its dependencies. Targets will ignore any  unknown experimental features.

> **Note**: First available in PackageDescription 5.8.

## Parameters

- `name`: The name of the experimental feature; for example,  .
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
- [static func defaultIsolation(MainActor.Type?, BuildSettingCondition?) -> SwiftSetting](swiftsetting/defaultisolation(_:_:).md)
  Set the default isolation to the given global actor type.
- [static func enableUpcomingFeature(String, BuildSettingCondition?) -> SwiftSetting](swiftsetting/enableupcomingfeature(_:_:).md)
  Enable an upcoming feature with the given name.
- [static func interoperabilityMode(SwiftSetting.InteroperabilityMode, BuildSettingCondition?) -> SwiftSetting](swiftsetting/interoperabilitymode(_:_:).md)
  Enable Swift interoperability with a given language.
- [SwiftSetting.InteroperabilityMode](swiftsetting/interoperabilitymode.md)
- [static func swiftLanguageVersion(SwiftVersion, BuildSettingCondition?) -> SwiftSetting](swiftsetting/swiftlanguageversion(_:_:).md)
  Defines a `-swift-version` to pass  to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/enableexperimentalfeature(_:_:))*