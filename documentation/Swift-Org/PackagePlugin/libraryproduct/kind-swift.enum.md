---
url: "https://docs.swift.org/latest/documentation/packageplugin/libraryproduct/kind-swift.enum"
framework: "Swift-Org/PackagePlugin"
---

# LibraryProduct.Kind

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

The kind of library product.

## Declaration

```swift
enum Kind
```

## Topics

### Kinds of Library Targets
- [LibraryProduct.Kind.automatic](./kind-swift.enum/automatic.md)
  The kind of library produced is unspecified and will be determined by the build system based on how the library is used.
- [LibraryProduct.Kind.dynamic](./kind-swift.enum/dynamic.md)
  Dynamic library, whose code is referenced by its clients.
- [LibraryProduct.Kind.static](./kind-swift.enum/static.md)
  A static library, whose code is copied into its clients.
### Default Implementations
- [Equatable Implementations](./kind-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable

## See Also

### Inspecting a Library Product
- [let id: ID](./id.md)
  Unique identifier for the product.
- [let name: String](./name.md)
  The name of the product, as defined in the package manifest.
- [let kind: Kind](./kind-swift.property.md)
  A value that indicates whether the library is static, dynamic, or automatically determined.
- [let targets: [Target]](./targets.md)
  The targets that directly comprise the product, in the order in which they are declared in the package manifest.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/libraryproduct/kind-swift.enum)*