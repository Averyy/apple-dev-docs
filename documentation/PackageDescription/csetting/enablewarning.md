# enableWarning(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Enable a specific C compiler warning group.

**Availability**:
- SwiftPM 6.2+

## Declaration

```swift
static func enableWarning(_ name: String, _ condition: BuildSettingCondition? = nil) -> CSetting
```

#### Discussion

Use this setting to enable a specific warning group. This is equivalent to passing `-W` followed by the group name to the C compiler.

> **Note**: First available in PackageDescription 6.2.

## Parameters

- `name`: The name of the warning group to enable.
- `condition`: A condition that restricts the application of the build setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/csetting/enablewarning(_:_:))*