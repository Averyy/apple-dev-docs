# treatAllWarnings(as:_:)

**Framework**: PackageDescription  
**Kind**: method

Controls how all Swift compiler warnings are treated during compilation.

**Availability**:
- SwiftPM 6.2+

## Declaration

```swift
static func treatAllWarnings(as level: WarningLevel, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

Use this setting to specify whether all warnings should be treated as warnings (default behavior) or as errors. This is equivalent to passing `-warnings-as-errors` or `-no-warnings-as-errors` to the Swift compiler.

This setting applies to all warnings emitted by the Swift compiler. To control specific warnings individually, use `treatWarning(name:as:_:)` instead.

> **Note**: First available in PackageDescription 6.2.

## Parameters

- `level`: The treatment level for all warnings (  or  ).
- `condition`: A condition that restricts the application of the build setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/treatallwarnings(as:_:))*