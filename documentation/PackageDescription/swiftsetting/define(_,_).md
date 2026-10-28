# define(_:_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Defines a compilation condition.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func define(_ name: String, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

## Discussion

Use compilation conditions to only compile statements if a certain condition is true. For example, the Swift compiler will only compile the statements inside the `#if` block when `ENABLE_SOMETHING` is defined:

```swift
#if ENABLE_SOMETHING
   ...
#endif
```

Unlike macros in C/C++, compilation conditions don’t have an associated value.

> **Since**: First available in PackageDescription 5.0.

## Parameters

- `name`: The name of the macro.
- `condition`: A condition that restricts the application of the build setting.

## See Also

### Configuring Swift Settings
- [static func unsafeFlags([String], BuildSettingCondition?) -> SwiftSetting](./unsafeflags%28_,_%29.md)
  Set unsafe flags to pass arbitrary command-line flags to the corresponding build tool.
- [static func strictMemorySafety(BuildSettingCondition?) -> SwiftSetting](./strictmemorysafety%28_%29.md)
  Enable strict memory safety checking.
- [static func swiftLanguageMode(SwiftLanguageMode, BuildSettingCondition?) -> SwiftSetting](./swiftlanguagemode%28_,_%29.md)
  Defines a `-language-mode` to pass  to the corresponding build tool.
- [static func defaultIsolation(MainActor.Type?, BuildSettingCondition?) -> SwiftSetting](./defaultisolation%28_,_%29.md)
  Set the default isolation to the given global actor type.
- [static func enableExperimentalFeature(String, BuildSettingCondition?) -> SwiftSetting](./enableexperimentalfeature%28_,_%29.md)
  Enable an experimental feature with the given name.
- [static func enableUpcomingFeature(String, BuildSettingCondition?) -> SwiftSetting](./enableupcomingfeature%28_,_%29.md)
  Enable an upcoming feature with the given name.
- [static func interoperabilityMode(SwiftSetting.InteroperabilityMode, BuildSettingCondition?) -> SwiftSetting](./interoperabilitymode%28_,_%29.md)
  Enables Swift interoperability with a given language.
- [SwiftSetting.InteroperabilityMode](./interoperabilitymode.md)
  The interoperability mode
- [static func swiftLanguageVersion(SwiftVersion, BuildSettingCondition?) -> SwiftSetting](./swiftlanguageversion%28_,_%29.md)
  Defines a `-swift-version` to pass  to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/define(_:_:))*