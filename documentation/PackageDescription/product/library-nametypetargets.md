# library(name:type:targets:)

**Framework**: PackageDescription  
**Kind**: method

Creates a library product to allow clients that declare a dependency on this package to use the package’s functionality.

## Declaration

```swift
static func library(name: String, type: Product.Library.LibraryType? = nil, targets: [String]) -> Product
```

#### Return Value

A `Product` instance.

#### Discussion

A library’s product can be either statically or dynamically linked. It’s recommended that you don’t explicitly declare the type of library, so Swift Package Manager can choose between static or dynamic linking based on the preference of the package’s consumer.

## Parameters

- `name`: The name of the library product.
- `type`: The optional type of the library that’s used to determine how to   link to the library. Leave this parameter so   Swift Package Manager can choose between static or dynamic linking (recommended). If you   don’t support both linkage types, use    or    for this parameter.
- `targets`: The targets that are bundled into a library product.

## See Also

- [Product.Library](product/library.md)
  The library product of a Swift package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/product/library(name:type:targets:))*