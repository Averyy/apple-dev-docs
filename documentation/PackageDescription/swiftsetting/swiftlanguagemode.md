# swiftLanguageMode(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Defines a `-language-mode` to pass  to the corresponding build tool.

**Availability**:
- SwiftPM 6.0+

## Declaration

```swift
static func swiftLanguageMode(_ mode: SwiftLanguageMode, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

> **Note**: First available in PackageDescription 6.0.

First available in PackageDescription 6.0.

## Parameters

- `mode`: The Swift language mode to use.
- `condition`: A condition that restricts the application of the build setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/swiftlanguagemode(_:_:))*