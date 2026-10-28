---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/products(named:)"
framework: "Swift-Org/PackagePlugin"
---

# products(named:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

The list of products matching the given names.

## Declaration

```swift
func products(named productNames: [String]) throws -> [Product]
```

## Discussion

Throws an error if any of the products cannot be found.

## See Also

### Inspecting Package Products
- [let products: [Product]](./products.md)
  Any regular products defined in this package, with the exception of plugin products.
- [func products<T>(ofType: T.Type) -> [T]](./products%28oftype%29.md)
  The products in this package that conform to a specific type.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/products(named:))*