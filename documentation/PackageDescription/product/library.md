# Product.Library

**Framework**: PackageDescription  
**Kind**: class

The library product of a Swift package.

## Declaration

```swift
final class Library
```

## Topics

### Describing a Library Product
- [let targets: [String]](product/library/targets.md)
  The names of the targets in this product.
- [let type: Product.Library.LibraryType?](product/library/type.md)
  The type of the library.
- [Product.Library.LibraryType](product/library/librarytype.md)
  The different types of a library product.

## Relationships

### Inherits From
- [Product](product.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func library(name: String, type: Product.Library.LibraryType?, targets: [String]) -> Product](product/library(name:type:targets:).md)
  Creates a library product to allow clients that declare a dependency on this package to use the package’s functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/product/library)*