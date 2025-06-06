# define(_:to:_:)

**Framework**: PackageDescription  
**Kind**: method

Defines a value for a macro.

**Availability**:
- SwiftPM 5.0+

## Declaration

```swift
static func define(_ name: String, to value: String? = nil, _ condition: BuildSettingCondition? = nil) -> CSetting
```

#### Discussion

If you don’t specify a value, the macro’s default value is 1.

> **Note**: First available in PackageDescription 5.0.

First available in PackageDescription 5.0.

## Parameters

- `name`: The name of the macro.
- `value`: The value of the macro.
- `condition`: A condition that restricts the use of the build   setting.

## See Also

- [static func headerSearchPath(String, BuildSettingCondition?) -> CSetting](csetting/headersearchpath(_:_:).md)
  Provides a header search path relative to the target’s directory.
- [static func unsafeFlags([String], BuildSettingCondition?) -> CSetting](csetting/unsafeflags(_:_:).md)
  Sets unsafe flags to pass arbitrary command-line flags to the corresponding build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/csetting/define(_:to:_:))*