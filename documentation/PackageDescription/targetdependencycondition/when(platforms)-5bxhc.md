# when(platforms:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Creates a target dependency condition.

**Availability**:
- SwiftPM 5.7+

## Declaration

```swift
static func when(platforms: [Platform]) -> TargetDependencyCondition?
```

## Parameters

- `platforms`: The applicable platforms for this target dependency condition.

## See Also

### Creating a Dependency Condition
- [static func when(traits: Set<String>) -> TargetDependencyCondition?](./when%28traits%29.md)
  Creates a target dependency condition.
- [static func when(platforms: [Platform], traits: Set<String>) -> TargetDependencyCondition?](./when%28platforms,traits%29.md)
  Creates a target dependency condition.
- [static func when(platforms: [Platform]?) -> TargetDependencyCondition](./when%28platforms%29-4djh6.md)
  Creates a target dependency condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/targetdependencycondition/when(platforms:)-5bxhc)*