# unsafeFlags(_:_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func unsafeFlags(_ flags: [String], _ condition: BuildSettingCondition? = nil) -> CSetting
```

#### Discussion

As the usage of the word “unsafe” implies, Swift Package Manager can’t safely determine if the build flags have any negative side effect on the build since certain flags can change the behavior of how it performs a build.

As some build flags can be exploited for unsupported or malicious behavior, the use of unsafe flags makes the products containing this target ineligible for use by other packages.

> **Since**: First available in PackageDescription 5.0.

## Parameters

- `flags`: The unsafe flags to set.
- `condition`: A condition that restricts the application of the build setting.

## See Also

### Configuring C Settings
- [static func define(String, to: String?, BuildSettingCondition?) -> CSetting](./define%28_,to,_%29.md)
  Defines a value for a macro.
- [static func headerSearchPath(String, BuildSettingCondition?) -> CSetting](./headersearchpath%28_,_%29.md)
  Provides a header search path relative to the target’s directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/csetting/unsafeflags(_:_:))*