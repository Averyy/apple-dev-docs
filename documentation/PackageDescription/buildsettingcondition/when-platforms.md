# when(platforms:)

**Framework**: PackageDescription  
**Kind**: method

Creates a build setting condition.

**Availability**:
- SwiftPM 5.7+

## Declaration

```swift
static func when(platforms: [Platform]) -> BuildSettingCondition
```

## Parameters

- `platforms`: The applicable platforms for this build setting condition.

## See Also

- [static func when(configuration: BuildConfiguration) -> BuildSettingCondition](buildsettingcondition/when(configuration:).md)
  Creates a build setting condition.
- [static func when(platforms: [Platform], configuration: BuildConfiguration) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:)-475co.md)
  Creates a build setting condition.
- [static func when(platforms: [Platform]?, configuration: BuildConfiguration?, traits: Set<String>?) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:traits:).md)
  Creates a build setting condition.
- [static func when(platforms: [Platform]?, configuration: BuildConfiguration?) -> BuildSettingCondition](buildsettingcondition/when(platforms:configuration:)-2991l.md)
  Creates a build setting condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/buildsettingcondition/when(platforms:))*