# SwiftSetting.InteroperabilityMode

**Framework**: PackageDescription  
**Kind**: enum

The interoperability mode

## Declaration

```swift
enum InteroperabilityMode
```

## Topics

### Enumeration Cases
- [SwiftSetting.InteroperabilityMode.C](swiftsetting/interoperabilitymode/c.md)
  Emit code compatible with being imported from C and Objective-C.
- [SwiftSetting.InteroperabilityMode.Cxx](swiftsetting/interoperabilitymode/cxx.md)
  Emit code compatible with being imported from C++ and Objective-C++.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

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
- [static func enableExperimentalFeature(String, BuildSettingCondition?) -> SwiftSetting](swiftsetting/enableexperimentalfeature(_:_:).md)
  Enable an experimental feature with the given name.
- [static func enableUpcomingFeature(String, BuildSettingCondition?) -> SwiftSetting](swiftsetting/enableupcomingfeature(_:_:).md)
  Enable an upcoming feature with the given name.
- [static func interoperabilityMode(SwiftSetting.InteroperabilityMode, BuildSettingCondition?) -> SwiftSetting](swiftsetting/interoperabilitymode(_:_:).md)
  Enables Swift interoperability with a given language.
- [static func swiftLanguageVersion(SwiftVersion, BuildSettingCondition?) -> SwiftSetting](swiftsetting/swiftlanguageversion(_:_:).md)
  Defines a `-swift-version` to pass  to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/interoperabilitymode)*