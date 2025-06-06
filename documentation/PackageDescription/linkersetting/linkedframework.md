# linkedFramework(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Declares linkage to a system framework.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func linkedFramework(_ framework: String, _ condition: BuildSettingCondition? = nil) -> LinkerSetting
```

#### Discussion

This setting is most useful when the framework can’t be linked automatically, such as C++ based frameworks and non-modular frameworks.

> **Note**: First available in PackageDescription 5.0.

First available in PackageDescription 5.0.

## Parameters

- `framework`: The framework name.
- `condition`: A condition that restricts the application of the build   setting.

## See Also

- [static func linkedLibrary(String, BuildSettingCondition?) -> LinkerSetting](linkersetting/linkedlibrary(_:_:).md)
  Declares linkage to a system library.
- [static func unsafeFlags([String], BuildSettingCondition?) -> LinkerSetting](linkersetting/unsafeflags(_:_:).md)
  Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/linkersetting/linkedframework(_:_:))*