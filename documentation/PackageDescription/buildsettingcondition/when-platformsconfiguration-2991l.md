# when(platforms:configuration:)

**Framework**: PackageDescription  
**Kind**: method

Creates a build setting condition.

**Availability**:
- SwiftPM ?+

## Declaration

```swift
static func when(platforms: [Platform]? = nil, configuration: BuildConfiguration? = nil) -> BuildSettingCondition
```

## Parameters

- `platforms`: The applicable platforms for this build setting condition.
- `configuration`: The applicable build configuration for this build setting condition.

## See Also

- [static func when(platforms: [Platform]) -> BuildSettingCondition](buildsettingcondition/when(platforms:).md)
  Creates a build setting condition.
- [static func when(configuration: BuildConfiguration) -> BuildSettingCondition](buildsettingcondition/when(configuration:).md)
  Creates a build setting condition.
- [static func when(platforms: [Platform], configuration: BuildConfiguration) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:)-475co.md)
  Creates a build setting condition.
- [static func when(platforms: [Platform]?, configuration: BuildConfiguration?, traits: Set<String>?) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:traits:).md)
  Creates a build setting condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/buildsettingcondition/when(platforms:configuration:)-2991l)*