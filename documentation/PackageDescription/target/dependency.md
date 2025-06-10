# Target.Dependency

**Framework**: PackageDescription  
**Kind**: enum

The different types of a target’s dependency on another entity.

## Declaration

```swift
enum Dependency
```

## Topics

### Creating a Target Dependency
- [static func product(name: String, package: String, moduleAliases: [String : String]?, condition: TargetDependencyCondition?) -> Target.Dependency](target/dependency/product(name:package:modulealiases:condition:).md)
  Creates a target dependency on a product from a package dependency.
- [case productItem(name: String, package: String?, moduleAliases: [String : String]?, condition: TargetDependencyCondition?)](target/dependency/productitem(name:package:modulealiases:condition:).md)
  A dependency on a product.
- [static func target(name: String, condition: TargetDependencyCondition?) -> Target.Dependency](target/dependency/target(name:condition:).md)
  Creates a dependency on a target in the same package.
- [case targetItem(name: String, condition: TargetDependencyCondition?)](target/dependency/targetitem(name:condition:).md)
  A dependency on a target.
- [static func byName(name: String, condition: TargetDependencyCondition?) -> Target.Dependency](target/dependency/byname(name:condition:).md)
  Creates a dependency that resolves to either a target or a product with the specified name.
- [case byNameItem(name: String, condition: TargetDependencyCondition?)](target/dependency/bynameitem(name:condition:).md)
  A by-name dependency on either a target or a product.
- [struct TargetDependencyCondition](targetdependencycondition.md)
  A condition that limits the application of a target’s dependency.
- [init(stringLiteral: String)](target/dependency/init(stringliteral:).md)
  Creates a target dependency instance with the given value.
- [static func product(name: String, package: String, condition: TargetDependencyCondition?) -> Target.Dependency](target/dependency/product(name:package:condition:).md)
  Creates a target dependency on a product from a package dependency.
- [static func product(name: String, package: String?) -> Target.Dependency](target/dependency/product(name:package:)-fp0j.md)
  Creates a dependency on a product from a package dependency.
- [static func product(name: String, package: String) -> Target.Dependency](target/dependency/product(name:package:)-2nako.md)
  Creates a dependency on a product from a package dependency.
- [static func productItem(name: String, package: String?, condition: TargetDependencyCondition?) -> Target.Dependency](target/dependency/productitem(name:package:condition:).md)
- [static func target(name: String) -> Target.Dependency](target/dependency/target(name:).md)
  Creates a dependency on a target in the same package.
- [static func byName(name: String) -> Target.Dependency](target/dependency/byname(name:).md)
  Creates a dependency that resolves to either a target or a product with the specified name.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](target/dependency/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](target/dependency/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](target/dependency/expressiblebyunicodescalarliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var dependencies: [Target.Dependency]](target/dependencies.md)
  The target’s dependencies on other entities inside or outside the package.
- [struct TargetDependencyCondition](targetdependencycondition.md)
  A condition that limits the application of a target’s dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/dependency)*