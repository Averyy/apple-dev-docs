# treatWarning(_:as:_:)

**Framework**: PackageDescription  
**Kind**: method

Controls how a specific Swift compiler warning is treated during compilation.

**Availability**:
- SwiftPM 6.2+

## Declaration

```swift
static func treatWarning(_ name: String, as level: WarningLevel, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

Use this setting to specify whether a particular warning should be treated as a warning (default behavior) or as an error. This is equivalent to passing `-Werror` or `-Wwarning` followed by the warning name to the Swift compiler.

This setting allows for fine-grained control over individual warnings. To control all warnings at once, use `treatAllWarnings(as:_:)` instead.

> **Note**: First available in PackageDescription 6.2.

## Parameters

- `name`: The name of the specific warning to control.
- `level`: The treatment level for the warning (  or  ).
- `condition`: A condition that restricts the application of the build setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/treatwarning(_:as:_:))*