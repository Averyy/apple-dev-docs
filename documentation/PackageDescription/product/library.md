# Product.Library

**Framework**: PackageDescription  
**Kind**: class  
**Role**: Class

The library product of a Swift package.

## Declaration

```swift
final class Library
```

## Topics

### Describing a Library Product
- [let targets: [String]](./library/targets.md)
  The names of the targets in this product.
- [let type: Product.Library.LibraryType?](./library/type.md)
  The type of the library.
- [Product.Library.LibraryType](./library/librarytype.md)
  The different types of a library product.

## Relationships

### Inherits From
- [Product](../product.md)
### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Library Product
- [static func library(name: String, type: Product.Library.LibraryType?, targets: [String]) -> Product](./library%28name,type,targets%29.md)
  Creates a library product to allow clients that declare a dependency on this package to use the package’s functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/product/library)*