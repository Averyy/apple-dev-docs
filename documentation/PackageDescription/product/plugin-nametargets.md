# plugin(name:targets:)

**Framework**: PackageDescription  
**Kind**: method

Defines a product that vends a package plugin target for use by clients of the package.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func plugin(name: String, targets: [String]) -> Product
```

#### Return Value

A `Product` instance.

#### Discussion

It is not necessary to define a product for a plugin that is only used within the same package where you define it. All the targets listed must be plugin targets in the same package as the product. Swift Package Manager will apply them to any client targets of the product in the order they are listed.

## Parameters

- `name`: The name of the plugin product.
- `targets`: The plugin targets to vend as a product.

## See Also

- [Product.Plugin](product/plugin.md)
  The plug-in product of a Swift package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/product/plugin(name:targets:))*