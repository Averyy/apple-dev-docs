# Product

**Framework**: PackageDescription  
**Kind**: class

The object that defines a package product.

## Declaration

```swift
class Product
```

#### Overview

A package product defines an externally visible build artifact that’s available to clients of a package. Swift Package Manager assembles the product from the build artifacts of one or more of the package’s targets. A package product can be one of three types:

The following example shows a package manifest for a library called “Paper” that defines multiple products:

```swift
let package = Package(
    name: "Paper",
    products: [
        .executable(name: "tool", targets: ["tool"]),
        .library(name: "Paper", targets: ["Paper"]),
        .library(name: "PaperStatic", type: .static, targets: ["Paper"]),
        .library(name: "PaperDynamic", type: .dynamic, targets: ["Paper"]),
    ],
    dependencies: [
        .package(url: "http://example.com.com/ExamplePackage/ExamplePackage", from: "1.2.3"),
        .package(url: "http://some/other/lib", .exact("1.2.3")),
    ],
    targets: [
        .executableTarget(
            name: "tool",
            dependencies: [
                "Paper",
                "ExamplePackage"
            ]),
        .target(
            name: "Paper",
            dependencies: [
                "Basic",
                .target(name: "Utility"),
                .product(name: "AnotherExamplePackage"),
            ])
    ]
)
```

## Topics

### Creating a Library Product
- [static func library(name: String, type: Product.Library.LibraryType?, targets: [String]) -> Product](product/library(name:type:targets:).md)
  Creates a library product to allow clients that declare a dependency on this package to use the package’s functionality.
- [Product.Library](product/library.md)
  The library product of a Swift package.
### Creating an Executable Product
- [static func executable(name: String, targets: [String]) -> Product](product/executable(name:targets:).md)
  Creates an executable package product.
- [Product.Executable](product/executable.md)
  The executable product of a Swift package.
### Creating a Plugin Product
- [static func plugin(name: String, targets: [String]) -> Product](product/plugin(name:targets:).md)
  Defines a product that vends a package plugin target for use by clients of the package.
- [Product.Plugin](product/plugin.md)
  The plug-in product of a Swift package.
### Naming the product
- [let name: String](product/name.md)
  The name of the package product.

## Relationships

### Inherited By
- [Product.Executable](product/executable.md)
- [Product.Library](product/library.md)
- [Product.Plugin](product/plugin.md)

## See Also

- [var products: [Product]](package/products.md)
  The list of products that this package vends and that clients can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/product)*