# Target.Dependency.productItem(name:package:moduleAliases:condition:)

**Framework**: PackageDescription  
**Kind**: case

A dependency on a product.

## Declaration

```swift
case productItem(name: String, package: String?, moduleAliases: [String : String]?, condition: TargetDependencyCondition?)
```

## Parameters

- `name`: The name of the product.
- `package`: The name of the package.
- `moduleAlias`: The module aliases for targets in the product.
- `condition`: A condition that limits the application of the target dependency. For example, only apply a dependency for a specific platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/dependency/productitem(name:package:modulealiases:condition:))*