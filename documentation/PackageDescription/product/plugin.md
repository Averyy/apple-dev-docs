# Product.Plugin

**Framework**: PackageDescription  
**Kind**: class

The plug-in product of a Swift package.

## Declaration

```swift
final class Plugin
```

## Topics

### Describing a plug-in product
- [let targets: [String]](product/plugin/targets.md)
  The name of the plug-in target to vend as a product.

## Relationships

### Inherits From
- [Product](product.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func plugin(name: String, targets: [String]) -> Product](product/plugin(name:targets:).md)
  Defines a product that vends a package plugin target for use by clients of the package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/product/plugin)*