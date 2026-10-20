# linkedLibrary(_:_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Declares linkage to a system library.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func linkedLibrary(_ library: String, _ condition: BuildSettingCondition? = nil) -> LinkerSetting
```

#### Discussion

This setting is most useful when the library can’t be linked automatically, such as C++ based libraries and non-modular libraries.

> **Since**: First available in PackageDescription 5.0.

## Parameters

- `library`: The library name.
- `condition`: A condition that restricts the application of the build setting.

## See Also

### Configuring Linker Settings
- [static func linkedFramework(String, BuildSettingCondition?) -> LinkerSetting](./linkedframework%28_,_%29.md)
  Declares linkage to a system framework.
- [static func unsafeFlags([String], BuildSettingCondition?) -> LinkerSetting](./unsafeflags%28_,_%29.md)
  Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/linkersetting/linkedlibrary(_:_:))*