# enableExperimentalFeature(_:_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

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

> **Since**: First available in PackageDescription 5.8.

## Parameters

- `name`: The name of the experimental feature; for example, `VariadicGenerics`.
- `condition`: A condition that restricts the application of the build setting.

## See Also

### Configuring Swift Settings
- [static func define(String, BuildSettingCondition?) -> SwiftSetting](./define%28_,_%29.md)
  Defines a compilation condition.
- [static func unsafeFlags([String], BuildSettingCondition?) -> SwiftSetting](./unsafeflags%28_,_%29.md)
  Set unsafe flags to pass arbitrary command-line flags to the corresponding build tool.
- [static func strictMemorySafety(BuildSettingCondition?) -> SwiftSetting](./strictmemorysafety%28_%29.md)
  Enable strict memory safety checking.
- [static func swiftLanguageMode(SwiftLanguageMode, BuildSettingCondition?) -> SwiftSetting](./swiftlanguagemode%28_,_%29.md)
  Defines a `-language-mode` to pass  to the corresponding build tool.
- [static func defaultIsolation(MainActor.Type?, BuildSettingCondition?) -> SwiftSetting](./defaultisolation%28_,_%29.md)
  Set the default isolation to the given global actor type.
- [static func enableUpcomingFeature(String, BuildSettingCondition?) -> SwiftSetting](./enableupcomingfeature%28_,_%29.md)
  Enable an upcoming feature with the given name.
- [static func interoperabilityMode(SwiftSetting.InteroperabilityMode, BuildSettingCondition?) -> SwiftSetting](./interoperabilitymode%28_,_%29.md)
  Enables Swift interoperability with a given language.
- [SwiftSetting.InteroperabilityMode](./interoperabilitymode.md)
  The interoperability mode
- [static func swiftLanguageVersion(SwiftVersion, BuildSettingCondition?) -> SwiftSetting](./swiftlanguageversion%28_,_%29.md)
  Defines a `-swift-version` to pass  to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/enableexperimentalfeature(_:_:))*