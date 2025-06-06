# TargetDependencyCondition

**Framework**: PackageDescription  
**Kind**: struct

A condition that limits the application of a target’s dependency.

## Declaration

```swift
struct TargetDependencyCondition
```

## Topics

### Creating a Dependency Condition
- [static func when(platforms: [Platform]) -> TargetDependencyCondition?](targetdependencycondition/when(platforms:)-5bxhc.md)
  Creates a target dependency condition.
- [static func when(platforms: [Platform]?) -> TargetDependencyCondition](targetdependencycondition/when(platforms:)-4djh6.md)
  Creates a target dependency condition.
### Type Methods
- [static func when(platforms: [Platform], traits: Set<String>) -> TargetDependencyCondition?](targetdependencycondition/when(platforms:traits:).md)
  Creates a target dependency condition.
- [static func when(traits: Set<String>) -> TargetDependencyCondition?](targetdependencycondition/when(traits:).md)
  Creates a target dependency condition.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var dependencies: [Target.Dependency]](target/dependencies.md)
  The target’s dependencies on other entities inside or outside the package.
- [Target.Dependency](target/dependency.md)
  The different types of a target’s dependency on another entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/targetdependencycondition)*