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

## See Also

- [static func when(platforms: [Platform]) -> BuildSettingCondition](buildsettingcondition/when(platforms:).md)
  Creates a build setting condition.
- [static func when(configuration: BuildConfiguration) -> BuildSettingCondition](buildsettingcondition/when(configuration:).md)
  Creates a build setting condition.
- [static func when(platforms: [Platform], configuration: BuildConfiguration) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:)-475co.md)
  Creates a build setting condition.
- [static func when(platforms: [Platform]?, configuration: BuildConfiguration?) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:)-2991l.md)
  Creates a build setting condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/buildsettingcondition/when(platforms:configuration:traits:))*