# linkedLibrary(_:_:)

**Framework**: Packagedescription  
**Kind**: method

Declares linkage to a system library.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func linkedLibrary(_ library: String, _ condition: BuildSettingCondition? = nil) -> LinkerSetting
```

#### Discussion

This setting is most useful when the library can’t be linked automatically, such as C++ based libraries and non-modular libraries.

> **Note**: First available in PackageDescription 5.0.

## Parameters

- `library`: The library name.
- `condition`: A condition that restricts the application of the build   setting.

## See Also

- [static func linkedFramework(String, BuildSettingCondition?) -> LinkerSetting](linkersetting/linkedframework(_:_:).md)
  Declares linkage to a system framework.
- [static func unsafeFlags([String], BuildSettingCondition?) -> LinkerSetting](linkersetting/unsafeflags(_:_:).md)
  Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/linkersetting/linkedlibrary(_:_:))*