# SwiftSetting.InteroperabilityMode

**Framework**: PackageDescription  
**Kind**: enum  
**Role**: Enumeration

The interoperability mode

## Declaration

```swift
enum InteroperabilityMode
```

## Topics

### Enumeration Cases
- [SwiftSetting.InteroperabilityMode.C](./interoperabilitymode/c.md)
  Emit code compatible with being imported from C and Objective-C.
- [SwiftSetting.InteroperabilityMode.Cxx](./interoperabilitymode/cxx.md)
  Emit code compatible with being imported from C++ and Objective-C++.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

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
- [static func interoperabilityMode(SwiftSetting.InteroperabilityMode, BuildSettingCondition?) -> SwiftSetting](./interoperabilitymode%28_,_%29.md)
  Enables Swift interoperability with a given language.
- [static func swiftLanguageVersion(SwiftVersion, BuildSettingCondition?) -> SwiftSetting](./swiftlanguageversion%28_,_%29.md)
  Defines a `-swift-version` to pass  to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/interoperabilitymode)*