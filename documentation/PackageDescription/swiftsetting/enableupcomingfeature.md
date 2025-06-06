# enableUpcomingFeature(_:_:)

**Framework**: PackageDescription  
**Kind**: method

Enable an upcoming feature with the given name.

**Availability**:
- SwiftPM 5.8+

## Declaration

```swift
static func enableUpcomingFeature(_ name: String, _ condition: BuildSettingCondition? = nil) -> SwiftSetting
```

#### Discussion

An upcoming feature is one that is available in Swift as of a certain language version, but isn’t available by default in prior language modes because it has some impact on source compatibility.

You can add and use multiple upcoming features in a given target without affecting its dependencies. Targets will ignore any unknown upcoming features.

> **Note**: First available in PackageDescription 5.8.

First available in PackageDescription 5.8.

## Parameters

- `name`: The name of the upcoming feature; for example,  .
- `condition`: A condition that restricts the application of the build   setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/swiftsetting/enableupcomingfeature(_:_:))*