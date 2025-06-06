# when(platforms:traits:)

**Framework**: PackageDescription  
**Kind**: method

Creates a target dependency condition.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func when(platforms: [Platform], traits: Set<String>) -> TargetDependencyCondition?
```

## Parameters

- `platforms`: The applicable platforms for this target dependency condition.
- `traits`: The applicable traits for this target dependency condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/targetdependencycondition/when(platforms:traits:))*