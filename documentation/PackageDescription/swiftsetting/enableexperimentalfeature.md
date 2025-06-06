# enableExperimentalFeature(_:_:)

**Framework**: Packagedescription  
**Kind**: method

Enable an experimental feature with the given name.

**Availability**:
- SwiftPM 5.8+

## Declaration

```swift
static func enableExperimentalFeature(_ name: String, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

An experimental feature is one that’s in development, but is not yet available in Swift as a language feature.

You can add and use multiple experimental features in a given target without affecting its dependencies. Targets will ignore any  unknown experimental features.

> **Note**: First available in PackageDescription 5.8.

## Parameters

- `name`: The name of the experimental feature; for example,  .
- `condition`: A condition that restricts the application of the build   setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/enableexperimentalfeature(_:_:))*