# when(traits:)

**Framework**: PackageDescription  
**Kind**: method

Creates a package dependency trait condition.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func when(traits: Set<String>) -> Package.Dependency.Trait.Condition?
```

#### Discussion

If the depending package enables any of the traits you provide, the package manager enables the dependency to which this condition applies.

## Parameters

- `traits`: The set of traits that enable the dependencies trait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/trait/condition-swift.struct/when(traits:))*