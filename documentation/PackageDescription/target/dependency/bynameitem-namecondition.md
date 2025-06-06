# Target.Dependency.byNameItem(name:condition:)

**Framework**: PackageDescription  
**Kind**: case

A by-name dependency on either a target or a product.

## Declaration

```swift
case byNameItem(name: String, condition: TargetDependencyCondition?)
```

## Parameters

- `name`: The name of the dependency, either a target or a product.
- `condition`: A condition that limits the application of the target   dependency. For example, only apply a dependency for a specific   platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/dependency/bynameitem(name:condition:))*