# interoperabilityMode(_:_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Enables Swift interoperability with a given language.

**Availability**:
- SwiftPM 5.9+

## Declaration

```swift
static func interoperabilityMode(_ mode: SwiftSetting.InteroperabilityMode, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

This is useful for enabling interoperability between Swift and C++ for a given target.

Enabling C++ interoperability mode might alter the way some existing C and Objective-C APIs are imported.

> **Since**: First available in PackageDescription 5.9.

## Parameters

- `mode`: The interoperability mode, either C-compatible or C++-compatible.
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
- [static func enableExperimentalFeature(String, BuildSettingCondition?) -> SwiftSetting](./enableexperimentalfeature%28_,_%29.md)
  Enable an experimental feature with the given name.
- [static func enableUpcomingFeature(String, BuildSettingCondition?) -> SwiftSetting](./enableupcomingfeature%28_,_%29.md)
  Enable an upcoming feature with the given name.
- [SwiftSetting.InteroperabilityMode](./interoperabilitymode.md)
  The interoperability mode
- [static func swiftLanguageVersion(SwiftVersion, BuildSettingCondition?) -> SwiftSetting](./swiftlanguageversion%28_,_%29.md)
  Defines a `-swift-version` to pass  to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/interoperabilitymode(_:_:))*