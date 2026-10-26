---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/products"
framework: "Swift-Org/PackagePlugin"
---

# products

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

Any regular products defined in this package, with the exception of plugin products.

## Declaration

```swift
let products: [Product]
```

#### Discussion

The products are specified in the same order as the package manifest.

## See Also

### Inspecting Package Products
- [func products(named: [String]) throws -> [Product]](./products%28named%29.md)
  The list of products matching the given names.
- [func products<T>(ofType: T.Type) -> [T]](./products%28oftype%29.md)
  The products in this package that conform to a specific type.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/products)*