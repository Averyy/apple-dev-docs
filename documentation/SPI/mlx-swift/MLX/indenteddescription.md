---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/indenteddescription"
framework: "mlx-swift/MLX"
---

# IndentedDescription

**Framework**: mlx-swift/MLX  
**Kind**: protocol  
**Role**: Protocol

Protocol for types that can provide an indented description, e.g. nested types.

## Declaration

```swift
protocol IndentedDescription : CustomStringConvertible
```

## Topics

### Instance Methods
- [func description(indent: Int) -> String](./indenteddescription/description%28indent%29.md)
  Return the `description` with the given indent level.
### Default Implementations
- [CustomStringConvertible Implementations](./indenteddescription/customstringconvertible-implementations.md)

## Relationships

### Inherits From
- Swift.CustomStringConvertible
### Conforming Types
- [NestedItem](./nesteditem.md)

## See Also

### Nested Data
- [struct NestedDictionary](./nesteddictionary.md)
  Nested structure of arrays, dictionaries and values.
- [enum NestedItem](./nesteditem.md)
  Backing storage for [`NestedDictionary`](./nesteddictionary.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/indenteddescription)*