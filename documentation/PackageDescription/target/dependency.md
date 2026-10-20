# Target.Dependency

**Framework**: PackageDescription  
**Kind**: enum  
**Role**: Enumeration

The different types of a target’s dependency on another entity.

## Declaration

```swift
enum Dependency
```

## Topics

### Creating a Target Dependency
- [static func product(name: String, package: String, moduleAliases: [String : String]?, condition: TargetDependencyCondition?) -> Target.Dependency](./dependency/product%28name,package,modulealiases,condition%29.md)
  Creates a target dependency on a product from a package dependency.
- [case productItem(name: String, package: String?, moduleAliases: [String : String]?, condition: TargetDependencyCondition?)](./dependency/productitem%28name,package,modulealiases,condition%29.md)
  A dependency on a product.
- [static func target(name: String, condition: TargetDependencyCondition?) -> Target.Dependency](./dependency/target%28name,condition%29.md)
  Creates a dependency on a target in the same package.
- [case targetItem(name: String, condition: TargetDependencyCondition?)](./dependency/targetitem%28name,condition%29.md)
  A dependency on a target.
- [static func byName(name: String, condition: TargetDependencyCondition?) -> Target.Dependency](./dependency/byname%28name,condition%29.md)
  Creates a dependency that resolves to either a target or a product with the specified name.
- [case byNameItem(name: String, condition: TargetDependencyCondition?)](./dependency/bynameitem%28name,condition%29.md)
  A by-name dependency on either a target or a product.
- [struct TargetDependencyCondition](../targetdependencycondition.md)
  A condition that limits the application of a target’s dependency.
- [init(stringLiteral: String)](./dependency/init%28stringliteral%29.md)
  Creates a target dependency instance with the given value.
- [static func product(name: String, package: String, condition: TargetDependencyCondition?) -> Target.Dependency](./dependency/product%28name,package,condition%29.md)
  Creates a target dependency on a product from a package dependency.
- [static func product(name: String, package: String?) -> Target.Dependency](./dependency/product%28name,package%29-fp0j.md)
  Creates a dependency on a product from a package dependency.
- [static func product(name: String, package: String) -> Target.Dependency](./dependency/product%28name,package%29-2nako.md)
  Creates a dependency on a product from a package dependency.
- [static func productItem(name: String, package: String?, condition: TargetDependencyCondition?) -> Target.Dependency](./dependency/productitem%28name,package,condition%29.md)
- [static func target(name: String) -> Target.Dependency](./dependency/target%28name%29.md)
  Creates a dependency on a target in the same package.
- [static func byName(name: String) -> Target.Dependency](./dependency/byname%28name%29.md)
  Creates a dependency that resolves to either a target or a product with the specified name.
### Default Implementations
- [ExpressibleByStringLiteral Implementations](./dependency/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Declaring a Dependency Target
- [var dependencies: [Target.Dependency]](./dependencies.md)
  The target’s dependencies on other entities inside or outside the package.
- [struct TargetDependencyCondition](../targetdependencycondition.md)
  A condition that limits the application of a target’s dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/dependency)*