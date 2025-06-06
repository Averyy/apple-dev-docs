# byName(name:condition:)

**Framework**: PackageDescription  
**Kind**: method

Creates a dependency that resolves to either a target or a product with the specified name.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
static func byName(name: String, condition: TargetDependencyCondition? = nil) -> Target.Dependency
```

#### Return Value

A `Target.Dependency` instance.

#### Discussion

Swift Package Manager creates the by-name dependency after it has loaded the package graph.

## Parameters

- `name`: The name of the dependency, either a target or a product.
- `condition`: A condition that limits the application of the target   dependency. For example, only apply a dependency for a specific   platform.

## See Also

- [static func product(name: String, package: String, condition: TargetDependencyCondition?) -> Target.Dependency](target/dependency/product(name:package:condition:).md)
  Creates a target dependency on a product from a package dependency.
- [static func product(name: String, package: String?) -> Target.Dependency](target/dependency/product(name:package:)-fp0j.md)
  Creates a dependency on a product from a package dependency.
- [static func product(name: String, package: String) -> Target.Dependency](target/dependency/product(name:package:)-2nako.md)
  Creates a dependency on a product from a package dependency.
- [static func product(name: String, package: String, moduleAliases: [String : String]?, condition: TargetDependencyCondition?) -> Target.Dependency](target/dependency/product(name:package:modulealiases:condition:).md)
  Creates a target dependency on a product from a package dependency.
- [static func target(name: String, condition: TargetDependencyCondition?) -> Target.Dependency](target/dependency/target(name:condition:).md)
  Creates a dependency on a target in the same package.
- [static func target(name: String) -> Target.Dependency](target/dependency/target(name:).md)
  Creates a dependency on a target in the same package.
- [static func byName(name: String) -> Target.Dependency](target/dependency/byname(name:).md)
  Creates a dependency that resolves to either a target or a product with the specified name.
- [struct TargetDependencyCondition](targetdependencycondition.md)
  A condition that limits the application of a target’s dependency.
- [init(stringLiteral: String)](target/dependency/init(stringliteral:).md)
  Creates a target dependency instance with the given value.
- [init(extendedGraphemeClusterLiteral: Self.StringLiteralType)](target/dependency/init(extendedgraphemeclusterliteral:).md)
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](target/dependency/init(unicodescalarliteral:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/dependency/byname(name:condition:))*