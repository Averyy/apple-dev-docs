# when(platforms:configuration:traits:)

**Framework**: PackageDescription  
**Kind**: method

Creates a build setting condition.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func when(platforms: [Platform]? = nil, configuration: BuildConfiguration? = nil, traits: Set<String>? = nil) -> BuildSettingCondition
```

## Parameters

- `platforms`: The applicable platforms for this build setting condition.
- `configuration`: The applicable build configuration for this build setting condition.
- `traits`: The applicable traits for this build setting condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/buildsettingcondition/when(platforms:configuration:traits:))*