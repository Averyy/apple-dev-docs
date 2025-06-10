# define(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Defines a compilation condition.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func define(_ name: String, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

Use compilation conditions to only compile statements if a certain condition is true. For example, the Swift compiler will only compile the statements inside the `#if` block when `ENABLE_SOMETHING` is defined:

```swift
#if ENABLE_SOMETHING
   ...
#endif
```

Unlike macros in C/C++, compilation conditions don’t have an associated value.

> **Note**: First available in PackageDescription 5.0.

## Parameters

- `name`: The name of the macro.
- `condition`: A condition that restricts the application of the build   setting.

## See Also

- [static func unsafeFlags([String], BuildSettingCondition?) -> SwiftSetting](swiftsetting/unsafeflags(_:_:).md)
  Set unsafe flags to pass arbitrary command-line flags to the corresponding build tool.
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

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/define(_:_:))*