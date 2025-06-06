# swiftLanguageVersion(_:_:)

**Framework**: Packagedescription  
**Kind**: method

Defines a `-swift-version` to pass  to the corresponding build tool.

**Availability**:
- SwiftPM 6.0+

## Declaration

```swift
static func swiftLanguageVersion(_ version: SwiftVersion, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

> **Note**: First available in PackageDescription 6.0.

## Parameters

- `version`: The Swift language version to use.
- `condition`: A condition that restricts the application of the build setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/swiftlanguageversion(_:_:))*