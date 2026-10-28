# target(name:condition:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Creates a dependency on a target in the same package.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
static func target(name: String, condition: TargetDependencyCondition? = nil) -> Target.Dependency
```

## Return Value

A `Target.Dependency` instance.

## Parameters

- `name`: The name of the target.
- `condition`: A condition that limits the application of the target dependency. For example, only apply a dependency for a specific platform.

## See Also

### Creating a Target Dependency
- [static func product(name: String, package: String, moduleAliases: [String : String]?, condition: TargetDependencyCondition?) -> Target.Dependency](./product%28name,package,modulealiases,condition%29.md)
  Creates a target dependency on a product from a package dependency.
- [case productItem(name: String, package: String?, moduleAliases: [String : String]?, condition: TargetDependencyCondition?)](./productitem%28name,package,modulealiases,condition%29.md)
  A dependency on a product.
- [case targetItem(name: String, condition: TargetDependencyCondition?)](./targetitem%28name,condition%29.md)
  A dependency on a target.
- [static func byName(name: String, condition: TargetDependencyCondition?) -> Target.Dependency](./byname%28name,condition%29.md)
  Creates a dependency that resolves to either a target or a product with the specified name.
- [case byNameItem(name: String, condition: TargetDependencyCondition?)](./bynameitem%28name,condition%29.md)
  A by-name dependency on either a target or a product.
- [struct TargetDependencyCondition](../../targetdependencycondition.md)
  A condition that limits the application of a target’s dependency.
- [init(stringLiteral: String)](./init%28stringliteral%29.md)
  Creates a target dependency instance with the given value.
- [static func product(name: String, package: String, condition: TargetDependencyCondition?) -> Target.Dependency](./product%28name,package,condition%29.md)
  Creates a target dependency on a product from a package dependency.
- [static func product(name: String, package: String?) -> Target.Dependency](./product%28name,package%29-fp0j.md)
  Creates a dependency on a product from a package dependency.
- [static func product(name: String, package: String) -> Target.Dependency](./product%28name,package%29-2nako.md)
  Creates a dependency on a product from a package dependency.
- [static func productItem(name: String, package: String?, condition: TargetDependencyCondition?) -> Target.Dependency](./productitem%28name,package,condition%29.md)
- [static func target(name: String) -> Target.Dependency](./target%28name%29.md)
  Creates a dependency on a target in the same package.
- [static func byName(name: String) -> Target.Dependency](./byname%28name%29.md)
  Creates a dependency that resolves to either a target or a product with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/dependency/target(name:condition:))*