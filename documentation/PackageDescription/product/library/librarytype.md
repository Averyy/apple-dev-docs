# Product.Library.LibraryType

**Framework**: PackageDescription  
**Kind**: enum

The different types of a library product.

## Declaration

```swift
enum LibraryType
```

## Topics

### Enumeration Cases
- [Product.Library.LibraryType.dynamic](product/library/librarytype/dynamic.md)
  A dynamically linked library.
- [Product.Library.LibraryType.static](product/library/librarytype/static.md)
  A statically linked library.
### Hashing
- [func hash(into: inout Hasher)](product/library/librarytype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](product/library/librarytype/hashvalue.md)
  The library type’s hash value.
### Operator Functions
- [static func != (Self, Self) -> Bool](product/library/librarytype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Creating a Value
- [init?(rawValue: String)](product/library/librarytype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](product/library/librarytype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [Product.Library.LibraryType.RawValue](product/library/librarytype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](product/library/librarytype/equatable-implementations.md)
- [RawRepresentable Implementations](product/library/librarytype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [let targets: [String]](product/library/targets.md)
  The names of the targets in this product.
- [let type: Product.Library.LibraryType?](product/library/type.md)
  The type of the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/product/library/librarytype)*