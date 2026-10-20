# when(platforms:configuration:traits:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

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

### Checking for a Build Condition
- [static func when(platforms: [Platform]) -> BuildSettingCondition](./when%28platforms%29.md)
  Creates a build setting condition.
- [static func when(configuration: BuildConfiguration) -> BuildSettingCondition](./when%28configuration%29.md)
  Creates a build setting condition.
- [static func when(platforms: [Platform], configuration: BuildConfiguration) -> BuildSettingCondition](./when%28platforms,configuration%29-475co.md)
  Creates a build setting condition.
- [static func when(platforms: [Platform]?, configuration: BuildConfiguration?) -> BuildSettingCondition](./when%28platforms,configuration%29-2991l.md)
  Creates a build setting condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/buildsettingcondition/when(platforms:configuration:traits:))*