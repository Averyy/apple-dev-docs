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

## Parameters

- `traits`: The set of traits that enable the dependencies trait. If any of the traits are enabled on this package   the dependencies trait will be enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/trait/condition-swift.struct/when(traits:))*